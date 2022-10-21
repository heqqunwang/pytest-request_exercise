
from litemall.apis.base import BaseApi
##管理后台的商品管理方法类
class Goods(BaseApi):

	def add_goods(self,upload_data):
		##管理后台增加商品列表
		upload_url = "/admin/goods/create"
		r = self.send(method="post",url=upload_url,json=upload_data)
		return r["errno"]



	def query_goods(self,goodsname):
		##查询管理后台商品，获取到商品id
		query_admin_url = "/admin/goods/list"
		goods_data = {"name": goodsname, "order": "desc", "sort": "add_time"}
		r=self.send(method="get",url=query_admin_url,params=goods_data)
		##self.goods_id = r["data"]["list"][0]["id"]##获取商品得id，如果商品不存在这里会报错
		self.exist = r["data"]["total"]
		if self.exist >= 1:
			self.goods_id = r["data"]["list"][0]["id"]
			self.result = r["errmsg"]
			return [self.goods_id, self.result]  ##返回响应码与goodsid，封装为一个数组
		else:
			return ["商品名不存在", "商品不存在，接口查询成功"]
		#self.result=r["errmsg"]
		#return [self.goods_id,self.result]##返回响应码与goodsid，封装为一个数组

	def delete_goods(self,goods_id):
		##删除管理后台商品
		delete_url = "/admin/goods/delete"
		goods_data={
			"id": goods_id
		}

		r = self.send(method="post",url=delete_url,json=goods_data)
		return r["errno"]



