# -*- coding: utf-8 -*-
import json
import time

import requests

class Soda_Checker():

    qrLink = ""
    location = ""

    USING = "USING"
    AVAILABLE = "AVAILABLE"

    def init(self,mJson):
        self.qrLink = mJson["qrLink"]
        self.location = mJson["location"]

    def check(self,mJson = None):
        if mJson != None:
            self.init(mJson)
        status = self.getStatus()
        if status == self.AVAILABLE:
            return {"status":"available","location":self.location,"message":"洗衣机无人使用","remainTime":-1,"belong":"soda"}
        elif status == self.USING:
            return {"status":"using","location":self.location,"message":"洗衣机被占用","remainTime":-1,"belong":"soda"}
        else:
            return {"status": "unknown","remainTime":-2,"message": self.getSession().text}

    def getStatus(self):
        response = self.getSession()
        responseJson = json.loads(response.text)
        return responseJson["data"]["status"]

    def getSession(self):
        """
        获取响应
        :return: 返回洗衣机状态的响应 {status,location,message,remainTime,belong}
        """
        s = requests.session()
        #+ "__t=" + str(int(time.time()*1000))
        return s.get(self.qrLink)

if __name__ == '__main__':
    S = Soda_Checker()
    total = None
    with open("../conf/D19.json", encoding="utf8") as f:
        total = json.load(f)
    for i in total:
        if (total[i]["belong"] == "sodalife"):
            S.init(total[i])
            print(S.check())
