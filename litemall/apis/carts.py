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

	def delete_cart_good(self,product_id):
		##删除购物车里的商品，这里的id组成一个数组,如果是多个怎么处理？？？
		delete_url="/wx/cart/delete"
		data={"productIds":[product_id]}
		r=self.send(url=delete_url,method="post",json=data)
		return r["errno"]

	def update_cart_good_number(self,product_id,goods_id,number,id):
		##这个id的值不知道是从哪里取的，暂时没有写该接口的测试用例
		##修改购物车里指定商品的数量
		update_url="/wx/cart/update"
		data={"productId":product_id,"goodsId":goods_id,"number":number,"id":id}
		r=self.send(url=update_url,method="post",json=data)
		return r["errno"]##0是修改成功，710是库存不足

	def cart_list(self):
		##购物车列表
		cart_list="/wx/cart/index"
		r = self.send(url=cart_list, method="get")
		return r["data"]["cartlist"][0]["id"]  ##返回购物车列表第一个商品的id

	##从购物车点击结算按钮发起的请求
	def checkout_order(self,addressid,cartid=0,couponid=0,userCouponId=0,grouponRulesId=0):
		##参数默认为0,不为0的参数放最前面
		checkout_order_url="/wx/cart/checkout"
		data={"cartID":{cartid},"addressId":addressid,"couponId":couponid,"userCouponId":userCouponId,"grouponRulesId":grouponRulesId}
		self.send(method="get",url=checkout_order_url,params=data)

	def submit_order(self,addressid,cartid=0,couponid=0,userCouponId=0,grouponRulesId=0,grouponLinkId=0,message=None):
		##确认提交订单,目前参数写死
		submit_order_url="/wx/order/submit"
		data={
		"addressId": addressid,
		"cartId": cartid,
		"couponId": couponid,
		"userCouponId": userCouponId,
		"grouponLinkId": grouponRulesId,
		"grouponRulesId": grouponRulesId,
		"message": message
	}
		r=self.send(method="post",url=submit_order_url,json=data)


		return r["data"]["orderId"]

	##点击提交订单按钮发起的请求
	##该请求为用了
	# def cart_chunked(self,list_productid):
	# 	##将商品点击去结算
	# 	cart_list_url = "/wx/cart/checked"
	# 	data = {
	# 		"productIds": list_productid,
	# 		"isChecked": 1
	# 	}
	# 	r = self.send(url=cart_list_url, method="post", json=data)


	def order_detail(self,id):
		##订单详情
		order_detail_url="/wx/order/detail"
		# id=self.submit_order()##orderid为submit的结果,则先调用submit方法
		data={"orderId":{id}}
		self.send(method="get",params=data,url=order_detail_url)


