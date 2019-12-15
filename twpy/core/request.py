# request handler
import requests
from ..utils import header_maker
import json


class RequestHandler:
	"""
	Handle all requests with specific user-agent
	"""
	def __init__(self, user_agent: str, ret: str = "text") -> None:
		self.user_agent = user_agent
		self.current_proxy = None
		self.ret = ret

	@property
	def proxy(self):
		return self.proxy

	@proxy.setter
	def proxy(self, new_proxy):
		self.current_proxy = new_proxy

	def get(self, url: str):
		"""
		make request
		:param url:
		:return:
		"""
		proxies = {
			"http": f"http://{self.current_proxy}",
			"https": f"https://{self.current_proxy}"
		}
		headers = {
			"User-Agent": header_maker(self.user_agent)
		}
		try:
			s = requests.Session()
			if self.current_proxy:
				res = s.get(url, headers=headers, proxies=proxies)
			else:
				res = s.get(url, headers=headers)
			if res.status_code == 200:
				# check return mode
				if self.ret == "text":
					return res.text
				else:
					return res.json()
			else:
				return None
		except requests.exceptions.ConnectionError:
			raise requests.exceptions.ConnectionError
		except json.decoder.JSONDecodeError:
			return None
