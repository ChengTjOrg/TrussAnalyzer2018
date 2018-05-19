# -*- coding: utf-8 -*-
"""
Created on Tue May 15 19:36:24 2018

@author: Nicole
"""

#post display

from __future__ import division
#import MyLine
#import PreUnitDisplay as pud
import Support
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib
#matplotlib.use('Agg')
#import matplotlib.lines as lines
#import matplotlib.transforms as mtransforms
#import matplotlib.text as mtext
import math
#from skimage import io,data


'''
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
        if len(x):
            self.text.set_position(((x[0]+x[1])/2-0.09, (y[0]+y[1])/2+0.08))#设置label位置
            #self.text.set_rotations(angle)#angle in degrees
            ''''''
            中点坐标在哪里计算——x,y是如何传过来的？
            angle在哪里计算,是如何传过来的？
            还要考虑注释数字的长度
            zorder应设为最高——在哪里设？
            ''''''
            k=(y[1]-y[0])/(x[1]-x[0])
            a=math.atan(k)/(2*math.pi)*360
            self.text.set_rotation(a)

        lines.Line2D.set_data(self, x, y)

    def draw(self, renderer):
        # draw my label at the end of the line with 2 pixel offset
        lines.Line2D.draw(self, renderer)
        self.text.draw(renderer)
        
    #def set_angle(self,x,y):
'''

        
class PostUnitDisplay:
    def __init__(self,a1,b1,a2,b2,s1,s2,l,tc,pc,sc,result):
        self.a1=a1
        self.b1=b1
        self.a2=a2
        self.b2=b2
        self.s1=s1
        self.s2=s2
        self.l=l
        self.tc=tc
        self.pc=pc
        self.sc=sc
        self.result=result
        self.x=[a1,a2]
        self.x=np.array(self.x)
        self.y=[b1,b2]
        self.y=np.array(self.y)
        self.c1=0.09
        self.c2=0.06
        self.c3=0.09
        self.c4=0.02
        self.c5=2.5#数字大小系数
    def display(self):
        #plt.figure()
        plt.figure(figsize=(self.l,self.l))
        plt.xlim(0,self.l)
        plt.ylim(0,self.l)
        #画两端结点
        x=[self.a1,self.a2]
        y=[self.b1,self.b2]
        plt.scatter(x,y,c='w',marker='o', s=60,edgecolors=self.pc,linewidths=3, zorder=100)#s是点大小
        #plt.savefig('C:\\文件\\大二下\\绗架结构分析助手\\图像\\后处理\\fig1.png',dpi=600)
        #画杆
        plt.plot(x,y,c=self.tc,linewidth=5,zorder=1)
        #plt.savefig('C:\\文件\\大二下\\绗架结构分析助手\\图像\\后处理\\fig2.png',dpi=600)
        #画支座
        sp1=Support.Support(self.s1,self.a1,self.b1,self.l,self.sc)
        sp1.display()
        sp2=Support.Support(self.s2,self.a2,self.b2,self.l,self.sc)
        sp2.display()
        #plt.savefig('C:\\文件\\大二下\\绗架结构分析助手\\图像\\后处理\\fig3.png',dpi=600)
        #标数据
        l1 = np.array([self.a1,self.b1])
        l2 = np.array([self.a2,self.b2])
        ## Rotate angle
        #trans_angle = plt.gca().transData.transform_angles(np.array((45,)),l2.reshape((1, 2)))[0]
        if self.a1==self.a2:
            if self.b1>self.b2:
                angle=-90
            else:
                angle=90
        else:
            angle=math.atan((self.b2-self.b1)/(self.a2-self.a1))/(2*math.pi)*360
        #将[-90,90]的角变为[0,90]
        if self.b2-self.b1>=0 and self.a2-self.a1>=0:
            trans_angle=angle
            plt.text((l1[0]+l2[0])/2-self.c1*self.l*math.cos(trans_angle)-self.c2*self.l*math.sin(trans_angle),
                 (l1[1]+l2[1])/2-self.c3*self.l*math.sin(trans_angle)+self.c4*self.l*math.cos(trans_angle),
                 str(self.result),fontsize=self.c5*self.l,rotation=angle, rotation_mode='anchor',zorder=1000)
        elif self.b2-self.b1>=0 and self.a2-self.a1<0:
            trans_angle=-angle
            plt.text((l1[0]+l2[0])/2-self.c1*self.l*math.cos(trans_angle)+self.c2*self.l*math.sin(trans_angle),
                 (l1[1]+l2[1])/2+self.c3*self.l*math.sin(trans_angle)+self.c4*self.l*math.cos(trans_angle),
                 str(self.result),fontsize=self.c5*self.l,rotation=angle, rotation_mode='anchor',zorder=1000)
        elif self.b2-self.b1<0 and self.a2-self.a1<=0:
            trans_angle=angle
            plt.text((l1[0]+l2[0])/2-self.c1*self.l*math.cos(trans_angle)-self.c2*self.l*math.sin(trans_angle),
                 (l1[1]+l2[1])/2-self.c3*self.l*math.sin(trans_angle)+self.c4*self.l*math.cos(trans_angle),
                 str(self.result),fontsize=self.c5*self.l,rotation=angle, rotation_mode='anchor',zorder=1000)
        elif self.b2-self.b1<0 and self.a2-self.a1>=0:
            trans_angle=-angle
            plt.text((l1[0]+l2[0])/2-self.c1*self.l*math.cos(trans_angle)+self.c2*self.l*math.sin(trans_angle),
                 (l1[1]+l2[1])/2+self.c3*self.l*math.sin(trans_angle)+self.c4*self.l*math.cos(trans_angle),
                 str(self.result),fontsize=self.c5*self.l,rotation=angle, rotation_mode='anchor',zorder=1000)
        '''trans_angle = plt.gca().transData.transform_angles(np.array((45,)),
                                                   l2.reshape((1, 2)))[0]'''
        ## Plot text
        '''
        plt.text((l1[0]+l2[0])/2-0.1*self.l*math.cos(trans_angle),(l1[1]+l2[1])/2+0.04*self.l*math.sin(trans_angle),
                 str(self.result),fontsize=self.c1*self.l,rotation=trans_angle, rotation_mode='anchor',zorder=1000)
        '''
        '''
        plt.text((l1[0]+l2[0])/2-0.16*self.l*abs(math.cos(trans_angle))+0.04*self.l*abs(math.sin(trans_angle)),
                 (l1[1]+l2[1])/2+0.03*self.l*abs(math.sin(trans_angle))+0.02*self.l*abs(math.cos(trans_angle)),
                 str(self.result),fontsize=self.c1*self.l,rotation=trans_angle, rotation_mode='anchor',zorder=1000)'''
        #plt.tight_layout()
        plt.savefig('C:\\文件\\大二下\\绗架结构分析助手\\图像\\后处理\\fig4.png',dpi=600)
        plt.show()
        '''
        img=data.chelsea()
        io.imshow(img)
        io.imsave('C:\\文件\\大二下\\绗架结构分析助手\\图像\\后处理\\fig2.png',img)'''


pud=PostUnitDisplay(1.8,1.4,6.8,6.4,3,1,8.0,'k','k','b',48.6667)
pud.display()



'''
fig,ax = plt.subplots()
x=[.4,.8]
y=[.18,.12]
x=np.array(x)
y=np.array(y)
result=12.3456

line = MyLine(x, y, mfc='red', ms=12, label=str(result),linewidth=0,zorder=1)
#line.text.set_text('line label')
line.text.set_color('red')
line.text.set_fontsize(16)


ax.add_line(line)


plt.show()
'''

