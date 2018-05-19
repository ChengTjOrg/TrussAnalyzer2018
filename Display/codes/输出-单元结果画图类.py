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

        
class PostUnitDisplay:
    def __init__(self,a1,b1,a2,b2,s1,s2,l,tc,pc,sc,result):
        self.a1=a1
        self.b1=b1
        self.a2=a2
        self.b2=b2
        self.s1=s1
        self.s2=s2
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
        self.c5=5#数字大小系数
        self.trusslength=math.sqrt((a2-a1)**2+(b2-b1)**2)
    def display(self):
        #plt.figure()
        plt.figure(figsize=(self.l,self.l))
        plt.xlim(0,self.l)
        plt.ylim(0,self.l)
        #画两端结点
        x=[self.a1,self.a2]
        y=[self.b1,self.b2]
        plt.scatter(x,y,c='w',marker='o', s=60,edgecolors=self.pc,linewidths=3, zorder=100)#s是点大小
        #画杆
        plt.plot(x,y,c=self.tc,linewidth=5,zorder=1)
        #画支座
        sp1=Support.Support(self.s1,self.a1,self.b1,self.l,self.sc)
        sp1.display()
        sp2=Support.Support(self.s2,self.a2,self.b2,self.l,self.sc)
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
        plt.text((l1[0]+l2[0])/2,(l1[1]+l2[1])/2,str(self.result),fontsize=self.c5*self.trusslength,rotation=angle,rotation_mode='anchor',zorder=1000)
        #plt.tight_layout()
        plt.savefig('path\\fig.png',dpi=600)
        plt.show()


pud=PostUnitDisplay(1.8,1.4,6.8,6.4,3,1,8.0,'k','k','b',48.6667)
pud.display()
