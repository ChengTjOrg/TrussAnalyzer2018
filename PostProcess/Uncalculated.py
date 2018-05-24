# -*- coding: utf-8 -*-
"""
Created on Thu May 24 20:06:25 2018

@author: Nicole
"""

import numpy as np
import matplotlib.pyplot as plt
import Truss
import Node

class Uncalculated:
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
    def UncalculatedLoadData(self):
        (node1_x,node1_y,node1_support_x,node1_support_y,node1_fx,node1_fy)=np.loadtxt(self.path,skiprows=0,delimiter=' ',dtype=float,usecols=(1,2,3,4,5,6),unpack=True)
        (node2_x,node2_y,node2_support_x,node2_support_y,node2_fx,node2_fy)=np.loadtxt(self.path,skiprows=0,delimiter=' ',dtype=float,usecols=(8,9,10,11,12,13),unpack=True)
        #if True:
        self.node1_x=node1_x.tolist()
        self.node1_y=node1_y.tolist()
        self.node1_support_x=node1_support_x.tolist()
        self.node1_support_y=node1_support_y.tolist()
        self.node2_x=node2_x.tolist()
        self.node2_y=node2_y.tolist()
        self.node2_support_x=node2_support_x.tolist()
        self.node2_support_y=node2_support_y.tolist()
        self.node1_fx=node1_fx.tolist()
        self.node1_fy=node1_fy.tolist()
        self.node2_fx=node2_fx.tolist()
        self.node2_fy=node2_fy.tolist()
        '''else:
            self.node1_x=list(node1_x)
            self.node1_y=list(node1_y)
            self.node1_support_x=list(node1_support_x)
            self.node1_support_y=list(node1_support_y)
            self.node2_x=list(node2_x)
            self.node2_y=list(node2_y)
            self.node2_support_x=list(node2_support_x)
            self.node2_support_y=list(node2_support_y)
            self.node1_fx=list(node1_fx)
            self.node1_fy=list(node1_fy)
            self.node2_fx=list(node2_fx)
            self.node2_fy=list(node2_fy)
        '''
    def UncalculatedPlot(self):
        if type(self.node1_x)==float:
            self.result=0
            self.size=max(abs(self.node1_x-self.node2_x),abs(self.node1_y-self.node2_y))
            plt.scatter(self.size,self.size,c='w',marker='o', s=6*self.size,edgecolors='w',linewidths=0.3*self.size, zorder=0.5)      #通过画白色点的方式微调画布尺寸使边角上的力能显示在画布范围内
            self.node1=Node.Node(self.node1_x,self.node1_y,self.node1_support_x,self.node1_support_y,self.node1_fx,self.node1_fy,self.size,self.ax)
            self.node2=Node.Node(self.node2_x,self.node2_y,self.node2_support_x,self.node2_support_y,self.node2_fx,self.node2_fy,self.size,self.ax)
            self.truss=Truss.Truss(self.node1,self.node2,self.size,self.result,self.ax)
            self.truss.size=self.size
            self.truss.PlotUncalculatedTruss()
        else:
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
            for i in range(len(self.node1_x)):
                self.node1=Node.Node(self.node1_x[i],self.node1_y[i],self.node1_support_x[i],self.node1_support_y[i],self.node1_fx[i],self.node1_fy[i],self.size,self.ax)
                self.node2=Node.Node(self.node2_x[i],self.node2_y[i],self.node2_support_x[i],self.node2_support_y[i],self.node2_fx[i],self.node2_fy[i],self.size,self.ax)
                self.truss=Truss.Truss(self.node1,self.node2,self.size,0,self.ax)
                self.truss.size=self.size
                self.truss.PlotUncalculatedTruss()   
    def UncalculatedSaveFig(self):
        plt.savefig('Uncalculated.png',dpi=600)