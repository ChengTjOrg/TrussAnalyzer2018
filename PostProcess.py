# -*- coding: utf-8 -*-
"""
Created on Mon May 21 15:55:43 2018

@author: Nicole
"""

import numpy as np
import matplotlib.pyplot as plt
import UnitPostProcess
import UnitPreProcess

class postProcess:
    def __init__(self,l):
        self.l=l
    def loadtruss(self):
        (a1,b1,sx1,sy1,a2,b2,sx2,sy2,fn,dx1,dy1,dx2,dy2)=np.loadtxt('temp.txt',skiprows=0,delimiter=' ',dtype=float,usecols=(1,2,3,4,8,9,10,11,15,16,17,18,19),unpack=True)
        self.x1=list(a1+dx1)
        self.y1=list(b1+dy1)
        self.x2=list(a2+dx2)
        self.y2=list(b2+dy2)
        #支座（0，1，2，3）到（0，1）*（0，1）的转换;支座方向要确定的话需要两个点的数据
        self.sx1=list(sx1)
        self.sy1=list(sy1)
        self.sx2=list(sx2)
        self.sy2=list(sy2)
        self.fn=list(fn)
    def loadtruss2(self):
        (a1,b1,sx1,sy1,a2,b2,sx2,sy2)=np.loadtxt('temp.txt',skiprows=0,delimiter=' ',usecols=(1,2,3,4,8,9,10,11),unpack=True)
        self.x1=list(a1)
        self.y1=list(b1)
        self.x2=list(a2)
        self.y2=list(b2)
        #支座（0，1，2，3）到（0，1）*（0，1）的转换;支座方向要确定的话需要两个点的数据
        self.sx1=list(sx1)
        self.sy1=list(sy1)
        self.sx2=list(sx2)
        self.sy2=list(sy2)
    def setfig(self):
        plt.figure(figsize=(self.l,self.l))
        plt.xlim(-1,self.l)
        plt.ylim(-1,self.l)
    def plot(self):
        for i in range(len(self.x1)):
            upp=UnitPostProcess.UnitPostProcess(self.x1[i],self.y1[i],self.x2[i],self.y2[i],self.sx1[i],self.sy1[i],self.sx2[i],self.sy2[i],self.l,self.fn[i])
            upp.plot()
    def plot2(self):
        for i in range(len(self.x1)):
            upp=UnitPreProcess.UnitPreProcess(self.x1[i],self.y1[i],self.x2[i],self.y2[i],self.sx1[i],self.sy1[i],self.sx2[i],self.sy2[i],self.l)
            upp.plot()
    def savefig(self):
        plt.savefig('fig.png',dpi=600)
