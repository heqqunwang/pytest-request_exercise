import os

import yaml

from litemall.apis.user_center import UserCenter


##测试用户中心接口
class TestUserCenter():##注意类名要以Test开头，不需要集成baseapi类
	def setup_class(self):
		env_path = os.getenv("interface_env", default="litemall_env_cofig_release")
		base_url = yaml.safe_load(open(f"../../config/{env_path}.yaml", encoding="utf-8"))
		self.base_user_url = base_url["base_url"]
		self.usercenter= UserCenter(self.base_user_url, "user")
	def test_my_order(self):

		result=self.usercenter.my_order(0)

	def test_my_coupon(self):
		result = self.usercenter.my_coupon(0)

	def test_my_address(self):
		result = self.usercenter.my_address()


	def test_add_address(self):
		result = self.usercenter.add_address()