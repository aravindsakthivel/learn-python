import json

pre_json = {"name": "Aravind",
						'age': 27,
						'info': ["programmer"],
						'others': False,
						'more_info': ("Nothing Found", "none")
						}


json_dumped = json.dumps(pre_json, indent=2, sort_keys=True)
print(json_dumped)

print(json.loads(json_dumped))

# https://github.com/patrickloeber/python-engineer-notebooks/blob/master/advanced-python/11-JSON.ipynb
