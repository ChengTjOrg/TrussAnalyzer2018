import numpy as np
import matplotlib.pyplot as plt
import UnitPostProcess

class PostProcess:
    def __init__(self,l):
        self.l=l
    def loadtruss(self):
        (a1,b1,sx1,sy1,fx1,fy1,a2,b2,sx2,sy2,fx2,fy2,fn,dx1,dy1,dx2,dy2)=np.loadtxt('C:\\文件\\大二下\\绗架结构分析助手\\输出.txt',skiprows=0,delimiter=' ',dtype=float,usecols=(1,2,3,4,5,6,8,9,10,11,12,13,15,16,17,18,19),unpack=True)
        self.x1=list(a1+dx1)
        self.y1=list(b1+dy1)
        self.x2=list(a2+dx2)
        self.y2=list(b2+dy2)
        self.sx1=list(sx1)
        self.sy1=list(sy1)
        self.sx2=list(sx2)
        self.sy2=list(sy2)
        self.fx1=list(fx1)
        self.fy1=list(fy1)
        self.fx2=list(fx2)
        self.fy2=list(fy2)
        self.fn=list(fn)
    def setfig(self):
        plt.figure(figsize=(self.l,self.l))
        plt.xlim(-1,self.l)
        plt.ylim(-1,self.l)
    def plot(self):
        for i in range(len(self.x1)):
            upp=UnitPostProcess.UnitPostProcess(self.x1[i],self.y1[i],self.x2[i],self.y2[i],self.sx1[i],self.sy1[i],self.sx2[i],self.sy2[i],self.fx1[i],self.fy1[i],self.fx2[i],self.fy2[i],self.l,self.fn[i])
            upp.plot()
    def savefig(self):
        plt.savefig('fig.png',dpi=600)
