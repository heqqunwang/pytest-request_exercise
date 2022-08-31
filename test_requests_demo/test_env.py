import os

import requests
import yaml
##多环境切换

class TestEnv:
	def setup_class(self):
		##优化方案：1从环境变量读取配置环境
		env_path=os.getenv("interface_env",default="test_env")##设置默认值，方便ide调试
		base_url = yaml.safe_load(open(f"{env_path}.yaml", encoding="utf-8"))
		self.base_url=base_url["base_url"]

	def test_testenv(self):
		path="get"
		r=requests.get(self.base_url+path)
		print(r)

	def test_dev_env(self):
		path="get"
		requests.get(self.base_url+path)
