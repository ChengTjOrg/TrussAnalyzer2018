import math
import numpy as np
class Node:
    """
    编写结点类信息
    """
    def __init__(self,x=0,y=0,number=0,constraint_x=0,constraint_y=0,fx=0,fy=0):
       self.x=x
       self.y=y
       self.number=number
       self.constraint_x=(2*self.number-1)*(not constraint_x)
       self.constraint_y=(2*self.number)*(not constraint_y)            #	1 约束
       self.fx=fx
       self.fy=fy
       self.displacement=[0,0]
    def setconstraint(self,constraint_x,constraint_y):
       self.constraint_x=constraint_x
       self.constraint_y=constraint_y
    def setf(self,fx,fy):
       self.fx=fx
       self.fy=fy
    def setdisplacement(self,displacement_x,displacement_y):
        self.displacement=[displacement_x,displacement_y]

class Truss:
    """
    编写单元类信息
    """
    def __init__(self,node1,node2):
        self.node1=node1
        self.node2=node2
        self.EA=0
        self.length=0
        self.ke=None
        self.Ke=None
        self.FN=0
    def setEA(self,EA):
        self.EA=EA
    def SetNodes(self,node1,node2):
        self.node1=node1
        self.node2=node2
    def calculatelength(self):
        dx=self.node2.x-self.node1.x
        dy=self.node2.y-self.node1.y
        self.length=math.sqrt(dx*dx+dy*dy)
    def length(self):
       return self.length
    def EA(self):
       return self.EA
    def calculateKe(self,c):
        k0=np.mat([[1,0,-1,0],[0,0,0,0],[-1,0,1,0],[0,0,0,0]])
        if (self.node2.x-self.node1.x) ==0:
            sita=3.14159/2.0
        else:
            sita=math.atan((self.node2.y-self.node1.y)/(self.node2.x-self.node1.x))
        T=np.mat([[math.cos(sita),math.sin(sita),0,0],[-math.sin(sita),math.cos(sita),0,0],[0,0,math.cos(sita),math.sin(sita)],[0,0,-math.sin(sita),math.cos(sita)]])
        self.ke=T.T*k0*T
        self.ke=self.ke*self.EA/self.length
        Ke=np.zeros([c,c])
        for i in range(c):
            for j in range(c):
                if j==0:
                    if i==0:
                        Ke[2*self.node1.number-2,2*self.node1.number-2]+=self.ke[i,j]
                    elif i==1:
                        Ke[2*self.node1.number-1,2*self.node1.number-2]+=self.ke[i,j]
                    elif i==2:
                        Ke[2*self.node2.number-2,2*self.node1.number-2]+=self.ke[i,j]
                    elif i==3:
                        Ke[2*self.node2.number-1,2*self.node1.number-2]+=self.ke[i,j]
                if j==1:
                    if i==0:
                        Ke[2*self.node1.number-2,2*self.node1.number-1]+=self.ke[i,j]
                    elif i==1:
                        Ke[2*self.node1.number-1,2*self.node1.number-1]+=self.ke[i,j]
                    elif i==2:
                        Ke[2*self.node2.number-2,2*self.node1.number-1]+=self.ke[i,j]
                    elif i==3:
                        Ke[2*self.node2.number-1,2*self.node1.number-1]+=self.ke[i,j]
                if j==2:
                    if i==0:
                        Ke[2*self.node1.number-2,2*self.node2.number-2]+=self.ke[i,j]
                    elif i==1:
                        Ke[2*self.node1.number-1,2*self.node2.number-2]+=self.ke[i,j]
                    elif i==2:
                        Ke[2*self.node2.number-2,2*self.node2.number-2]+=self.ke[i,j]
                    elif i==3:
                        Ke[2*self.node2.number-1,2*self.node2.number-2]+=self.ke[i,j]
                if j==3:
                    if i==0:
                        Ke[2*self.node1.number-2,2*self.node2.number-1]+=self.ke[i,j]
                    elif i==1:
                        Ke[2*self.node1.number-1,2*self.node2.number-1]+=self.ke[i,j]
                    elif i==2:
                        Ke[2*self.node2.number-2,2*self.node2.number-1]+=self.ke[i,j]
                    elif i==3:
                        Ke[2*self.node2.number-1,2*self.node2.number-1]+=self.ke[i,j]
        self.Ke=Ke
    def calculateFN(self,F):
        if (self.node2.x-self.node1.x) ==0:
            sita=3.14159/2.0
        else:
            sita=math.atan((self.node2.y-self.node1.y)/(self.node2.x-self.node1.x))
        T=np.mat([[math.cos(sita),math.sin(sita),0,0],[-math.sin(sita),math.cos(sita),0,0],[0,0,math.cos(sita),math.sin(sita)],[0,0,-math.sin(sita),math.cos(sita)]])
        FN=T*F
        return FN[2][0]
    def setFN(self,FN):
        if self.node1.number<self.node2.number:
            self.FN=FN
        else:
            self.FN=-FN
        
