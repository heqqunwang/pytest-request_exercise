import os

import requests
import yaml
##多环境切换
from test_requests_demo.conftest import global_env


class TestEnv:
	def setup_class(self):
		##优化方案：1从环境变量读取配置环境
		env_path=global_env.get("env")
		base_url = yaml.safe_load(open(f"{env_path}.yaml", encoding="utf-8"))

		# base_url=yaml.safe_load(open("test_env.yaml",encoding="utf-8"))##从yanl文件读取数据，仍然是硬编码方式

		self.base_url=base_url["base_url"]


	def test_testenv(self):
		path="get"
		r=requests.get(self.base_url+path)
		print(r.json())
		assert r.json()["headers"]["Host"] == "https://httbin.org/"

	def test_dev_env(self):
		path="get"
		r=requests.post(self.base_url+path)
		assert r.json()["headers"]["Host"] == "https://httbin.ceshiren.com/"
