import matplotlib.pyplot as plt

class Support:
    def __init__(self,sx,sy,a,b,l,sc):
        self.sx=int(sx)
        self.sy=int(sy)
        self.a=a
        self.b=b
        self.l=l
        self.c1=1/20#支座长短系数1
        self.c2=1/40#支座长短系数2（大地）
        self.c3=8#点大小系数
        self.sc=sc
    def none(self):
        pass
    def horizontal(self):
        #仅有水平支座，向左画
        x=[self.a,self.a-self.c1*self.l]
        y=[self.b,self.b]
        plt.scatter(x[1],y[1],c='w',marker='o',s=self.c3*self.l,edgecolors=self.sc,linewidths=2,zorder=100)
        plt.plot(x,y,c=self.sc,linewidth=2.5,zorder=1)
        x1=[self.a-self.c1*self.l,self.a-self.c1*self.l]
        y1=[self.b+self.c2*self.l,self.b-self.c2*self.l]
        plt.plot(x1,y1,c=self.sc,linewidth=2.5,zorder=1)
    def vertical(self):
        #仅有竖直支座，向下画
        x=[self.a,self.a]
        y=[self.b,self.b-self.c1*self.l]
        plt.scatter(x[1],y[1],c='w',marker='o',s=self.c3*self.l,edgecolors=self.sc,linewidths=2,zorder=100)
        plt.plot(x,y,c=self.sc,linewidth=2.5,zorder=1)
        x1=[self.a-self.c2*self.l,self.a+self.c2*self.l]
        y1=[self.b-self.c1*self.l,self.b-self.c1*self.l]
        plt.plot(x1,y1,c=self.sc,linewidth=2.5,zorder=1)
    def display(self):
        self.xswitcher={0:Support.none,1:Support.horizontal}
        self.xswitcher.get(self.sx)(self)
        self.yswitcher={0:Support.none,1:Support.vertical}
        self.yswitcher.get(self.sy)(self)
