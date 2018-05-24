# -*- coding: utf-8 -*-
"""
Created on Tue May 22 16:06:49 2018

@author: Nicole
"""


import Calculated
import Uncalculated

def CalculatedPostProcess(path):
    data=Calculated.Calculated(path)
    data.SetFig()
    data.CalculatedLoadData()
    data.CalculatedPlot()
    data.CalculatedSaveFig()

def UncalculatedPostProcess(path):
    data=Uncalculated.Uncalculated(path)
    data.SetFig()
    data.UncalculatedLoadData()
    data.UncalculatedPlot()
    data.UncalculatedSaveFig()