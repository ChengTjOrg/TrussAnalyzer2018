# -*- coding: utf-8 -*-
"""
Created on Tue May 15 21:58:04 2018

@author: Nicole
"""

from __future__ import division
import matplotlib.pyplot as plt
import Support

class PreUnitDisplay:
    def __init__(self,a1,b1,a2,b2,s1,s2,l,tc,pc,sc):#依次为x坐标/y坐标/支座情况/画布大小/构件颜色,lx,ly只需全局输入一次
        self.a1=a1
        self.b1=b1
        self.a2=a2
        self.b2=b2
        self.s1=s1
        self.s2=s2
        self.l=l
        self.tc=tc#杆颜色
        self.pc=pc#端点颜色
        self.sc=sc#支座颜色
    def display(self):
        plt.figure(figsize=(self.l,self.l))
        #画两端结点
        x=[self.a1,self.a2]
        y=[self.b1,self.b2]
        '''plt.plot(x[0], y[0], 'C3', zorder=1,lw=3)#zorder用来标记显示顺序（层次）
        plt.plot(x[1], y[1], 'C3', zorder=1,lw=3)'''
        plt.scatter(x,y,c='w',marker='o', s=60,edgecolors=self.pc,linewidths=3, zorder=100)#s是点大小
        #画杆
        plt.plot(x,y,c=self.tc,linewidth=5,zorder=1)
        #画支座
        sp1=Support(self.s1,self.a1,self.b1,self.l,self.sc)
        sp1.display()
        sp2=Support(self.s2,self.a2,self.b2,self.l,self.sc)
        sp2.display()
        plt.tight_layout()
