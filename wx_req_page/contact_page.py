import requests

from wx_req_page.base import Base


class ContactPage(Base):
   def find_member(self,userid:str):
      ##查找成员
      get_member_url = "cgi-bin/user/get"
      get_member_data={"access_token":self.access_token,"userid":userid}
      r=self.send(method="get",url=get_member_url,params=get_member_data)
      return r["errcode"]


   def add_member(self,userid,name,alias,mobile,**kwargs):
      ##新增成员
      add_member_url = "cgi-bin/user/create"
      p={"access_token":self.access_token}
      data = {

         "userid": userid,
         "name": name,
         "alias": alias,
         "mobile": mobile,
      }
      data.update(kwargs)
      r = self.send(method="post",url=add_member_url, json=data,params=p)
      # try:
      #    assert 0 == r['errcode']
      # except Exception:
      #    print("删除失败")



   def delete_member(self,userid):
      ##删除成员
      params={"access_token":self.access_token,"userid":userid}
      delete_member_url = "cgi-bin/user/delete"
      r = self.send(method="get",url=delete_member_url,params=params)
      try:
         assert 0 == r['errcode']
      except Exception:
         print("删除失败")

   def update_member(self,userid,name,mobile,**kwargs):
      ##编辑更新成员
      update_member_url = "cgi-bin/user/update"
      p = {"access_token": self.access_token}
      data = {
         "userid": userid,
         "name": name,
         "mobile": mobile

      }
      r = self.send(method="post",url=update_member_url, json=data,params=p)

      return r["errcode"]

