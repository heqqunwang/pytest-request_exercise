import requests
class Test_request:
	def setup_class(self):
		self.proxies = {
			'http': "http://127.0.0.1:8888",
			'https': "http://127.0.0.1:8888"
		}

	def test_proxies(self):
		proxies={
			'http':"http://127.0.0.1:8888",
			'https':"http://127.0.0.1:8888"
		}
		requests.get('https://ceshiren.com/t/topic/21093',proxies=proxies,verify=False)


	def test_headers(self):
		headers={"host":"dubhe.stnts.com",
		         "Cookie":"sessionid=vic6a5foqqyqxqdb4w7x86zruka4pm71",
		         "Accept":"application/json, text/plain, */*"
		         }
		url="http://dubhe.stnts.com/api/product/19/bug/list"
		r=requests.post(url=url,headers=headers)
		print(r.request.headers)

	def test_cookie(self):
		url = "http://dubhe.stnts.com/api/product/19/bug/list"
		headers = {"host": "dubhe.stnts.com",
		           "Accept":"application/json, text/plain, */*"
		                     }
		cookie={"sessionid":"vic6a5foqqyqxqdb4w7x86zruka4pm71"}
		##注意这里格式为字典
		r = requests.post(url=url, headers=headers,cookies=cookie)
		print(r.request.headers)
	def test_put_file(self):
		url="https://httpbin.testing-studio.com/post"
		r = requests.post(url=url, files={"hogwarts_file": open("hogwarts.txt", "rb")},proxies=self.proxies,verify=False)
		print(r.json())