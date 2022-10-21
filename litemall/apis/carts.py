from litemall.apis.base import BaseApi

##用户端购物车方法
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

	def cart_list(self):
		##购物车列表
		cart_list="/wx/cart/index"
		r = self.send(url=cart_list, method="get")

	def cart_chunked(self,list_productid):
		##将商品点击去结算
		cart_list_url = "/wx/cart/checked"
		data = {
			"productIds": list_productid,
			"isChecked": 1
		}
		r = self.send(url=cart_list_url, method="post", json=data)
	def checkout_order(self,cartid=0,addressid=0,couponid=0,userCouponId=0,grouponRulesId=0):##参数默认为0
		##从结算点击提交订单
		checkout_order_url="/wx/cart/checkout"
		data={"cartID":{cartid},"addressId":addressid,"couponId":couponid,"userCouponId":userCouponId,"grouponRulesId":grouponRulesId}
		self.send(method="get",url=checkout_order_url,params=data)

	def submit_order(self):
		##确认提交订单,目前参数写死
		submit_order_url="/wx/order/submit"
		data={
		"addressId": "7",
		"cartId": "0",
		"couponId": "0",
		"userCouponId": "0",
		"grouponLinkId": 0,
		"grouponRulesId": 0,
		"message": ""
	}
		r=self.send(method="post",url=submit_order_url,json=data)

		return r["data"]["orderId"]

	def order_detail(self):
		##订单详情
		order_detail_url="/wx/order/detail"
		id=self.submit_order()##orderid为submit的结果,则先调用submit方法
		data={"orderId":{id}}
		self.send(method="get",params=data,url=order_detail_url)


