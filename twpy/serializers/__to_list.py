# to list serializer
def to_list(objects_list: list) -> list:
	"""
	Get objects and convert it to list
	:param objects_list:
	:return:
	"""
	try:
		if objects_list[0].__class__.__name__ == "FF":
			return [[obj.username, obj.avatar, obj.fullname] for obj in objects_list]

		elif objects_list[0].__class__.__name__ == "Timeline":
			return [[
				obj.tweet_id,
				obj.tweet_link,
				obj.conversation_id,
				obj.is_reply,
				obj.has_parent,
				obj.screen_name,
				obj.user_id,
				obj.user_mentions,
				obj.content,
				obj.reply_count,
				obj.retweet_count,
				obj.likes_count,
				obj.created_at] for obj in objects_list]
		elif objects_list[0].__class__.__name__ == "Profile":
			return [[
				obj.name,
				obj.verified,
				obj.protected,
				obj.username,
				obj.bio,
				obj.location,
				obj.url,
				obj.joined_date,
				obj.birthday,
				obj.user_id,
				obj.tweet_count,
				obj.following_count,
				obj.follower_count,
				obj.likes_count
			] for obj in objects_list]
	except IndexError:
		return []
