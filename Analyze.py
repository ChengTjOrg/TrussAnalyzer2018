# -*- coding: utf-8 -*-
"""
Created on Tue May 22 16:06:49 2018

@author: Nicole
"""


import PostProcess

def fig():
    data=PostProcess.PostProcess(6)
    data.loadtruss()
    data.setfig()
    data.plot()
    data.savefig()
'''    
def fig2():
    data=PostProcess.postProcess(6)
    data.loadtruss2()
    data.setfig()
    data.plot2()
    data.savefig()
'''
    
fig()