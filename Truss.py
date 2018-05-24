# -*- coding: utf-8 -*-
"""
Created on Thu May 24 18:18:36 2018

@author: Nicole
"""


from __future__ import division
import Rod
import matplotlib.pyplot as plt
import math

class Truss:
    def __init__(self,node1,node2,size,result,ax):
        self.node1=node1
        self.node2=node2
        self.rod=Rod.Rod(node1,node2,result)
        self.size=size
        self.result=result
        self.ax=ax
        self.length=math.sqrt((node1.x-node2.x)**2+(node1.y-node2.y)**2)
    def PlotCalculatedTruss(self):    
        self.node1.PlotNode()
        self.node1.PlotSupport()
        self.node1.PlotForce()
        self.node2.PlotNode()
        self.node2.PlotSupport()
        self.node2.PlotForce()
        self.rod.PlotRod()
        self.rod.PlotResult()
    def PlotUncalculatedTruss(self):
        self.node1.PlotNode()
        self.node1.PlotSupport()
        self.node1.PlotForce()
        self.node2.PlotNode()
        self.node2.PlotSupport()
        self.node2.PlotForce()
        self.rod.PlotRod()
    def SaveTrussFig(self):
        plt.savefig('truss.png',dpi=600)
        plt.show()

'''
pud=UnitPostProcess(1.8,1.4,3.4,3.2,1,1,1,0,5,0,0,8,8.0,48.6667)
pud.setfig()
pud.plot()
pud=UnitPostProcess(3.4,3.2,7.4,3.2,0,0,1,1,0,0,0,0,8.0,23.3333)
pud.plot()
pud.savefig()
'''