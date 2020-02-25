import re
from bs4 import BeautifulSoup
from ..models import FF, Timeline, Profile
import json


def header_maker(mode: str) -> str:
	"""
	make header and return as dict
	:param mode:
	:return:
	"""
	user_agents = {
		"FF": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36",
		"TIMELINE": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
		"MOBILE": "Opera/9.80 (Android 4.1.2; Linux; Opera Mobi/ADR-1305251841) Presto/2.11.355 Version/12.10"
	}

	return user_agents[mode]


def extract_cursor(html) -> str:
	"""
	extract token for next page
	:param html:
	:return:
	"""
	cursor = re.findall('cursor=(\d+)', html)
	if len(cursor) > 0:
		return cursor[0]
	else:
		return ""


def extract_timeline_cursor(response: json) -> tuple:
	"""
	Extract cursor from json
	:param response:
	:return:
	"""
	return response['min_position'], response['has_more_items']


def extract_ff(html: str) -> list:
	"""
	Extract followers/followings data from html
	:param html:
	:return:
	"""
	result: list = []
	soup = BeautifulSoup(html, 'html.parser')
	user_tables = soup.find_all('table', attrs={"class": "user-item"})
	if user_tables:
		for user in user_tables:
			avatar = user.find("img", attrs={"class": "profile-image"})['src']
			username = user.find("span", attrs={"class": "username"}).text.strip("@")
			fullname = user.find("strong", attrs={"class": "fullname"}).text
			# append to result list
			result.append(FF(username=username, avatar=avatar, fullname=fullname))
	return result


def extract_timeline(html: str) -> list:
	"""
	Extract tweets from timeline data
	:param html:
	:return:
	"""
	result: list = []
	soup = BeautifulSoup(html, 'html.parser')

	for li in soup.find_all('li', attrs={'class': 'js-stream-item stream-item stream-item'}):
		# find first div
		first_div = li.find('div')
		# user and tweet info
		tweet_id = first_div['data-tweet-id']
		tweet_link = first_div['data-permalink-path']
		conversation_id = first_div['data-conversation-id']
		is_reply = first_div.get('data-is-reply-to', "false")
		has_parent = first_div.get('data-has-parent-tweet', "false")
		screen_name = first_div['data-screen-name']
		name = first_div['data-name']
		user_id = first_div['data-user-id']
		user_mentions = first_div.get('data-mentions', 'false')
		if ' ' in user_mentions:
			user_mentions = [user for user in user_mentions.split(" ")]
		# get content info
		content = li.find('div', attrs={'class': 'js-tweet-text-container'}).text
		# tweet statistics
		reply_count = li.find('span', attrs={'class': 'ProfileTweet-action--reply u-hiddenVisually'}).text
		reply_count = reply_count.split(" ")[0].strip()
		retweet_count = li.find('span', attrs={'class': 'ProfileTweet-action--retweet u-hiddenVisually'}).text
		retweet_count = retweet_count.split(" ")[0].strip()
		likes_count = li.find('span', attrs={'class': 'ProfileTweet-action--favorite u-hiddenVisually'}).text
		likes_count = likes_count.split(" ")[0].strip()
		# time
		created_at = li.find('a', attrs={'class': 'tweet-timestamp js-permalink js-nav js-tooltip'})['title']
		#
		# add data to result
		result.append(Timeline(
			tweet_id=tweet_id,
			tweet_link=tweet_link,
			conversation_id=conversation_id,
			is_reply=is_reply,
			has_parent=has_parent,
			screen_name=screen_name,
			name=name,
			user_id=user_id,
			user_mentions=user_mentions,
			content=content,
			reply_count=reply_count,
			retweet_count=retweet_count,
			likes_count=likes_count,
			created_at=created_at
		))
	return result


def extract_profile(html: str) -> object:
	"""
	extract profile data
	:param html:
	:return:
	"""
	result: list = []

	soup = BeautifulSoup(html, 'html.parser')
	# get name
	name = soup.find('div', class_='fullname').text.strip()
	# verified account
	verified = soup.find('img', attrs={'alt': 'Verified Account'})
	if verified:
		verified = "true"
	else:
		verified = "false"
	# protected account
	protected = soup.find('div', class_='protected')
	if protected:
		protected = "true"
	else:
		protected = "false"
	# screen name
	username = soup.find('span', class_='screen-name').text.strip()
	# bio
	bio = soup.find('div', class_='bio').text.strip()
	# location
	location = soup.find('div', class_='location').text.strip()
	# url
	url = soup.find('div', class_='url').text.strip()
	# find profile info
	info = soup.find_all('div', class_='statnum')
	if info:
		tweet_count = info[0].text
		following_count = info[1].text
		follower_count = info[2].text
	else:
		tweet_count = 0
		following_count = 0
		follower_count = 0

	result.append(Profile(
		name=name,
		verified=verified,
		protected=protected,
		username=username,
		bio=bio,
		location=location,
		url=url,
		tweet_count=tweet_count,
		following_count=following_count,
		follower_count=follower_count
	))
	return result
