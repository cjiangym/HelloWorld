import unittest
import urllib
import urllib.request
import requests
import json


class Test_OpenApp(unittest.TestCase):
    def setUp(self):
        self.headers={
            "User - Agent": "Mozilla / 5.0(WindowsNT10.0;WOW64;rv: 44.0) Gecko/20100101 Firefox/44.0"
        }
    def test_getSessionId(self):
        u"测试google"
        self.url='http://sv.ismartgo.cn:29090/appsv2/app/getAppSessionId.do?appversion=401000&client=ios&devcode=e895ec8c-6c18-4a27-a509-328cd252b6fa&lat=23.152676&lon=113.368790&os=iOS&reqtime=2017-10-14%2021%3A49%3A14&uid=832776&userkey=123'
        print(self.url)
        r = requests.get(self.url)
        result = json.loads(r.content)
        print(u"restult=",result)
        data = result["data"]
        print(u"data=",data)
        appgamesvurl=data["appgamesvurl"]
        print(u"appgamesvurl=",appgamesvurl)
        statu=result["status"]
        print(u"status=",statu)
        self.assertEqual(statu,10001)


