# -*- coding: utf-8 -*-
# 项目入口
import os

from flask import Flask
import json
from conf.allowList import allowList
from controller.factory import *
from controller.logger import *
from conf.config import config
from Checker import Soda_Checker, UClean_Checker
from flask_apscheduler import APScheduler
import pymysql

logger = logger()
db = pymysql.connect(config["sqlUrl"],config["user"],config["passwd"],config["database"])
scheduler = APScheduler()
app = Flask(__name__)
app.config["path"] = os.path.abspath(os.path.dirname(__file__))

# TODO 将controller设置为application对象/requests对象

def preventEvil(s):
    #TODO 阻止非法访问
    pass

@app.route('/')
def hello_world():
    return 'Hello World! message from xWash!'

# 测试用
@app.route("/update/<building>")
def update(building):
    '''
    测试用
    :param building: 宿舍楼
    :return: 更新成功与否
    '''

    logger.info("更新" + building + "数据")

    # 新建controller
    fc = factory(db)
    controller = fc.getController(building)

    return controller.update()


@app.route('/<school>/<building>')
def scnu(school,building):
    # 过滤非法请求
    if school == "" or building=="":
        return "<h1>非法进入</h1>"

    if(school not in allowList):
        return "<h1>不支持该学校</h1>"

    if(building not in allowList[school]):
        return "<h1>不支持该宿舍楼</h1>"

    # 查询返回
    fc = factory(db)
    controller = fc.getController(building)

    return str(controller.getAll())

# 旧接口
@app.route('/api/all')
def getAll():
    # 新建controller
    fc = factory(db)
    controller = fc.getController("D19")

    return str(controller.getAll())


if __name__ == '__main__':
    # 设置定时任务
    scheduler.init_app(app=app)
    scheduler.add_job(func=update, id='1', args=("D19",), trigger='interval', seconds=config['autoUpdateTime'], replace_existing=True)
    scheduler.start()

    # 设置日志路径
    logger.init(path=os.getcwd() + '/back-end/logs/')

    # 开启服务
    app.run("0.0.0.0",port=5000,debug=False)
