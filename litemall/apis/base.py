import json

import requests

import utils
from utils.log_utils import logger
class BaseApi:
##base方法封装：域名地址封装、登录获取token、send方法封装

	def __init__(self,base_url,role=None):
		##构造函数，实例化得时候需要得参数
		# self.proxies = {
		# 	##代理，调试接口
		# 	'http': "http://127.0.0.1:8888",
		# 	'https': "http://127.0.0.1:8888"}
		self.base_url=base_url
		if role:
			self.role=role
			##获取对应端得角色信息

	def __set_token(self,request_info):
		##管理后台登录：token获取
		admin_url = "/admin/auth/login"
		admin_data = {
			"username": "hogwarts",
			"password": "test12345",
			"code": ""
		}
		# admin_r = requests.post(url=self.base_url+admin_url, json=admin_data,proxies=self.proxies,verify=False)
		admin_r = requests.post(url=self.base_url + admin_url, json=admin_data)
		self.admin_token = {"X-Litemall-Admin-Token":admin_r.json()["data"]["token"]}

		##用户端登录，获取用户端登录token
		user_url = "/wx/auth/login"
		user_data = {
			"username": "user123",
			"password": "user123"
		}
		user_r =requests.post(url=self.base_url+user_url,json=user_data)
		self.user_token ={"X-Litemall-Token":user_r.json()["data"]["token"]}


		if self.role=="admin":
			##判断是哪个端
			self.final_token=self.admin_token
		else:
			self.final_token=self.user_token

		if request_info.get("headers"):
			request_info["headers"].update(self.final_token)
		else:
			request_info["headers"]=self.final_token
		return request_info





	def send(self,method,url,**kwargs):
		##send方法封装，且携带上token
		##这里怎么现在不定长参数里塞入header信息，data数据？？重难点，录播视频有讲
		kwargs=self.__set_token(kwargs)##将token塞入到kwargs里
		send_result=requests.request(method,url=self.base_url+url,**kwargs)
		# logger.debug(f"{url}响应为{r.json()}")
		print(f"{self.base_url + url},请求体为{kwargs}")
		print(f"{self.base_url + url}请求响应为{json.dumps(send_result.json(), ensure_ascii=False, indent=2)}")##控制台打印请求与返回信息，便于查阅问题

		logger.debug(f"{self.base_url+url}响应为{send_result.json()}")##在send方法里封装log信息，就不用单独在每个接口里添加了
		return send_result.json()





