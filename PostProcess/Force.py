# -*- coding: utf-8 -*-
"""
Created on Tue May 22 16:37:53 2018

@author: Nicole
"""

class Force:
    def __init__(self,a,b,fx,fy,size,ax):
        self.a=a
        self.b=b
        self.fx=fx
        self.fy=fy
        self.size=size
        self.ax=ax
        self.c1=0.4#width系数
        self.c2=1#headwidth系数
        self.c3=1#箭头头部长度系数
    def Plot(self):
        d=1/5*self.size
        if self.fx>0:
            self.ax.annotate(str(self.fx), xy=(self.a,self.b), xytext=(self.a-1.6*d,self.b),arrowprops=dict(facecolor='r', shrink=0.005*self.size,width=self.c1*self.size,headwidth=self.c2*self.size,headlength=self.c3*self.size),zorder=800)
        elif self.fx<0:
            self.ax.annotate(str(self.fx), xy=(self.a,self.b), xytext=(self.a+1.6*d,self.b),arrowprops=dict(facecolor='r', shrink=0.005*self.size,width=self.c1*self.size,headwidth=self.c2*self.size,headlength=self.c3*self.size),zorder=800)    
        if self.fy>0:
            self.ax.annotate(str(self.fy), xy=(self.a,self.b), xytext=(self.a,self.b-d),arrowprops=dict(facecolor='r', shrink=0.005*self.size,width=self.c1*self.size,headwidth=self.c2*self.size,headlength=self.c3*self.size),zorder=800)
        elif self.fy<0:
            self.ax.annotate(str(self.fy), xy=(self.a,self.b), xytext=(self.a,self.b+d),arrowprops=dict(facecolor='r', shrink=0.005*self.size,width=self.c1*self.size,headwidth=self.c2*self.size,headlength=self.c3*self.size),zorder=800)
        #plt.show()
        #plt.savefig('C:\\文件\\大二下\\绗架结构分析助手\\图像\\fig.png',dpi=600)

'''
f=Force(2,3,5,10,5)
f.ForcePlot()
'''