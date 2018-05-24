# -*- coding: utf-8 -*-
"""
Created on Thu May 24 17:43:08 2018

@author: Nicole
"""

import matplotlib.pyplot as plt
import Support
import Force

class Node:
    def __init__(self,x,y,support_x,support_y,fx,fy,size,ax):
        self.x=x
        self.y=y
        self.support_x=support_x
        self.support_y=support_y
        self.fx=fx
        self.fy=fy
        self.size=size
        self.ax=ax
        self.c_s=6
        self.c_lw=0.3
    def PlotNode(self):
        plt.scatter(self.x,self.y,c='w',marker='o', s=self.c_s*self.size,edgecolors='k',linewidths=self.c_lw*self.size, zorder=100)
    def PlotSupport(self):
        support=Support.Support(self.x,self.y,self.support_x,self.support_y,self.size)
        support.Plot()
    def PlotForce(self):
        force=Force.Force(self.x,self.y,self.fx,self.fy,self.size,self.ax)
        force.Plot()