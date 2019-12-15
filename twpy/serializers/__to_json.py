# to json serializer

import json


def to_json(objects_list: list) -> list:
	"""
	Get objects and convert it to json
	:param objects_list:
	:return:
	"""
	try:
		if objects_list[0].__class__.__name__ == "FF":
			return [obj.__dict__ for obj in objects_list]

		elif objects_list[0].__class__.__name__ == "Timeline":
			return [obj.__dict__ for obj in objects_list]
		elif objects_list[0].__class__.__name__ == "Profile":
			return [obj.__dict__ for obj in objects_list]
	except IndexError:
		return []
