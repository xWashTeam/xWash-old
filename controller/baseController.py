# -*- coding: utf-8 -*-
import json
from xWash.Checker.Soda_Checker import *
from xWash.Checker.UClean_Checker import *
import pymysql
import os

class baseController:
    db = None
    name = 'D19'
    # TODO 将name以 building的格式更新为 school/building的格式


    def __init__(self,db,name):
        self.db = db

    def select(self):
        '''
        数据库查询
        :return: tuple(location,remainTime,status,belong,message)组合
        '''
        cursor = self.db.cursor()
        results = None
        sql = """select location,remainTime,status,belong,message from """+self.name+";"
        try:
            # 执行sql语句
            cursor.execute(sql)
            results = cursor.fetchall()
            # for item in results:
            #     print(item)
        except Exception:
            print(Exception)
            # 如果发生错误则回滚
            self.db.rollback()
        return results

    def update(self):
        # 获取qrLink 和 location
        with open(os.path.abspath(os.path.dirname(__file__)) + "/../conf/" + self.name + ".json","r",encoding="utf8") as f:
            map = json.loads(f.read())



        for i in map:
            resJson = None
            # 根据belong不同选择不同checker
            if map[i]["belong"] == "UClean":
                # 选择UClean
                resJson = UClean_Checker().check(map[i])
            elif map[i]["belong"] == "soda":
                # 选择soda
                resJson = Soda_Checker().check(map[i])


            # update
            cursor = self.db.cursor()
            sql = "update "+self.name+" set remainTime=" + str(resJson["remainTime"]) + ",status=\""+resJson["status"] \
                    + "\",message=\""+resJson["message"] + "\" where name =\"" + i +"\";"

            cursor.execute(sql)
        try:
            self.db.commit()
            return "<h1>success!</h1>"
        except Exception:
            print(Exception)
            self.db.rollback()
            return "<h1>fail !</h1>"



    def getAll(self):
        '''
        获取所有洗衣机状态(location,remainTime,status,belong,message)
        :return:
        '''
        sqlRes = self.select()
        res=[]
        for i in sqlRes:
            item = {}
            item["location"] = i[0]
            item["remainTime"] = i[1]
            item["status"] = i[2]
            item["belong"] = i[3]
            item["message"] = i[4]
            res.append(item)
        return res
