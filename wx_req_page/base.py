import json
import logging

import requests


class Base:
	def __init__(self,base_url):
		#环境切换
		self.base_url=base_url



	def get_token(self, **request_infos):
		params = {"corpid": corpid, "corpsecret": corpsecret}  ##requests特点
		token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
		r = requests.get(token_url, params)
		print(r.json())
		self.access_token=r.json()["access_token"]
		return self.access_token

	def send(self,method,url,tools,**kwargs):
		##1接口里直接使用了requests方法，进行封装
		##大量使用了域名，页进行封装替换，base_url,便于后许进行环境切换
		##token封装，也放到构造函数里
		data={
			"method":method,
			"url":url,
			"tools":tools##测试框架工具

		}
		if tools=="requests":##当前框架为request
			kwargs=self.get_token(kwargs)
			r=requests.request(method,url,**kwargs)
			logging.Logger.info(f"{url}请求响应为{json.dumps(r.json(),ensure_ascii=False,indent=2) }")
		else:
			pass
		##如果是其他框架，再测试用例里修改参数即可，其他逻辑都直接可用
