import requests

from req_page.base import Base


class ContactPage(Base):
   def find_member(self,access_token,userid:str):
      ##查找成员
      get_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={access_token}&userod={userid}"
      r = requests.get(get_member_url)
      print(r.json())
      return r.json()["errcode"]


   def add_member(self,access_token,userid,name,alias,mobile,**kwargs):
      ##新增成员
      add_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={access_token}"
      data = {

         "userid": userid,
         "name": name,
         "alias": alias,
         "mobile": mobile,
      }
      data.update(kwargs)
      r = requests.post(url=add_member_url, json=data)
      print(r.json())
      return r.json()["errcode"]
      # try:
      #    assert r.json()['errcode'] =="0"
      # except Exception:
      #    print("添加失败")

   def delete_member(self,access_token,userid):
      ##删除成员
      params={"userid":userid}
      delete_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={access_token}&={userid}"
      #proxies={"https":"127.0.0.1:8888"},通过代理监听请求发出去的情况
      r = requests.get(delete_member_url,params)
      #r = requests.get(delete_member_url,proxies=proxies,verify=False)
      try:
         assert 0 == r.json()['errcode']
      except Exception:
         print("删除失败")

   def update_member(self,access_token,userid,name,mobile,**kwargs):
      ##编辑更新成员
      update_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={access_token}"
      data = {
         "userid": userid,
         "name": name,
         "mobile": mobile

      }
      r = requests.post(url=update_member_url, json=data)
      print(r.json())

      return r.json()["errcode"]

