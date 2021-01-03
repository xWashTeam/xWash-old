# -*- coding: utf-8 -*-
import json
import requests

class UClean_Checker:
    url = r"https://u.zhinengxiyifang.cn/api/Devices"
    USING = "1"
    SPARE = "0"
    responseJson = ""
    location = ""
    para = ""

    #TODO 统一代码风格

    def init(self, mJson):
        # 装载一个洗衣机的信息
        self.location = mJson["location"]
        self.responseJson = ""
        self.para = r'?filter={"where":{"qrCode":"' + mJson["qrLink"] + '","isRemoved":false},"scope":{"fields":["virtualId","scanSelfClean","hasAutoLaunchDevice","autoLaunchDeviceOutOfStock","isSlotMachine","deviceTypeId","online","status","boxTypeId","sn"]},"include":[{"relation":"store","scope":{"fields":["isRemoved","enable"]}}]}'

    def loadResponseStatus(self):
        # 读取洗衣机状态
        res = self.getSession()
        text = res.text[1:-1] # 去除response中前后的[ ]
        try:
            self.responseJson = json.loads(text)
        except Exception:
            # TODO 异常处理
            print(Exception)
            return False

    def getSession(self):
        """
        查询洗衣机状态
        :return : 响应对象
        """
        s = requests.session()
        res = s.get(url=self.url + self.para)
        return res

    def check(self,mJson=None):
        if mJson != None:
            self.init(mJson)
        self.loadResponseStatus()
        status = self.responseJson["status"]
        remainTime = self.responseJson["remainTime"]
        if status == self.SPARE:
            return {"status":"available","location":self.location,"message":"洗衣机无人使用","remainTime": 0,"belong":"U净"}
        elif status == self.USING :
            return {"status" : "using","location":self.location,"message":"洗衣机被占用","remainTime": remainTime,"belong":"U净"}
        else:
            return {"status": "unknown","remainTime":-2,"message":"未知情况发生.","sessionText": self.getSession().text}

if __name__ == '__main__':
    u = UClean_Checker()
    total = None
    with open("../conf/D19.json", encoding="utf8") as f:
        total = json.load(f)
    for i in total:
        if(total[i]["belong"] == "U-clean"):
            # print(total[i])
            u.init(total[i])
            print(u.check())
