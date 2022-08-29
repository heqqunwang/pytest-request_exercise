import pytest

from litemall.apis.carts import Carts
from litemall.apis.goods import Goods
class TestCarts:


	def setup_class(self):
		self.base_admin_url="https://litemall.hogwarts.ceshiren.com"
		self.base_user_url="https://litemall.hogwarts.ceshiren.com"
		self.goods=Goods(self.base_admin_url,"admin")##测试用例示例化，可以在测试用例里调用api的接口
		self.cart=Carts(self.base_user_url,"user")

	@pytest.mark.parametrize("name,goodssn",[("quto_3","10026")])
	def test_add_carts(self,name,goodssn):
		upload_data = {"goods": {
				"picUrl": "",
				"gallery": [],
				"isHot":False,
				"isNew":True,
				"isOnSale":True,
				"goodsSn": goodssn,
				"name": name,
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
				"price": 1,
				"number": 1000,
				"url": ""
			}],
			"attributes": []}
		self.goods.upload_goods(upload_data=upload_data)
		r=self.goods.query_goods(name)
		# self.goods.delete_goods(r[0])

	def test_query_goods(self):
		##测试管理后台商品查询
		query_url="goods/list"
		#query_data={"name":"丽姿2","order":"desc","sort":"add_time"}
		res=self.goods.query_goods("丽姿2")
		assert res[1]==0

##目前是写死得
	def test_delete_goods(self):
		self.goods.delete_goods(1181920)

	@pytest.mark.parametrize("name",[("quto_3")])
	def test_add_cart(self,name):
		goods_id=self.goods.query_goods(name)
		product_id=self.cart.query_goods_detail(goods_id)
		self.cart.add_cart(goods_id[0],product_id)



