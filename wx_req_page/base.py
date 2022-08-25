import requests


class Base:
	def get_token(self, corpid, corpsecret):
		params = {"corpid": corpid, "corpsecret": corpsecret}  ##requests特点
		token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
		r = requests.get(token_url, params)
		print(r.json())
		self.access_token=r.json()["access_token"]
		return self.access_token