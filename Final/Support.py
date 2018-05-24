<<<<<<< HEAD:Final/Support.py
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 21:57:30 2018

@author: Nicole
"""

import matplotlib.pyplot as plt

class Support:
    def __init__(self,x,y,support_x,support_y,size):
        self.x=x
        self.y=y
        self.support_x=int(support_x)
        self.support_y=int(support_y)
        self.size=size
        self.c1=1/15#支座长短系数1
        self.c2=1/24#支座长短系数2（大地）
        self.c3=20#点大小系数
        self.c_plw=1#点线宽系数
        self.c_lw=1#线宽系数
    def NoneSupport(self):
        pass
    def Horizontal(self):
        #仅有水平支座，向左画
        xList1=[self.x,self.x-self.c1*self.size]
        yList1=[self.y,self.y]
        plt.scatter(xList1[1],yList1[1],c='w',marker='o',s=self.c3,edgecolors='b',linewidths=self.c_plw,zorder=100)
        plt.plot(xList1,yList1,c='b',linewidth=self.c_lw,zorder=50)
        xList2=[self.x-self.c1*self.size,self.x-self.c1*self.size]
        yList2=[self.y+self.c2*self.size,self.y-self.c2*self.size]
        plt.plot(xList2,yList2,c='b',linewidth=self.c_lw,zorder=50)
    def Vertical(self):
        #仅有竖直支座，向下画
        xList1=[self.x,self.x]
        yList1=[self.y,self.y-self.c1*self.size]
        plt.scatter(xList1[1],yList1[1],c='w',marker='o',s=self.c3,edgecolors='b',linewidths=self.c_plw,zorder=100)
        plt.plot(xList1,yList1,c='b',linewidth=self.c_lw,zorder=50)
        xList2=[self.x-self.c2*self.size,self.x+self.c2*self.size]
        yList2=[self.y-self.c1*self.size,self.y-self.c1*self.size]
        plt.plot(xList2,yList2,c='b',linewidth=self.c_lw,zorder=50)
    def Plot(self):
        self.xswitcher={0:Support.NoneSupport,1:Support.Horizontal}
        self.xswitcher.get(self.support_x)(self)
        self.yswitcher={0:Support.NoneSupport,1:Support.Vertical}
        self.yswitcher.get(self.support_y)(self)
=======
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 21:57:30 2018

@author: Nicole
"""

import matplotlib.pyplot as plt

class Support:
    def __init__(self,x,y,support_x,support_y,size):
        self.x=x
        self.y=y
        self.support_x=int(support_x)
        self.support_y=int(support_y)
        self.size=size
        self.c1=1/15#支座长短系数1
        self.c2=1/24#支座长短系数2（大地）
        self.c3=20#点大小系数
        self.c_plw=1#点线宽系数
        self.c_lw=1#线宽系数
    def NoneSupport(self):
        pass
    def Horizontal(self):
        #仅有水平支座，向左画
        xList1=[self.x,self.x-self.c1*self.size]
        yList1=[self.y,self.y]
        plt.scatter(xList1[1],yList1[1],c='w',marker='o',s=self.c3,edgecolors='b',linewidths=self.c_plw,zorder=100)
        plt.plot(xList1,yList1,c='b',linewidth=self.c_lw,zorder=50)
        xList2=[self.x-self.c1*self.size,self.x-self.c1*self.size]
        yList2=[self.y+self.c2*self.size,self.y-self.c2*self.size]
        plt.plot(xList2,yList2,c='b',linewidth=self.c_lw,zorder=50)
    def Vertical(self):
        #仅有竖直支座，向下画
        xList1=[self.x,self.x]
        yList1=[self.y,self.y-self.c1*self.size]
        plt.scatter(xList1[1],yList1[1],c='w',marker='o',s=self.c3,edgecolors='b',linewidths=self.c_plw,zorder=100)
        plt.plot(xList1,yList1,c='b',linewidth=self.c_lw,zorder=50)
        xList2=[self.x-self.c2*self.size,self.x+self.c2*self.size]
        yList2=[self.y-self.c1*self.size,self.y-self.c1*self.size]
        plt.plot(xList2,yList2,c='b',linewidth=self.c_lw,zorder=50)
    def Plot(self):
        self.xswitcher={0:Support.NoneSupport,1:Support.Horizontal}
        self.xswitcher.get(self.support_x)(self)
        self.yswitcher={0:Support.NoneSupport,1:Support.Vertical}
        self.yswitcher.get(self.support_y)(self)
>>>>>>> 8b97942996753b96dda6f542a9bd993f9d3cb72b:PostProcess/Support.py
