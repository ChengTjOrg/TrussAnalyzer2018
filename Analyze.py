# -*- coding: utf-8 -*-
"""
Created on Tue May 22 01:46:50 2018

@author: Nicole
"""

import PostProcess

data=PostProcess.postProcess(6)
data.loadtruss()
data.setfig()
data.plot()
data.savefig()