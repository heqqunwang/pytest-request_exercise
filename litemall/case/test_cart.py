import os
import time

import pytest
import yaml

from litemall.apis.carts import Carts
from litemall.apis.admin_goods import Goods
class TestCarts:
##测试管理后台添加一个商品，用户端添加到购物车

	def setup_class(self):
		env_path = os.getenv("interface_env", default="litemall_env_cofig_release")
		base_url=yaml.safe_load(open(f"../../config/{env_path}.yaml",encoding="utf-8"))
		self.base_admin_url=base_url["base_url"]
		self.base_user_url=base_url["base_url"]

		##测试用例示例化，可以在测试用例里调用api的接口
		self.goods=Goods(self.base_admin_url,"admin")
		self.cart=Carts(self.base_user_url,"user")


##在管理后台添加商品
	@pytest.mark.parametrize("name,goodssn",[("quto_5","10028")])
	def test_add_carts(self,name,goodssn):
		data = {
			"goods": {
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

		result_addgoods=self.goods.add_goods(data)
		assert result_addgoods==0
		time.sleep(5)##等待5s，免得删除接口很快，断言失败
		r=self.goods.query_goods(name)

		result_deletegood=self.goods.delete_goods(r[0])
		assert result_deletegood==0

##这里目前是写死得，待优化为新增得商品名称
	def test_query_goods(self):
		##测试管理后台商品查询
		#query_url="goods/list"
		#query_data={"name":"丽姿2","order":"desc","sort":"add_time"}
		res=self.goods.query_goods("HJJ20")
		assert res[1]=="成功"

##目前是写死得
##管理后台：通过商品id删除商品
	def test_delete_goods(self):
		res=self.goods.delete_goods(1181923)
		assert res ==0

##添加商品到购物车
	@pytest.mark.parametrize("name",[("quto_3")])
	def test_add_cart(self,name):
		goods_id=self.goods.query_goods(name)##1、在管理后台通过name获取到商品得goodsid

		product_id=self.cart.query_goods_detail(goods_id)##2、在用户端通过goodsid获得产品id
		self.cart.add_cart(goods_id[0],product_id)  ##3、在用户端：通过productid加入到购物车

##下单流程，
##暂时写死
	def test_buy_product(self):
		self.cart.cart_chunked([2587])##调用购物车的结算
		self.cart.checkout_order()
		#self.cart.submit_order()
		self.cart.order_detail()



