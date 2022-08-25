import pytest
import requests
import yaml


def get_token():
    r=requests.get(
        "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww99eaf6cddda35ee6&corpsecret=jNN55_k4HpZcXxbr6RGrfKT9Cvs3ZUG-LlYa4t5HZ1w")

    print(r)
    print(r.json())
    assert 0 == r.json()['errcode']
    token=r.json()['access_token']
    return token
    ##参数传递
# 获取成员
def test_member():
    get_member_url=f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_token()}&userid=WangHeQun"
    r=requests.get(get_member_url)
    print(r.json())
# 更新成员信息
def test_update_member():

    update_member_url=f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={get_token()}"
    data={
        "userid": "zhangyi",
        "name": "李时珍",
        "department": [1],
        "order": [10],
        "position": "后台工程师",
        "mobile": "13800000000",
        "gender": "1",
        "email": "zhangsan@gzdev.com",

    }
    r=requests.post(url=update_member_url,json=data)
# 成员添加
def test_add_member():
    add_member_url=f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token()}"
    data={

            "userid": "wahaha",
            "name": "娃哈哈",
            "alias": "ad",
            "mobile": "+86 13812345678",
            "department": [1, 2],
            "order": [10, 40],
            "position": "产品经理",
            "gender": "1",
            "email": "wahaha@gzdev.com",

        }
    r=requests.post(url=add_member_url,json=data)
    try:
        assert r.json()['errcode']==400
    except Exception:
        print("添加失败")
# 考虑以yml的形式实现增加，待完成

# 删除信息
def test_delete_member():
    delete_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token()}&userid=zhangyi"

    r=requests.get(delete_member_url)
    try:
        assert 0==r.json()['errcode']
    except Exception:
        print("删除失败")


