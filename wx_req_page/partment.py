import requests

from wx_req_page.base import Base


class Partment(Base):
	# def __init__(self):
	# 	##构造函数
	# 	self.get_token()

	def add_partment(self,name,parentid):
		##创建部门
		add_partment_url="delete_partment_url"
		add_paramns = {"access_token": self.access_token}
		add_partment_data={"name":name,"parentid":parentid,}
		r=requests.post(url=add_partment_url,json=add_paramns)
		return r.json()


	def get_deprtment_list(self):
		##获取部门列表
		get_deprtment_list_url="https://qyapi.weixin.qq.com/cgi-bin/department/simplelist"
		get_params = {"access_token": self.access_token}
		partment_list=requests.get(url=get_deprtment_list_url,params=get_params)
		print(partment_list.json())
		return partment_list.json()["department_id"]
	##返回部门列表的第一个部门id

	def edit_partment(self,id,name):
		##编辑部门
		edit_partment_url="https://qyapi.weixin.qq.com/cgi-bin/department/update"
		edit_params={"access_token":self.access_token}
		update_data={"id":id,"name":name}
		requests.post(url=edit_partment_url,json=update_data,params=edit_params)




	def delete_partment_url(self,id):
		##删除部门
		delete_partment_url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
		delete_params={"access_token":self.access_token,"id":id}
		requests.post(url=delete_partment_url,params=delete_params)



