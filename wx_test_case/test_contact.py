import pytest

from wx_req_page.contact_page import ContactPage


class TestContact:
    def setup_class(self):


        self.contact=ContactPage
        self.contact.get_token(self,"ww99eaf6cddda35ee6","jNN55_k4HpZcXxbr6RGrfKT9Cvs3ZUG-LlYa4t5HZ1w")


    # @pytest.mark.parametrize("corpid,corpsecret,result",[("ww99eaf6cddda35ee6","jNN55_k4HpZcXxbr6RGrfKT9Cvs3ZUG-LlYa4t5HZ1w",0)])
    # def test_token(self,corpid,corpsecret,result):
    # ##获取token及测试断言
    #     r=self.contact.get_token(self,corpid,corpsecret)
    #     assert  r.get("errcode")==result

    def test_find_member(self):
        r=self.contact.find_member(self,self.access_token,"liuyi12")
        # assert r=="0"

    def test_add_member(self):##测试添加接口
        r=self.contact.add_member(self,self.access_token,"whq123","hqwang","alieen",17894561235)
        assert r == "0"

    def test_update_member(self):##测试更新接口
        r=self.contact.update_member(self,self.access_token,"FangFa","name222","13122244561")
        assert r == "0"

    def test_delete_member(self):##测试删除接口
        self.contact.delete_member(self,self.access_token,"FangFa")

