# -*- coding: utf-8 -*-
"""
Created on Tue May 15 19:36:24 2018

@author: Nicole
"""

#post display

from __future__ import division
import Support
import numpy as np
import matplotlib.pyplot as plt
import math

        
class UnitPostProcess:
    def __init__(self,a1,b1,a2,b2,sx1,sy1,sx2,sy2,l,tc,pc,sc,result):
        self.a1=a1
        self.b1=b1
        self.a2=a2
        self.b2=b2
        self.sx1=sx1
        self.sy1=sy1
        self.sx2=sx2
        self.sy2=sy2
        self.l=l
        self.tc=tc
        self.pc=pc
        self.sc=sc
        self.result=result
        self.x=[a1,a2]
        self.x=np.array(self.x)
        self.y=[b1,b2]
        self.y=np.array(self.y)
        self.c1=0.09
        self.c2=0.06
        self.c3=0.09
        self.c4=0.02
        self.c5=1.2#数字大小系数
        self.trusslength=math.sqrt((a2-a1)**2+(b2-b1)**2)
    def setfig(self):
        #plt.figure()
        plt.figure(figsize=(self.l,self.l))
        plt.xlim(0,self.l)
        plt.ylim(0,self.l)
    def plot(self):    
        #画两端结点
        x=[self.a1,self.a2]
        y=[self.b1,self.b2]
        plt.scatter(x,y,c='w',marker='o', s=10*self.l,edgecolors=self.pc,linewidths=3, zorder=100)#s是点大小
        #画杆
        plt.plot(x,y,c=self.tc,linewidth=5,zorder=1)
        #画支座
        sp1=Support.Support(self.sx1,self.sy1,self.a1,self.b1,self.l,self.sc)
        sp1.display()
        sp2=Support.Support(self.sx2,self.sy2,self.a2,self.b2,self.l,self.sc)
        sp2.display()
        #标数据
        l1 = np.array([self.a1,self.b1])
        l2 = np.array([self.a2,self.b2])
        #计算角度
        if self.a1==self.a2:
            if self.b1>self.b2:
                angle=-90
            else:
                angle=90
        else:
            angle=math.atan((self.b2-self.b1)/(self.a2-self.a1))/(2*math.pi)*360
        plt.text((l1[0]+l2[0])/2,(l1[1]+l2[1])/2,str(self.result),fontsize=self.c5*self.l,rotation=angle,rotation_mode='anchor',zorder=1000)
        #plt.tight_layout()
    def savefig(self):
        #fig = plt.gcf()
        #fig.set_size_inches(20,20)
        plt.savefig('C:\\文件\\大二下\\绗架结构分析助手\\图像\\后处理\\fig.png',dpi=600)
        plt.show()


pud=UnitPostProcess(1.8,1.4,6.8,6.4,1,1,1,0,20.0,'k','k','b',48.6667)
pud.setfig()
pud.plot()
pud=UnitPostProcess(6.8,6.4,18.8,6.4,0,0,1,1,20.0,'k','k','b',23.3333)
pud.plot()
pud.savefig()
