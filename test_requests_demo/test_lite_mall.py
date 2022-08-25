import pytest
import requests
import yaml


class Test_litemall:
	def setup_class(self):
		# ##代理
		self.proxies = {
			'http': "http://127.0.0.1:8888",
			'https': "http://127.0.0.1:8888"
		}
		##登录接口获取token
		admin_url="https://litemall.hogwarts.ceshiren.com/admin/auth/login"
		admin_data={
					"username": "admin123",
					"password": "admin123",
					"code": ""
					}
		r=requests.post(url=admin_url,json=admin_data,proxies=self.proxies,verify=False)
		self.admin_token=r.json()["data"]["token"]

		# self.admin_token=r.jsonpath(r.json,'$..token')
		#响应结果里获取token，便于后续传参
		# user_url=""
		# user_header = ""
		# j=requests.post(url=user_url,headers=user_header)
		# self.user_token=j.json()[1]
	@pytest.mark.parametrize("goodsid,goodsname",yaml.safe_load(open("goods.yaml",encoding="UTF-8")))
	def test_upload_goods(self,goodsid,goodsname):
		##商品上架
		url="https://litemall.hogwarts.ceshiren.com/admin/goods/create"
		create_data={
			"goods": {
				"picUrl": "",
				"gallery": [],
				"isHot":False,
				"isNew":True,
				"isOnSale":True,
				"goodsSn": f"{goodsid}",
				"name": f"{goodsname}",
				"counterPrice": "15"
			},
			"specifications": [{
				"specification": "规格",
				"value": "标准",
				"picUrl": ""
			}],
			"products": [{
				"id": 0,
				"specifications": ["标准"],
				"price": 0,
				"number": 0,
				"url": ""
			}],
			"attributes": []
		}

		r=requests.post(url=url,headers={"X-Litemall-Admin-Token":self.admin_token},json=create_data,proxies=self.proxies,verify=False)
		##注意这里headers是字典，要用冒号
		assert r.json()["errmsg"]=='成功'
	def test_query_goods_list(self):
		##查询商品列表
		query_url = "https://litemall.hogwarts.ceshiren.com/admin/goods/list?page=1&limit=20&sort=add_time&order=desc"

		r = requests.get(url=query_url, headers={"X-Litemall-Admin-Token": self.admin_token},
		                  proxies=self.proxies, verify=False)
		##注意这里headers是字典，要用冒号
		assert r.json()["errmsg"] == '成功'

	@pytest.mark.parametrize("goodsid,goodsname", yaml.safe_load(open("goods.yaml", encoding="UTF-8")))
	def delete_goods(self,goodsid,goodsname):
		delete_url = "https://litemall.hogwarts.ceshiren.com/admin/goods/delete"
		delete_data={
			"id": 1181493,
			"goodsSn": f"{goodsid}",
			"name": f"{goodsname}",
			"categoryId": 0,
			"brandId": 0,
			"gallery": [],
			"keywords": "",
			"brief": "",
			"isOnSale": True,
			"sortOrder": 100,
			"picUrl": "",
			"isNew": True,
			"isHot": False,
			"unit": "’件‘",
			"counterPrice": 15,
			"retailPrice": 0,
			"addTime": "2022-08-19 03:18:28",
			"updateTime": "2022-08-19 03:18:28",
			"deleted": False,
			"preview": [""]
		}

		r = requests.get(url=delete_url, headers={"X-Litemall-Admin-Token": self.admin_token},json=delete_data,
		                  proxies=self.proxies, verify=False)
		##注意这里headers是字典，要用冒号
		assert r.json()["errmsg"] == '成功'




