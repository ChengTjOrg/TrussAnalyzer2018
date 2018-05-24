# -*- coding: utf-8 -*-
"""
Created on Thu May 24 18:21:29 2018

@author: Nicole
"""

import matplotlib.pyplot as plt
import math

class Rod:
    def __init__(self,node1,node2,result):
        self.node1=node1
        self.node2=node2
        self.size=self.node1.size
        self.result=result
        self.c_rod=2
        self.c_result=8
    def PlotRod(self):
        x=[self.node1.x,self.node2.x]
        y=[self.node1.y,self.node2.y]
        plt.plot(x,y,c='grey',linewidth=self.c_rod,zorder=1)
    def PlotResult(self):
        if self.node1.x==self.node2.x:
            if self.node1.y>self.node2.y:
                angle=-90
            else:
                angle=90
        else:
            angle=math.atan((self.node2.y-self.node1.y)/(self.node2.x-self.node1.x))/(2*math.pi)*360
        plt.text((self.node1.x+self.node2.x)/2,(self.node1.y+self.node2.y)/2,str(self.result),fontsize=self.c_result,rotation=angle,rotation_mode='anchor',zorder=1000)
    