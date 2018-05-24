<<<<<<< HEAD:Final/PostProcess.py
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
=======
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
    
CalculatedPostProcess('输出.txt')
UncalculatedPostProcess('temp(6).txt')
>>>>>>> 8b97942996753b96dda6f542a9bd993f9d3cb72b:PostProcess/PostProcess.py