def analyzer():
    data = np.loadtxt('temp.txt')#读取数据
    [h,l]=data.shape             #读取单元数

    x=np.matrix.tolist(data[:,0])#读取节点数
    y=np.matrix.tolist(data[:,7])
    a=int(np.max(x))
    b=int(np.max(y))
    if a>b:
        countnode=a
    else:
        countnode=b

    node_list=[]                 #节点列表赋值
    for i in range(countnode):
        for j in range(h):
            if (i+1)==data[j][0]:
                n=Node(int(data[j][1]),int(data[j][2]),int(data[j][0]),int(data[j][3]),int(data[j][4]),int(data[j][5]),int(data[j][6]))
                node_list.append(n)
                break
            if (i+1)==data[j][7]:
                n=Node(int(data[j][8]),int(data[j][9]),int(data[j][7]),int(data[j][10]),int(data[j][11]),int(data[j][12]),int(data[j][13]))
                node_list.append(n)
                break

    nodexy_list=[]#坐标情况
    constraint_list=[]#支座情况
    f_list=[]#受力情况
    
    for i in range(countnode):     #节点情况赋值
          nodexy_list.append(node_list[i].x)
          nodexy_list.append(node_list[i].y) 
          constraint_list.append(node_list[i].constraint_x)
          constraint_list.append(node_list[i].constraint_y)
          f_list.append(node_list[i].fx)
          f_list.append(node_list[i].fy)
      
    trussnode_list=[] #单元所含节点
    EA_list=[]        #单元EA
    for i in range(h): #单元情况赋值
        trussnode_list.append(int(data[int(i)][0]))
        trussnode_list.append(int(data[int(i)][7]))
        EA_list.append(int(data[i-1][14]))

    truss_list=[]   #单元列表
    c=len(nodexy_list)
    K=np.zeros([c,c])        #计算总刚度矩阵
    for i in range(h): 
        n1=node_list[trussnode_list[2*i]-1]
        n2=node_list[trussnode_list[2*i+1]-1]
        t=Truss(n1,n2)
        t.calculatelength()
        t.setEA(EA_list[i-1])
        t.calculateKe(c)
        truss_list.append(t)  
        K=K+truss_list[i].Ke

    displacement_list=constraint_list#方程组排序
    c1=displacement_list.count(0)
    c=len(displacement_list)
    f1_list=f_list
    k=K
    for i in range(c-1):
        min=displacement_list[i]
        m=i
        for j in range(i+1,c,1):
            if min>displacement_list[j]:
                min=displacement_list[j]
                m=j
        t=displacement_list[i]
        displacement_list[i]=displacement_list[m]
        displacement_list[m]=t
        t=f1_list[i]
        f1_list[i]=f1_list[m]
        f1_list[m]=t
        for w in range(c):
             t=k[i,w]
             k[i,w]=k[m,w]
             k[m,w]=t
   
    Ke0=np.zeros([c-c1,c-c1])#删去部分方程，建立方程组
    f0=np.zeros([c-c1,1])
    for i in range(c-c1):
        f0[i,0]=f1_list[i+c1]
        for j in range(c-c1):
            Ke0[i,j]=k[i+c1,j+c1]
    
    A=Ke0 #求解方程，得出位移
    B=f0
    r=np.linalg.solve(A,B)
    count=0
    for i in range(c):
        if displacement_list[i]!=0:
            displacement_list[i]=r[count,0]
            count=count+1

    for i in range(int(c/2)):
        node_list[i].setdisplacement(displacement_list[2*i],displacement_list[2*i+1]) 
    for i in range(h):#轴力位移赋值
        a=trussnode_list[2*i]
        b=trussnode_list[2*i+1]
        v=np.mat([[displacement_list[a*2-2],],[displacement_list[a*2-1],],[displacement_list[b*2-2],],[displacement_list[b*2-1]]])
        F=truss_list[i].ke*v
        truss_list[i].setFN(truss_list[i].calculateFN(F))

    solve_list=[] #得出结果，输出
    for i in range(h):
        s_list=[truss_list[i].node1.number,truss_list[i].node1.x,truss_list[i].node1.y,data[i][3],data[i][4],truss_list[i].node1.fx,truss_list[i].node1.fy,truss_list[i].node2.number,truss_list[i].node2.x,truss_list[i].node2.y,data[i][10],data[i][11],truss_list[i].node2.fx,truss_list[i].node2.fy,truss_list[i].EA,truss_list[i].FN,truss_list[i].node1.displacement[0],truss_list[i].node1.displacement[1],truss_list[i].node2.displacement[0],truss_list[i].node2.displacement[1]]
        solve_list.append(s_list)
    
    np.savetxt("answer.txt",solve_list, fmt='%f', delimiter=' ',newline='\r\n')
