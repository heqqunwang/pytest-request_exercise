import pytest

from wx_req_page.partment import Partment


class TestPaerment:
	def setup_class(self):
		self.partment=Partment(base_url="https://qyapi.weixin.qq.com/",tools="request")



	@pytest.mark.parametrize("name,parentid",[("hq_1",1)])
	def test_add_partment(self,name,parentid):
		result=self.partment.add_partment(name=name,parentid=parentid)
		department_list=self.partment.get_deprtment_list(1)##获取部门列表

		# assert result["errcode"]==0 and result[id] in department_list
##断言创建成功的接口为0，且返回结果的id在部门列表的id里

	def test_get_partment_list(self):
		self.partment.get_deprtment_list(1)


	def test_edit_partment(self):
		pass


	def test_delete_partment(self):
		pass