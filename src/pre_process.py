#!/usr/bin/env python

import numpy

def delrepeat(a):
    ll2=[]
    for i in a:
        if i not in ll2:
            ll2.append(i)
    return ll2

def preprocess():
    f = open('number.txt','r')
    number = numpy.loadtxt('number.txt') 
    f.close()

    myList = number[:,:3]
    myList2 = number[:,7:10]
    l = numpy.concatenate((myList,myList2),axis=0)

    l = delrepeat(l.tolist())
    l = numpy.array(l)

    idex=numpy.lexsort([l[:,2], l[:,1], l[:,0]])
    l = l[idex, :]

    [a,b]= l.shape
    for i in range(0,a):
        l[i][0]=i+1

    [c,d]= number.shape
    for i in range(0,c):
        for j in range(0,a):
            if number[i][1] == l[j][1] and number[i][2] == l[j][2]:
                number[i][0] = l [j][0]
            if number[i][8] == l[j][1] and number[i][9] == l[j][2]:
                number[i][7] = l [j][0]

    number = number.tolist()

    numpy.savetxt("temp.txt", number)
