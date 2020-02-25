from .config.config import VERSION
from .core.grabber import follower_following, timeline, profile, search, get_user_id


class TwpyClient(object):

	def __init__(self, proxy: str = "") -> None:
		"""
		Twpy client
		:param proxy:
		"""
		self.proxy = proxy

	@property
	def __version__(self):
		return VERSION

	def get_followers(self, username: str, interval: int = 0, limit: int = 0) -> list:
		"""
		get user followers
		:param username:
		:param interval:
		:param limit:
		:return:
		"""
		return follower_following(username=username, limit=limit, proxy=self.proxy, interval=interval)

	def get_friends(self, username: str, limit: int = 0, interval: int = 0) -> list:
		"""
		get user friends
		:param username:
		:param limit:
		:param interval:
		:return:
		"""
		return follower_following(username=username, limit=limit, proxy=self.proxy, type_="followings", interval=interval)

	def get_timeline(self, username: str, limit: int = 0, interval: int = 0) -> list:
		"""
		get user timeline
		:param username:
		:param limit:
		:param interval:
		:return:
		"""
		return timeline(username=username, limit=limit, proxy=self.proxy, interval=interval)

	def get_user(self, username: str):
		"""
		get user profile info
		:param username:
		:return:
		"""
		return profile(username=username, proxy=self.proxy)

	def search(self, username: str = "", since: str = "", until: str = "", query: str = "", limit: int = 0, verified: bool = False, interval: int = 0):
		"""
		search tweets by given parameters
		:param username:
		:param since:
		:param until:
		:param query:
		:param limit:
		:param verified:
		:param interval:
		:return:
		"""
		return search(username=username, since=since, until=until, query=query, limit=limit, verified=verified, proxy=self.proxy, interval=interval)

	def get_user_id(self, username: str) -> str:
		"""
		Get user_id of user
		:param username
		:return: str
		"""
		return get_user_id(username=username, proxy=self.proxy)
