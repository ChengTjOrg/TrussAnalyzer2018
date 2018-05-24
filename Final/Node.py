<<<<<<< HEAD:Final/Node.py
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
        self.c_s=24
        self.c_lw=1.2
    def PlotNode(self):
        plt.scatter(self.x,self.y,c='w',marker='o', s=self.c_s,edgecolors='k',linewidths=self.c_lw, zorder=100)
    def PlotSupport(self):
        support=Support.Support(self.x,self.y,self.support_x,self.support_y,self.size)
        support.Plot()
    def PlotForce(self):
        force=Force.Force(self.x,self.y,self.fx,self.fy,self.size,self.ax)
=======
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
        self.c_s=24
        self.c_lw=1.2
    def PlotNode(self):
        plt.scatter(self.x,self.y,c='w',marker='o', s=self.c_s,edgecolors='k',linewidths=self.c_lw, zorder=100)
    def PlotSupport(self):
        support=Support.Support(self.x,self.y,self.support_x,self.support_y,self.size)
        support.Plot()
    def PlotForce(self):
        force=Force.Force(self.x,self.y,self.fx,self.fy,self.size,self.ax)
>>>>>>> 8b97942996753b96dda6f542a9bd993f9d3cb72b:PostProcess/Node.py
        force.Plot()