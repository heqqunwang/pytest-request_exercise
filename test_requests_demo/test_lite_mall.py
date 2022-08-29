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
	##用户端登录，获取用户端登录token
		user_url="https://litemall.hogwarts.ceshiren.com/wx/auth/login"
		user_data={
			"username": "user123",
			"password": "user123"
			}

		j=requests.post(url=user_url,json=user_data, proxies=self.proxies, verify=False)
		self.user_token=j.json()["data"]["token"]



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
				"price": 1.5,
				"number":100,
				"url": ""
			}],
			"attributes": []
		}

		add_good_r=requests.post(url=url,headers={"X-Litemall-Admin-Token":self.admin_token},json=create_data,proxies=self.proxies,verify=False)
		##注意这里headers是字典，要用冒号


		##查询后台商品
		query_url = "https://litemall.hogwarts.ceshiren.com/admin/goods/list"
		goods_data={"name":{goodsname},"order":"desc","sort":"add_time"}
		r = requests.get(url=query_url, params=goods_data,headers={"X-Litemall-Admin-Token": self.admin_token},
		                  proxies=self.proxies, verify=False)
		##注意这里headers是字典，要用冒号
		##返回第一个商品的商品id
		# return r.json()["data"]["list"]["id"][0]
		print("获取到goods_id是：")
		print(r.json()["data"]["list"][0]["id"])##后面商品商详，删除，编辑都需要用到商品goods_id
		self.goods_id=r.json()["data"]["list"][0]["id"]


		##查看用户端商品详情，获得商品product_id
		user_goods_detail = f"https://litemall.hogwarts.ceshiren.com/wx/goods/detail?id={self.goods_id}"
		# user_goods_detail = f"https://litemall.hogwarts.ceshiren.com/wx/goods/detail?id=1181827"
		r = requests.get(url=user_goods_detail, headers={"X-Litemall-Token": self.user_token},
		                 proxies=self.proxies, verify=False)
		self.product_id = r.json()["data"]["productList"][0]["id"]
		print(self.product_id)

		##用户端加入购物车

		add_cart_url = "https://litemall.hogwarts.ceshiren.com/wx/cart/add"
		data = {
			"goodsId": self.goods_id,
			"number": 1,
			"productId": self.product_id
		}
		requests.post(url=add_cart_url, json=data, headers={"X-Litemall-Token": self.user_token},
		              proxies=self.proxies, verify=False)

		#===============删除商品
		delete_url = "https://litemall.hogwarts.ceshiren.com/admin/goods/delete"
		delete_data={
			"id": self.goods_id
		}

		r = requests.post(url=delete_url, headers={"X-Litemall-Admin-Token": self.admin_token},json=delete_data,
		                  proxies=self.proxies, verify=False)
		# ##注意这里headers是字典，要用冒号

#======	##用户页地址为https://litemall.hogwarts.ceshiren.com/vue/index.html#/










