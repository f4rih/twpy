
# Grabber Engine
from .request import RequestHandler
from ..config.config import BASE_URL, MOBILE_URL
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
	:param user_id:
	:return:
	"""
	result: list = []
	cursor: str = str()
	first_request: bool = True
	# mode = FF -> followers/followings user-agent
	req = RequestHandler(user_agent="FF")
	# if proxy enabled set it
	if proxy:
		req.proxy = proxy
	while True:
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
				break
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
	cursor: str = str()
	first_request = True
	has_more = True
	req = RequestHandler(user_agent="TIMELINE", ret="json")
	if proxy:
		req.proxy = proxy

	while True:
		if has_more is False:
			break
		if first_request:
			url = BASE_URL+f"/i/search/timeline?vertical=default&src=unkn&include_available_features=1&lang=en" \
						f"&include_entities=1&max_position=-1&reset_error_state=false&f=tweets&q=+from:{username} "
			res = req.get(url)
			first_request = False
			cursor, has_more = extract_timeline_cursor(response=res)
		else:
			url = BASE_URL+f"/i/search/timeline?vertical=default&src=unkn&include_available_features=1&lang=en" \
						f"&include_entities=1&max_position={cursor}&reset_error_state=false&f=tweets&q=+from:{username}"
			res = req.get(url)
		if res:
			cursor, has_more = extract_timeline_cursor(response=res)
			if cursor:
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
				break
		sleep(interval)

	return result


def profile(username: str, proxy: str):
	"""
	get user profile
	"""
	
	req = RequestHandler(user_agent="TIMELINE")
	if proxy:
		req.proxy = proxy
	url = BASE_URL+username+"/?lang=en"
	res = req.get(url=url)
	if res:
		return extract_profile(res)
	else:
		return None
