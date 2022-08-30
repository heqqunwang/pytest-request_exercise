import json
import requests

from utils.log_utils import logger


class Base:
	def __init__(self,base_url,tools):
		self.proxies = {
			'http': "http://127.0.0.1:8888",
			'https': "http://127.0.0.1:8888"}

		self.base_url=base_url
		self.tools=tools#环境切换初始化
		self.get_token()




	def get_token(self):
		params = {"corpid": "ww99eaf6cddda35ee6", "corpsecret": "jNN55_k4HpZcXxbr6RGrfKT9Cvs3ZUG-LlYa4t5HZ1w"}  ##requests特点
		token_url = "cgi-bin/gettoken"
		r = requests.get(url=self.base_url+token_url, params=params,proxies=self.proxies,verify=False)
		self.access_token = r.json()["access_token"]
		logger.debug(f"{self.base_url+token_url}请求响应为{json.dumps(r.json(),ensure_ascii=False,indent=2)}")
		return self.access_token



	def send(self,method,url,**kwargs):
		##1接口里直接使用了requests方法，进行封装
		##大量使用了域名，页进行封装替换，base_url,便于后许进行环境切换
		##token封装，也放到构造函数里

		if self.tools=="requests":##当前框架为request

			r=requests.request(method=method,url=self.base_url+url,**kwargs,proxies=self.proxies,verify=False)
			print(f"{self.base_url+url}请求响应为{json.dumps(r.json(),ensure_ascii=False,indent=2)}")
			logger.debug(f"{self.base_url+url}请求响应为{json.dumps(r.json(),ensure_ascii=False,indent=2)}")
			return r.json()
		else:
			pass
		##如果是其他框架，再测试用例里修改参数即可，其他逻辑都直接可用
