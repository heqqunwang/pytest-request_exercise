
from litemall.apis.base import BaseApi

##用户端首页接口方法
class UserIndex(BaseApi):
	##待完成
	def index_query(self):
		##首页index接口
		index_url="/wx/home/index"
		r=self.send(method="get",url=index_url)
		return r["errmsg"]

	def brand(self):
		##品牌商列表
		brand_url="/wx/brand/list"
		r=self.send(method="get", url=brand_url)
		print(type(r))##是一个字典格式，不是json格式
		res=[r["errmsg"],r["data"]["list"][0]["id"]]##这里是提取第一个品牌商的id
		##怎么提取出所有的品牌商的id？

		return res
	def brand_detail(self,id):
		##查看品牌商详情接口
		brand_detail_url="/wx/brand/detail"
		detail_data={"id":f"{id}"}
		r=self.send(method="get", url=brand_detail_url,params=detail_data)
		return r["errmsg"]

	def brand_goods_list(self,id):
		brand_goods_url="/wx/goods/list"
		detail_data = {"brandId": f"{id}"}
		r=self.send(method="get", url=brand_goods_url, params=detail_data)
		return r["errmsg"]

	def groupon(self):
		##团购列表
		groupon_url="/wx/groupon/list"
		r=self.send(method="get", url=groupon_url)
		return r["errmsg"]
	def publish_new(self):
		##新品首发
		publish_new_url="/wx/goods/list?isNew=true"
		r = self.send(method="get", url=publish_new_url)
		return r["errmsg"]

	def recommend(self):
		##人气推荐
		recommend_url="/wx/goods/list?isHot=true"
		r = self.send(method="get", url=recommend_url)
		return r["errmsg"]

	def topics(self):
		##专题精选
		topics_url="/wx/topic/list"
		r = self.send(method="get", url=topics_url)
		return r["errmsg"]



