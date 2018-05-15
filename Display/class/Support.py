# -*- coding: utf-8 -*-
"""
Created on Tue May 15 21:57:30 2018

@author: Nicole
"""

class Support:
    def __init__(self,s,a,b,l,sc):
        self.s=s
        self.a=a
        self.b=b
        self.l=l
        self.c1=1/25#支座长短系数1
        self.c2=1/50#支座长短系数2（大地）
        self.sc=sc
    def none(self):
        pass
    def horizontal(self):
        #仅有水平支座，向左画
        x=[self.a,self.a-self.c1*self.l]
        y=[self.b,self.b]
        plt.scatter(x[1],y[1],c='w',marker='o',s=50,edgecolors=self.sc,linewidths=2,zorder=100)
        plt.plot(x,y,c=self.sc,linewidth=2.5,zorder=1)
        x1=[self.a-self.c1*self.l,self.a-self.c1*self.l]
        y1=[self.b+self.c2*self.l,self.b-self.c2*self.l]
        plt.plot(x1,y1,c=self.sc,linewidth=2.5,zorder=1)
    def vertical(self):
        #仅有竖直支座，向下画
        x=[self.a,self.a]
        y=[self.b,self.b-self.c1*self.l]
        plt.scatter(x[1],y[1],c='w',marker='o',s=50,edgecolors=self.sc,linewidths=2,zorder=100)
        plt.plot(x,y,c=self.sc,linewidth=2.5,zorder=1)
        x1=[self.a-self.c2*self.l,self.a+self.c2*self.l]
        y1=[self.b-self.c1*self.l,self.b-self.c1*self.l]
        plt.plot(x1,y1,c=self.sc,linewidth=2.5,zorder=1)
    def both(self):
        #有两个方向的支座
        Support.horizontal(self)
        Support.vertical(self)
    def display(self):
        self.switcher={0:Support.none,1:Support.horizontal,2:Support.vertical,3:Support.both}
        self.switcher.get(self.s)(self)
    '''要注意支座图像的放置方向和大小不要与杆件重叠!!'''