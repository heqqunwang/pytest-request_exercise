import os
import time

import pytest
import yaml

from litemall.apis.carts import Carts
from litemall.apis.admin_goods import Goods
from litemall.apis.user_center import UserCenter


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
		self.usercenter=UserCenter(self.base_user_url,"user")




	@pytest.mark.run(order=1)
	@pytest.mark.parametrize("name,goodssn",[("quto_5","10028")])
	def test_add_goods(self,name,goodssn):  ##在管理后台添加商品
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

		result_addgoods=self.goods.add_goods(data)  ##管理后台添加商品
		assert result_addgoods==0
		time.sleep(5)##等待5s，免得删除接口很快，断言失败
		r=self.goods.query_goods(name)  ##管理后台查询商品

		result_deletegood=self.goods.delete_goods(r[0])
		assert result_deletegood==0


	@pytest.mark.run(order=2)
	def test_query_goods(self):
		##测试管理后台商品查询
		res=self.goods.query_goods()
		assert res[1]=="成功"


	##管理后台：通过商品id删除商品--删除查询到的第一个商品
	def test_delete_goods(self):
		delete_goods_id = self.goods.query_goods()
		print(delete_goods_id)
		if delete_goods_id!="商品不存在":
			res=self.goods.delete_goods(delete_goods_id[0])
			assert res ==0

##添加商品到购物车，修改数量，从购物车里删除
	def test_add_cart(self):
		goods_id=self.goods.query_goods()##1、在管理后台查询商品列表获得第一个商品得goodsid
		if goods_id!="商品不存在":
			product_id=self.cart.query_goods_detail(goods_id[0])##2、在用户端通过goodsid获得产品id
			self.cart.add_cart(goods_id[0],product_id)  ##3、在用户端：通过productid加入到购物车
			##从购物车里删除
			self.cart.delete_cart_good(product_id)

##下单流程，未支付的
##暂时写死
	def test_buy_product(self):
		goods_id = self.goods.query_goods()
		if goods_id != "商品不存在":
			product_id = self.cart.query_goods_detail(goods_id[0])
			self.cart.add_cart(goods_id[0], product_id)
			address_id=self.usercenter.my_address()
			self.cart.checkout_order(addressid=address_id)
			order_id=self.cart.submit_order(addressid=address_id)
			self.cart.order_detail(order_id)



