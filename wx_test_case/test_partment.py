import pytest

from wx_req_page.partment import Partment


class TestPaerment:
	def setup_class(self):
		self.partment=Partment()
		self.partment.get_token("ww99eaf6cddda35ee6",
		                         "jNN55_k4HpZcXxbr6RGrfKT9Cvs3ZUG-LlYa4t5HZ1w")

	#@pytest.mark.parametrize("name,parentid",["hq_1",11])
	def test_add_partment(self,name,parentid):
		result=self.partment.add_partment(name=name,parentid=parentid)
		depart_list=self.partment.get_deprtment_list()

		assert result==0 and result[id] in depart_list
##断言创建成功的接口为0，且他的id在部门列表的id里

	def test_get_partment_list(self):
		self.partment.get_deprtment_list()

	def test_edit_partment(self):
		pass

	def test_delete_partment(self):
		pass