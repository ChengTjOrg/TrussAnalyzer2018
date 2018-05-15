# -*- coding: utf-8 -*-
"""
Created on Tue May 15 22:00:20 2018

@author: Nicole
"""

#import numpy as np
#import matplotlib.pyplot as plt
import matplotlib.text as mtext
import matplotlib.lines as lines
import matplotlib.transforms as mtransforms
import math


class MyLine(lines.Line2D):
    def __init__(self, *args, **kwargs):
        # we'll update the position when the line data is set
        self.text = mtext.Text(0, 0, '')
        lines.Line2D.__init__(self, *args, **kwargs)

        # we can't access the label attr until *after* the line is
        # inited
        self.text.set_text(self.get_label())

    def set_figure(self, figure):
        self.text.set_figure(figure)
        lines.Line2D.set_figure(self, figure)

    def set_axes(self, axes):
        self.text.set_axes(axes)
        lines.Line2D.set_axes(self, axes)

    def set_transform(self, transform):
        # 2 pixel offset
        texttrans = transform + mtransforms.Affine2D().translate(2, 2)
        self.text.set_transform(texttrans)
        lines.Line2D.set_transform(self, transform)

    def set_data(self, x, y):
        global l
        if len(x):
            self.text.set_position(((x[0]+x[1])/2-0.09*l, (y[0]+y[1])/2+0.08*l))#设置label位置
            #self.text.set_rotations(angle)#angle in degrees
            '''
            中点坐标在哪里计算——x,y是如何传过来的？
            angle在哪里计算,是如何传过来的？
            还要考虑注释数字的长度
            zorder应设为最高——在哪里设？
            '''
            k=(y[1]-y[0])/(x[1]-x[0])
            a=math.atan(k)/(2*math.pi)*360
            self.text.set_rotation(a)

        lines.Line2D.set_data(self, x, y)

    def draw(self, renderer):
        # draw my label at the end of the line with 2 pixel offset
        lines.Line2D.draw(self, renderer)
        self.text.draw(renderer)