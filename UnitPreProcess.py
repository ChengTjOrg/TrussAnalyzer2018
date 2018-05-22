# -*- coding: utf-8 -*-
"""
Created on Mon May 14 17:48:43 2018

@author: Nicole
"""

#pre display in unit

#import numpy as np
from __future__ import division
import matplotlib.pyplot as plt
#import pylab as plb
import Support

class UnitPreProcess:
    def __init__(self,a1,b1,a2,b2,sx1,sy1,sx2,sy2,l):#依次为x坐标/y坐标/支座情况/画布大小/构件颜色,lx,ly只需全局输入一次
        self.a1=a1
        self.b1=b1
        self.a2=a2
        self.b2=b2
        self.sx1=sx1
        self.sy1=sy1
        self.sx2=sx2
        self.sy2=sy2
        self.l=l
        self.tc='k'#杆颜色
        self.pc='k'#端点颜色
        self.sc='b'#支座颜色
    def setfig(self):
        plt.figure(figsize=(self.l,self.l))
        plt.xlim(0,self.l)
        plt.ylim(0,self.l)
    def plot(self):
        #画两端结点
        x=[self.a1,self.a2]
        y=[self.b1,self.b2]
        plt.scatter(x,y,c='w',marker='o', s=60,edgecolors=self.pc,linewidths=3, zorder=100)#s是点大小
        #画杆
        plt.plot(x,y,c=self.tc,linewidth=5,zorder=1)
        #画支座
        sp1=Support.Support(self.sx1,self.sy1,self.a1,self.b1,self.l,self.sc)
        sp1.display()
        sp2=Support.Support(self.sx2,self.sy2,self.a2,self.b2,self.l,self.sc)
        sp2.display()
        plt.tight_layout()
    def savefig(self):
        plt.savefig('prefig.png',dpi=600)
        plt.show()

'''
upp=UnitPreProcess(2.5,1.0,4.0,2.2,1,1,1,0,5.0)
upp.setfig()
upp.plot()
upp.savefig()     
'''

'''
问题：
1.程序中有大段重复的相似语句，不知道有没有办法优化
2.注释还没有认真写好
3.支座的方向是单一的，可能会出现重叠遮挡的问题，目前暂时采用了不同颜色作为解决方案，但是这个方案还不够好
'''


    
'''
弃用代码：
def supports(argument):
    switcher={
        0:pass
        1:pass#仅有水平支座
        2:pass#仅有竖直支座
        3:pass#有两个方向的支座
        #要注意支座图像的放置方向和大小不要与杆件重叠!!
            }'''
