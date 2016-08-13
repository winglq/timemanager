'''
Created on Nov 24, 2014
@author: Liu Qing
'''
import random
class Cfg:
    def __init__(self):
        self.worktime=2
        self.resttime=random.randint(3, 5) * 60
        self.delayTime=300
        self.resttime_long = random.randint(25, 30) * 60
        self.small_break_count = random.randint(4, 5)
        
