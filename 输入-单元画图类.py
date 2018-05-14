# -*- coding: utf-8 -*-
"""
Created on Mon May 14 17:48:43 2018

@author: Nicole
"""

#pre display in unit

#import numpy as np
from __future__ import division
import matplotlib.pyplot as plt


class PreUnitDisplay:
    def __init__(self,a1,b1,a2,b2,s1,s2,lx,ly):#依次为x坐标/y坐标/支座情况/画布大小,lx,ly只需全局输入一次
        self.a1=a1
        self.b1=b1
        self.a2=a2
        self.b2=b2
        self.s1=s1
        self.s2=s2
        self.lx=lx
        self.ly=ly
        self.l=min(self.lx,self.ly)
        self.c1=1#杆端圆圈大小系数
        self.c2=1/20#杆端圆圈线宽系数
        self.c3=0.1#杆线宽系数
    def display(self):
        plt.xlim(0,self.lx)
        plt.ylim(0,self.ly)
        #画两端结点
        x=[self.a1,self.a2]
        y=[self.b1,self.b2]
        '''plt.plot(x[0], y[0], 'C3', zorder=1,lw=3)#zorder用来标记显示顺序（层次）
        plt.plot(x[1], y[1], 'C3', zorder=1,lw=3)'''
        plt.scatter(x,y,c='w',marker='o', s=self.c1*self.l,edgecolors='k',linewidths=self.c2*self.l, zorder=100)#s是点大小
        #画杆
        plt.plot(x,y,c='r',linewidth=self.c3*self.l,zorder=1)
        #画支座
        sp1=Support(self.s1,self.a1,self.b1,self.l)
        sp1.display()
        sp2=Support(self.s2,self.a2,self.b2,self.l)
        sp2.display()
        plt.tight_layout()


class Support:
    def __init__(self,s,a,b,l):
        self.s=s
        self.a=a
        self.b=b
        self.l=l
        self.c1=1/15#支座长短系数1
        self.c2=1/30#支座长短系数2（大地）
        self.c3=1#支座圆圈大小s系数
        self.c4=1/25#支座圆圈线宽系数
        self.c5=1/20#支座线条宽度系数
    def none(self):
        pass
    def horizontal(self):
        #仅有水平支座，向左画
        x=[self.a,self.a-self.c1*self.l]
        y=[self.b,self.b]
        plt.scatter(x[1],y[1],c='w',marker='o',s=self.c3*self.l,edgecolors='b',linewidths=self.c4*self.l,zorder=100)
        plt.plot(x,y,c='b',linewidth=self.c5*self.l,zorder=1)
        x1=[self.a-self.c1*self.l,self.a-self.c1*self.l]
        y1=[self.b+self.c2*self.l,self.b-self.c2*self.l]
        plt.plot(x1,y1,c='b',linewidth=self.c5*self.l,zorder=1)
    def vertical(self):
        #仅有竖直支座，向下画
        x=[self.a,self.a]
        y=[self.b,self.b-self.c1*self.l]
        plt.scatter(x[1],y[1],c='w',marker='o',s=self.c3*self.l,edgecolors='b',linewidths=self.c4*self.l,zorder=100)
        plt.plot(x,y,c='b',linewidth=self.c5*self.l,zorder=1)
        x1=[self.a-self.c2*self.l,self.a+self.c2*self.l]
        y1=[self.b-self.c1*self.l,self.b-self.c1*self.l]
        plt.plot(x1,y1,c='b',linewidth=self.c5*self.l,zorder=1)
    def both(self):
        #有两个方向的支座
        Support.horizontal(self)
        Support.vertical(self)
    def display(self):
        self.switcher={0:Support.none,1:Support.horizontal,2:Support.vertical,3:Support.both}
        self.switcher.get(self.s)(self)
    '''要注意支座图像的放置方向和大小不要与杆件重叠!!'''
   

pud=PreUnitDisplay(25,10,40,22,3,1,100,50)
pud.display()     
       

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
