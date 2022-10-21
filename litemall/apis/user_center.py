from litemall.apis.base import BaseApi


class UserCenter(BaseApi):##我的--用户中心页面相关接口
	def my_order(self,status):
		##查看全部订单,showType=0表示全部订单，1代付款，2待发货3，待收货4待评价
		my_order_list_url="/wx/order/list"
		data={"showType":status}
		self.send(method="get",params=data,url=my_order_list_url)

	def my_coupon(self,status):
		##查看优惠券,status=0表示未使用，1已使用，2已过期
		my_coupon_list_url="/wx/coupon/mylist"
		data={"showType":status}
		self.send(method="get",params=data,url=my_coupon_list_url)

	def my_address(self):
		##查看优惠券,status=0表示未使用，1已使用，2已过期
		my_address_list_url="/wx/address/list"
		self.send(method="get",url=my_address_list_url)
	def add_address(self):
		##新增地址，目前是写死
		add_address_url="/wx/address/save"
		data={"name":"hq","tel":"15712345679","country":"",
		      "province":"湖北省","city":"武汉市","county":"江岸区",
		      "areaCode":"420102","postalCode":"","addressDetail":"解放大道01号","isDefault":False}
		self.send(method="post",url=add_address_url,json=data)
