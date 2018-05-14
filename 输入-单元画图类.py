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
    def __init__(self,a1,b1,a2,b2,c1,c2):
        self.a1=a1
        self.b1=b1
        self.a2=a2
        self.b2=b2
        self.c1=c1
        self.c2=c2  
    def display(self):
        #画两端结点
        x=[self.a1,self.a2]
        y=[self.b1,self.b2]
        '''plt.plot(x[0], y[0], 'C3', zorder=1,lw=3)#zorder用来标记显示顺序（层次）
        plt.plot(x[1], y[1], 'C3', zorder=1,lw=3)'''
        plt.scatter(x,y,c='w',marker='o', s=120,edgecolors='k',linewidths=3, zorder=100)#s是点大小
        #画杆
        plt.plot(x,y,c='grey',linewidth=6,zorder=1)
        #画支座
        s1=Support(self.c1,self.a1,self.b1)
        s1.display()
        s2=Support(self.c2,self.a2,self.b2)
        s2.display()
        plt.tight_layout()


class Support:
    def __init__(self,c,a,b):
        self.c=c
        self.a=a
        self.b=b
    def none(self):
        pass
    def horizontal(self):
        #仅有水平支座，向左画
        x=[self.a,self.a-0.6]
        y=[self.b,self.b]
        plt.scatter(x[1],y[1],c='w',marker='o',s=100,edgecolors='b',linewidths=2.5,zorder=100)
        plt.plot(x,y,c='b',linewidth=4,zorder=1)
        x1=[self.a-0.6,self.a-0.6]
        y1=[self.b+0.4,self.b-0.4]
        plt.plot(x1,y1,c='b',linewidth=4,zorder=1)
    def vertical(self):
        #仅有竖直支座，向下画
        x=[self.a,self.a]
        y=[self.b,self.b-0.6]
        plt.scatter(x[1],y[1],c='w',marker='o',s=100,edgecolors='b',linewidths=2.5,zorder=100)
        plt.plot(x,y,c='b',linewidth=4,zorder=1)
        x1=[self.a-0.4,self.a+0.4]
        y1=[self.b-0.6,self.b-0.6]
        plt.plot(x1,y1,c='b',linewidth=4,zorder=1)
    def both(self):
        #有两个方向的支座
        Support.horizontal(self)
        Support.vertical(self)
    def display(self):
        self.switcher={0:Support.none,1:Support.horizontal,2:Support.vertical,3:Support.both}
        self.switcher.get(self.c)(self)
    '''要注意支座图像的放置方向和大小不要与杆件重叠!!'''
   

pud=PreUnitDisplay(5,10,12,4,1,3)
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
