# to pandas serializer

import pandas as pd
from .__to_json import to_json


def to_pandas(objects_list: list) -> pd.DataFrame:
	"""
	Get objects and convert it pandas DataFrame
	:param objects_list:
	:return:
	"""
	try:
		if objects_list[0].__class__.__name__ == "FF":
			return pd.DataFrame(to_json(objects_list))
		elif objects_list[0].__class__.__name__ == "Timeline":
			return pd.DataFrame(to_json(objects_list))
		elif objects_list[0].__class__.__name__ == "Profile":
			return pd.DataFrame(to_json(objects_list))
	except IndexError:
		return pd.DataFrame()
