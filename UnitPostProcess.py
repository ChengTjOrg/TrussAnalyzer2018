from __future__ import division
import Support
import numpy as np
import matplotlib.pyplot as plt
import math
        
class UnitPostProcess:
    def __init__(self,a1,b1,a2,b2,sx1,sy1,sx2,sy2,fx1,fy1,fx2,fy2,l,result):
        self.a1=a1
        self.b1=b1
        self.a2=a2
        self.b2=b2
        self.sx1=sx1
        self.sy1=sy1
        self.sx2=sx2
        self.sy2=sy2
        self.fx1=fx1
        self.fy1=fy1
        self.fx2=fx2
        self.fy2=fy2
        self.l=l
        self.tc='grey'
        self.pc='k'
        self.sc='b'
        self.result=result
        self.x=[a1,a2]
        self.x=np.array(self.x)
        self.y=[b1,b2]
        self.y=np.array(self.y)
        self.c1=0.09
        self.c2=0.06
        self.c3=0.09
        self.c4=0.02
        self.c5=1.8#数字大小系数
        self.c6=0.6#线宽系数
        self.c7=0.4#点圆圈线宽系数
        self.trusslength=math.sqrt((a2-a1)**2+(b2-b1)**2)
    def setfig(self):
        #plt.figure()
        plt.figure(figsize=(self.l,self.l))
        plt.xlim(0,self.l)
        plt.ylim(0,self.l)
    def plot(self):    
        #画两端结点
        x=[self.a1,self.a2]
        y=[self.b1,self.b2]
        plt.scatter(x,y,c='w',marker='o', s=10*self.l,edgecolors=self.pc,linewidths=self.c7*self.l, zorder=100)#s是点大小
        #画杆
        plt.plot(x,y,c=self.tc,linewidth=self.c6*self.l,zorder=1)
        #画支座
        sp1=Support.Support(self.sx1,self.sy1,self.a1,self.b1,self.l,self.sc)
        sp1.display()
        sp2=Support.Support(self.sx2,self.sy2,self.a2,self.b2,self.l,self.sc)
        sp2.display()
        #画力
        pass
        #标数据
        l1 = np.array([self.a1,self.b1])
        l2 = np.array([self.a2,self.b2])
        #计算角度
        if self.a1==self.a2:
            if self.b1>self.b2:
                angle=-90
            else:
                angle=90
        else:
            angle=math.atan((self.b2-self.b1)/(self.a2-self.a1))/(2*math.pi)*360
        plt.text((l1[0]+l2[0])/2,(l1[1]+l2[1])/2,str(self.result),fontsize=self.c5*self.l,rotation=angle,rotation_mode='anchor',zorder=1000)
        #plt.tight_layout()
    def savefig(self):
        #fig = plt.gcf()
        #fig.set_size_inches(20,20)
        plt.savefig('fig.png',dpi=600)
        plt.show()
