import json
import  unittest
import os
from xlutils.copy import copy
import requests
import sys
import xlrd
import xlwt
from xlrd import open_workbook
import openpyxl

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

class ZhuishuSign(unittest.TestCase):
    path = curPath + "\\cases.xls"
    xlx_data = xlrd.open_workbook(path)
    # 取第x个表格
    sheet = xlx_data.sheet_by_index(0)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sign(self):
        total = 17
        for index in range(total):
            print(index)
            self.sign(index)

    def sign(self,index):
        u"每日签到"
        url = "http://api.zhuishushenqi.com/user/signIn"
        try:
            self.login_result = self.login(index)
            self.judge_result = self.judgeSign(index)
            params = {
                "token": self.login_result["token"],
                "version": 2,
                "activityId": self.judge_result["activityId"],
                "type": 2
            }
        except:
            params = {
                "token": self.sheet.cell_value(index,7),
                "version": 2,
                "activityId": self.sheet.cell_value(index,8),
                "type": 2
            }
        else:
            token = self.login_result["token"]
            activity_id = self.judge_result["activityId"]
            #wbk = xlwt.Workbook()
            #sheet1  = wbk.add_sheet("111")
            #sheet1.write(index,7,token)
            #sheet1.write(index,8,activity_id)
            #wbk.save(curPath+"\\cases.xlsx")
            open_book = open_workbook(curPath+"\\cases.xls")
            r_sheet =open_book.sheet_by_index(0)
            copy_book = copy(open_book)
            w_sheet = copy_book.get_sheet(0)
            w_sheet.write(index,7,token)
            w_sheet.write(index, 8, activity_id)
            copy_book.save(curPath+"\\cases.xls")
        response = requests.get(url, params)

    def judgeSign(self,index):
        url = "http://api.zhuishushenqi.com/user/v2/judgeSignIn"
        login_result = self.login(index)
        params = {
            "token" :login_result["token"]
        }
        response = requests.get(url,params)
        result = json.loads(response.content)
        return result

    def login(self,index):
        url = "http://api.zhuishushenqi.com/user/login"
        params = {
            "channelName" :self.sheet.cell_value(index,1),
            "platform_uid" :self.sheet.cell_value(index,2),
            "promoterId" :self.sheet.cell_value(index,3),
            "platform_token":self.sheet.cell_value(index,4),
            "version" :self.sheet.cell_value(index,5),
            "platform_code":self.sheet.cell_value(index,6),
            "packageName":"com.ushaqi.zhuishushenqi"

        }
        response = requests.post(url,params,verify=False)
        result = json.loads(response.content)
        return  result

if __name__ == '__main__':
    test = ZhuishuSign()
    test.test_sign()