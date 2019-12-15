
from .core.grabber import follower_following, timeline, profile


class TwpyClient(object):
	def __init__(self, proxy: str = "") -> None:
		"""
		Twpy client
		"""
		self.proxy = proxy

	def get_followers(self, username: str, interval: int = 0, limit: int = 0, user_id: bool = False) -> list:
		"""
		get user followers
		"""
		return follower_following(username=username, limit=limit, proxy=self.proxy, interval=interval)

	def get_friends(self, username: str, limit: int = 0, interval: int = 0, user_id: bool = False) -> list:
		"""
		get user friends
		"""
		return follower_following(username=username, limit=limit, proxy=self.proxy, type_="followings", interval=interval)

	def get_timeline(self, username: str, limit: int = 0, interval: int = 0) -> list:
		"""
		get user timeline
		"""
		return timeline(username=username, limit=limit, proxy=self.proxy, interval=interval)

	def get_user(self, username: str):
		"""
		get user profile info
		:param username:
		:return:
		"""
		return profile(username=username, proxy=self.proxy)
