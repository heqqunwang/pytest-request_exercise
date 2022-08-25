##测试响应加密解密
#  1.cd到加密文件路径
# 2.输入命令python  -m http.server 9999
# 3.浏览器输入http://127.0.0.1:9999/
# 4.点击加密文件
# 5.请求体即为http://127.0.0.1:9999/demo.txt
import requests
import base64
import json


def test_secret_1():
	url="http://127.0.0.1:9999/demo.txt"
	r=requests.get(url)
	result=json.loads(base64.b64decode(r.content))


	print(f"r是{r.content}")
	print(f"result是{result}")
def test_secret_3():
	res=requests.post("第三方服务的url",data="本地响应加密的请求")
	print(res.content)


