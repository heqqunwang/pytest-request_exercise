import os

import yaml


from litemall.apis.users_index import UserIndex


class TestUserIndex():##注意类名要以Test开头，不需要集成baseapi类
	def setup_class(self):
		env_path = os.getenv("interface_env", default="litemall_env_cofig_release")
		base_url = yaml.safe_load(open(f"../../config/{env_path}.yaml", encoding="utf-8"))
		self.base_user_url = base_url["base_url"]
		self.userindex = UserIndex(self.base_user_url, "user")
	def test_index_query(self):
		##测试首页index接口
		result=self.userindex.index_query()
		assert result=="成功"
	def test_brand_list(self):
		##测试品牌商列表接口
		result=self.userindex.brand()
		assert result[0] == "成功"

	def test_brand_detail(self):
		##测试某个品牌商详情接口
		brand_list_id=self.userindex.brand()
		id=brand_list_id[1]
		result=self.userindex.brand_detail(id)
		assert result == "成功"

	def test_brand_good_list(self):
		##测试某个品牌商的商品列表接口
		brand_list_id=self.userindex.brand()
		id=brand_list_id[1]
		result=self.userindex.brand_goods_list(id)
		assert result == "成功"
	def test_groupon(self):
		##测试团购列表接口
		result=self.userindex.groupon()
		assert result == "成功"

	def test_publish_new(self):
		result=self.userindex.publish_new()
		assert result == "成功"

	def test_recommend(self):
		result=self.userindex.recommend()
		assert result == "成功"

	def test_topics(self):
		result=self.userindex.topics()
		assert result == "成功"