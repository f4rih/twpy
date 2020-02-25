
# Grabber Engine
import time
from datetime import datetime
from ..exceptions import QueryError, ParameterRequired
from .request import RequestHandler
from ..config.config import BASE_URL, MOBILE_URL, TIMELINE_WITH_TOKEN_QUERY, APIV1_URL
from ..utils import extract_cursor, extract_ff, extract_timeline_cursor, extract_timeline, extract_profile
from time import sleep


def follower_following(
		username: str, limit: int = 0,
		type_: str = "followers",
		proxy: str = None,
		interval: int = 0) -> list:
	"""
	Followers/Followings scraper
	:param username:
	:param limit:
	:param type_:
	:param proxy:
	:param interval:
	:return:
	"""
	result: list = []
	cursor: str = str()
	first_request: bool = True
	has_more: bool = True
	# mode = FF -> followers/followings user-agent
	req = RequestHandler(user_agent="FF")
	# if proxy enabled set it
	if proxy:
		req.proxy = proxy
	while has_more:
		if first_request:
			url = MOBILE_URL + f"/{username}/{type_}/?lang=en"
			res = req.get(url)
			first_request = False
		else:
			url = MOBILE_URL + f"/{username}/{type_}/?lang=en&cursor={cursor}"
			res = req.get(url)
		if res:
			# extract cursor
			cursor = extract_cursor(res)
			if cursor:
				has_more = True
			else:
				has_more = False

			# parse followers/followings
			extracted_ff = extract_ff(res)
			result.extend(extracted_ff)
			# if there was limit
			if limit > 0:
				if len(result) > limit:
					return result[:limit]
			else:
				sleep(interval)
				continue

		else:
			return result
		# interval
		sleep(interval)

	return result


def timeline(username: str, limit: int = 0, proxy: str = None, interval: int = 0) -> list:
	"""
	timeline scraper
	:param username:
	:param limit:
	:param proxy:
	:param interval:
	:return:
	"""
	result: list = []
	cursor = "-1"
	has_more = True
	req = RequestHandler(user_agent="TIMELINE", ret="json")
	if proxy:
		req.proxy = proxy

	while has_more:

		url = BASE_URL+TIMELINE_WITH_TOKEN_QUERY+f"+from:{username}"
		url = url.replace("%TOKEN%", cursor)
		res = req.get(url)
		if res:
			cursor, has_more = extract_timeline_cursor(response=res)
			extracted_tweets = extract_timeline(res['items_html'])
			result.extend(extracted_tweets)
			# check limitation
			if limit > 0:
				if len(result) > limit:
					return result[:limit]
			else:
				sleep(interval)
				continue
		else:
			return result

		sleep(interval)

	return result


def profile(username: str, proxy: str):
	"""
	get user profile
	"""
	
	req = RequestHandler(user_agent="MOBILE")
	if proxy:
		req.proxy = proxy
	url = BASE_URL+username+"/?lang=en"
	res = req.get(url=url)
	if res:
		return extract_profile(res)
	else:
		return None


def get_user_id(username: str, proxy: str):
	"""
	get user id
	"""

	req = RequestHandler(user_agent="TIMELINE", ret="json")
	if proxy:
		req.proxy = proxy
	url = APIV1_URL + username
	res = req.get(url=url)
	if res:
		return res.get('user_id', '')
	else:
		return ''


def search(username: str = "", since: str = "", until: str = "", query: str = "", limit: int = 0, verified: bool = False, proxy: str = "", interval: int = 0):
	"""Advanced search engine"""

	cursor: str = "-1"
	has_more: bool = True
	result: list = []
	req = RequestHandler(user_agent="TIMELINE", ret="json")
	if proxy:
		req.proxy = proxy

	if since:
		since = int(time.mktime(datetime.strptime(since, "%Y-%m-%d").timetuple()))

	if until:
		if len(until) == 4:
			until = f"{until}-01-01"

	query_structure = {
		"from": f"+from:{username}",
		"since": f"+since:{since}",
		"verified": ":verified",
		"until": f"+until:{until}",
		"query": f"+{query}"
	}

	if username and query:
		""" not allowed """
		raise QueryError("`username` and `query` parameter not allowed together.")

	if since and until:
		""" not allowed """
		raise QueryError("`since` and `until` parameter not allowed together.")

	url = BASE_URL+TIMELINE_WITH_TOKEN_QUERY
	url = url.replace("%TOKEN%", cursor)

	# if there was username or query
	if username or query:
		if username:
			url += query_structure['from']
		else:
			url += query_structure['query']

	# if username and query aren't set properly raise error
	else:
		raise ParameterRequired("`username` or `query` required for search.")

	if since or until:
		if since:
			url += query_structure['since']
		elif until:
			url += query_structure['until']

	if verified:
		url += query_structure['verified']

	while has_more:
		res = req.get(url=url)
		if res:
			cursor, has_more = extract_timeline_cursor(response=res)
			if cursor:
				extracted_tweets = extract_timeline(res['items_html'])
				result.extend(extracted_tweets)
				url = url.replace("%TOKEN%", cursor)
				# check limitation
				if limit > 0:
					if len(result) > limit:
						return result[:limit]
				else:
					sleep(interval)
					continue
			else:
				break
			sleep(interval)
		else:
			return result

	return result
