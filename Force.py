import matplotlib.pyplot as plt

class Force:
    def __init__(self,a,b,fx,fy,l,ax):
        self.a=a
        self.b=b
        self.fx=fx
        self.fy=fy
        self.l=l
        self.fc='green'
        self.ax=ax
        self.c1=0.4#width系数
        self.c2=1#headwidth系数
        self.c3=1#箭头头部长度系数
    def ForcePlot(self):
        d=1/7.5*self.l
        if self.fx>0:
            self.ax.annotate(str(self.fx), xy=(self.a,self.b), xytext=(self.a-1.6*d,self.b),arrowprops=dict(facecolor='r', shrink=0.005*self.l,width=self.c1*self.l,headwidth=self.c2*self.l,headlength=self.c3*self.l),zorder=800)
        elif self.fx<0:
            self.ax.annotate(str(self.fx), xy=(self.a,self.b), xytext=(self.a+1.6*d,self.b),arrowprops=dict(facecolor='r', shrink=0.005*self.l,width=self.c1*self.l,headwidth=self.c2*self.l,headlength=self.c3*self.l),zorder=800)    
        if self.fy>0:
            self.ax.annotate(str(self.fy), xy=(self.a,self.b), xytext=(self.a,self.b-d),arrowprops=dict(facecolor='r', shrink=0.005*self.l,width=self.c1*self.l,headwidth=self.c2*self.l,headlength=self.c3*self.l),zorder=800)
        elif self.fy<0:
            self.ax.annotate(str(self.fy), xy=(self.a,self.b), xytext=(self.a,self.b+d),arrowprops=dict(facecolor='r', shrink=0.005*self.l,width=self.c1*self.l,headwidth=self.c2*self.l,headlength=self.c3*self.l),zorder=800)
        plt.savefig('fig.png',dpi=600)