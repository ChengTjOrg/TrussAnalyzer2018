#!/usr/bin/env python
"""
@author: 2Fzzzzz
"""

import numpy

def delrepeat(a):   #删除重复节点
    ll2=[]
    for i in a:
        if i not in ll2:
            ll2.append(i)
    return ll2

def preprocess():    #主程序
    number = numpy.loadtxt('temp.txt')       #载入数据
    
    myList = number[:,:3]
    myList2 = number[:,7:10]
    l = numpy.concatenate((myList,myList2),axis=0)     #读取所有节点

    l = delrepeat(l.tolist())
    l = numpy.array(l)     #删除多余节点

    idex=numpy.lexsort([l[:,2], l[:,1], l[:,0]])
    l = l[idex, :]        #节点排序

    [a,b]= l.shape
    for i in range(0,a):
        l[i][0]=i+1       #节点编号
    
    [c,d]= number.shape
    for i in range(0,c):
        for j in range(0,a):
            if number[i][1] == l[j][1] and number[i][2] == l[j][2]:
                number[i][0] = l [j][0]
            if number[i][8] == l[j][1] and number[i][9] == l[j][2]:
                number[i][7] = l [j][0]      #节点编号返回到原数据

    numpy.savetxt("temp.txt", number, fmt='%f', delimiter=' ',newline='\r\n')     #保存文件