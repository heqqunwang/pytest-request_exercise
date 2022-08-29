
from litemall.apis.base import BaseApi


class Goods(BaseApi):
	def upload_goods(self,upload_data):
		##管理后台增加商品列表
		upload_url = "goods/create"
		r = self.send(url=self.base_url+upload_url, json=upload_data,method="post")
		return r["errno"]



	def query_goods(self,goodsname):
		##查询管理后台商品，获取到商品id
		query_admin_url = "/admin/goods/list"
		goods_data = {"name": goodsname, "order": "desc", "sort": "add_time"}
		r=self.send(method="get",url=query_admin_url,params=goods_data)
		self.add_goods_id = r["data"]["list"][0]["id"]
		self.result=r["errno"]
		return [self.add_goods_id,self.result]##返回响应码与goodsid，封装为一个数组

	def delete_goods(self,goods_id):
		##删除管理后台商品
		delete_url = "/admin/goods/delete"
		goods_data={
			"id": goods_id
		}

		r = self.send(method="post",url=delete_url,json=goods_data)
		return r["errno"]



