# -*- coding: utf-8 -*-
"""
Created on Thu May 24 20:04:14 2018
@author: Nicole
"""

import numpy as np
import matplotlib.pyplot as plt
import Truss
import Node

class Calculated:
    def __init__(self,path):
        self.path=str(path)
        self.size=0
        self.x_min=self.y_min=self.x_max=self.y_max=0
    def SetFig(self):
        fig,ax=plt.subplots()
        self.ax=ax
        self.ax = plt.gca()
        self.ax.set_aspect(1)
        fig.tight_layout()
    def CalculatedLoadData(self):
        (node1_x,node1_y,node1_support_x,node1_support_y,node1_fx,node1_fy)=np.loadtxt(self.path,skiprows=0,delimiter=' ',dtype=float,usecols=(1,2,3,4,5,6),unpack=True)
        (node2_x,node2_y,node2_support_x,node2_support_y,node2_fx,node2_fy)=np.loadtxt(self.path,skiprows=0,delimiter=' ',dtype=float,usecols=(8,9,10,11,12,13),unpack=True)
        (result,node1_dx,node1_dy,node2_dx,node2_dy)=np.loadtxt(self.path,skiprows=0,delimiter=' ',dtype=float,usecols=(15,16,17,18,19),unpack=True)
        self.node1_x=list(node1_x+node1_dx)
        self.node1_y=list(node1_y+node1_dy)
        self.node1_support_x=list(node1_support_x)
        self.node1_support_y=list(node1_support_y)
        self.node2_x=list(node2_x+node2_dx)
        self.node2_y=list(node2_y+node2_dy)
        self.node2_support_x=list(node2_support_x)
        self.node2_support_y=list(node2_support_y)
        self.result=list(result)
        self.node1_fx=list(node1_fx)
        self.node1_fy=list(node1_fy)
        self.node2_fx=list(node2_fx)
        self.node2_fy=list(node2_fy)
    def CalculatedPlot(self):
        for i in range(len(self.node1_x)):
            if max(self.node1_x[i],self.node2_x[i])>self.x_max:
                self.x_max=max(self.node1_x[i],self.node2_x[i])
            if max(self.node1_y[i],self.node2_y[i]):
                self.y_max=max(self.node1_y[i],self.node2_y[i])
            if min(self.node1_x[i],self.node2_x[i])<self.x_min:
                self.x_min=min(self.node1_x[i],self.node2_x[i])
            if min(self.node1_y[i],self.node2_y[i]):
                self.y_min=min(self.node1_y[i],self.node2_y[i])
            self.size=max(self.x_max-self.x_min,self.y_max-self.y_min)    
        plt.scatter(self.size,self.size,c='w',marker='o', s=6*self.size,edgecolors='w',linewidths=0.3*self.size, zorder=0.5)      #通过画白色点的方式微调画布尺寸使边角上的力能显示在画布范围内
        for i in range(len(self.result)):
            self.node1=Node.Node(self.node1_x[i],self.node1_y[i],self.node1_support_x[i],self.node1_support_y[i],self.node1_fx[i],self.node1_fy[i],self.size,self.ax)
            self.node2=Node.Node(self.node2_x[i],self.node2_y[i],self.node2_support_x[i],self.node2_support_y[i],self.node2_fx[i],self.node2_fy[i],self.size,self.ax)
            self.truss=Truss.Truss(self.node1,self.node2,self.size,self.result[i],self.ax)
            self.truss.size=self.size
            self.truss.PlotCalculatedTruss()
            plt.scatter(self.size,self.size,c='w',marker='o', s=6*self.size,edgecolors='w',linewidths=0.3*self.size, zorder=0.5)      #通过画白色点的方式微调画布尺寸使边角上的力能显示在画布范围内
    def CalculatedSaveFig(self):
        plt.savefig('Calculated.png',dpi=600)