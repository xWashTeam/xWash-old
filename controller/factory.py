# -*- coding: utf-8 -*-
from xWash.controller.baseController import *
class factory:
    db = None
    def __init__(self,db):
        self.db = db

    def getController(self,name):
        return baseController(self.db,name)