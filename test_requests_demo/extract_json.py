import requests
from jsonpath import jsonpath


def test_json():
	url="https://ceshiren.com/categories.json"
	r=requests.get(url)
	print(type(r))##格式为<class 'requests.models.Response'>
	# print(r.json())
	print(jsonpath(r.json(), '$..name'))


def test_get_dubhe_list():
	proxies = {
		'http': "http://127.0.0.1:8888",
		'https': "http://127.0.0.1:8888"
	}
	url = "https://pre-www.steamshop.net/api/goods/window/data?ename=index_fixed_business&cid=100000&platform=pc"
	# cookie={"sessionid":"d0ja52od4eu4drk9fvaicfvawug5359b"}
	r = requests.get(url,proxies=proxies)
	print(type(r))
	# print(r.json())
	print(jsonpath(r.json(), '$..name'))