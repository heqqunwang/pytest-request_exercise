from litemall.apis.base import BaseApi


class Carts(BaseApi):
	def query_goods_detail(self,goods_id):
		##用户端查看商品详情获得product_id
		query_url="/wx/goods/detail"
		goods_data={
			"id": goods_id
		}
		r = self.send(url=query_url,params=goods_data,method="get")
		self.product_id = r["data"]["productList"][0]["id"]
		return self.product_id

	def add_cart(self,goods_id,product_id):
		add_url="/wx/cart/add"
		##商品添加到购物车
		data = {
			"goodsId":goods_id,##调用不同类得方法得返回结果？？？
			"number": 1,
			"productId": product_id
		}
		r=self.send(url=add_url, method="post",json=data)
