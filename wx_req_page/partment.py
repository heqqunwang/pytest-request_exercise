import json

import requests

from wx_req_page.base import Base
import jsonpath

class Partment(Base):


	def add_partment(self,name,parentid):
		##创建部门
		add_partment_url="cgi-bin/department/create"
		add_paramns = {"access_token": self.access_token}
		add_partment_data={"name":name,"parentid":parentid,}
		r=self.send(method="post",url=add_partment_url,json=add_partment_data,params=add_paramns)
		return r


	def get_deprtment_list(self,id):
		##获取部门列表
		get_deprtment_list_url="cgi-bin/department/simplelist"
		get_data={"access_token":self.access_token,"id":id}
		get_partment_result=self.send(method="get",url=get_deprtment_list_url,params=get_data)
		print(f"{self.base_url + get_deprtment_list_url}请求响应为{json.dumps(get_partment_result, ensure_ascii=False, indent=2)}")

		# partment_list=jsonpath($.department_id.id[*])
		##列表推导式获取部门列表
		return get_partment_result
	##返回s所有id

	def edit_partment(self,id,name):
		##编辑部门
		edit_partment_url="cgi-bin/department/update"
		edit_params={"access_token":self.access_token}
		update_data={"id":id,"name":name}
		edit_result=self.send(method="post",url=edit_partment_url,json=update_data,params=edit_params)
		return edit_result["errcode"]




	def delete_partment_url(self,id):
		##删除部门
		delete_partment_url = "cgi-bin/department/delete"
		delete_params={"access_token":self.access_token,"id":id}
		delete_result=self.send(method="post",url=delete_partment_url,params=delete_params)



