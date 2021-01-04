# 后端

## 环境

- python版本 :  `python 3.6`

- 安装依赖 : `pip install -r requirements.txt`

- mysql版本 : `mysql 8.02`

- 建表 `source xWash.sql`

## 配置

[conf.py](https://github.com/xWashTeam/xWash/blob/main/back-end/conf/config.py)

- 数据库连接数据
- 自动爬取洗衣机状态间隔

[allowList](https://github.com/xWashTeam/xWash/blob/main/back-end/conf/allowList.py)

- 允许访问的宿舍楼

[xWash/back-end/conf/xxx.json](https://github.com/xWashTeam/xWash/blob/main/back-end/conf/D19.json)(以D19示例)

- key值格式: 宿舍楼\_方向\_楼层
- name : 各个洗衣机的名字
- belong : 洗衣机的品牌
- location : 位置
- qrLink : 各个洗衣机二维码数据

## 路由

