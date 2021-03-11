# -*- coding: utf-8 -*-
"""
Created on Tue May 26 12:36:30 2020

@author: Janek
"""
import matplotlib.pyplot as plt
from openpyxl import load_workbook
import numpy as np
def Initialize():
    global checkerboard
    L=10*np.random.rand(201)
    L=np.floor(L)
    L=np.mod(L,2)
    L=np.array(list(L), dtype=int)
    checkerboard=L
    for i in range(200):
        L=10*np.random.rand(201)
        L=np.floor(L)
        L=np.mod(L,2)
        L=np.array(list(L), dtype=int)
        checkerboard=np.vstack((checkerboard,L))

def neighbourhood():
    global a0,a1,a2,a3,a4,a5,a6,a7,a8
    a0=np.roll(np.roll(checkerboard,-1,axis=0),-1,axis=1)#
    a1=np.roll(np.roll(checkerboard,-1,axis=0),0,axis=1)#
    a2=np.roll(np.roll(checkerboard,-1,axis=0),1,axis=1)#
    a3=np.roll(np.roll(checkerboard,0,axis=0),-1,axis=1)#
    a4=checkerboard
    a5=np.roll(np.roll(checkerboard,0,axis=0),1,axis=1)#
    a6=np.roll(np.roll(checkerboard,1,axis=0),-1,axis=1)#
    a7=np.roll(np.roll(checkerboard,1,axis=0),0,axis=1)#
    a8=np.roll(np.roll(checkerboard,1,axis=0),1,axis=1)#
def score(A,B):
    return(np.multiply(A,B)+np.multiply((1-A),B)*b)
def evaluation():
    global scoreboard, s0,s1,s2,s3,s4,s5,s6,s7,s8
    scoreboard = score(a4,a0) + score(a4,a1) + score(a4,a2) + score(a4,a3) +score(a4,a4)+ score(a4,a5) + score(a4,a6) + score(a4,a7) + score(a4,a8)
    s0=np.roll(np.roll(scoreboard,-1,axis=0),-1,axis=1)#
    s1=np.roll(np.roll(scoreboard,-1,axis=0),0,axis=1)#
    s2=np.roll(np.roll(scoreboard,-1,axis=0),1,axis=1)#
    s3=np.roll(np.roll(scoreboard,0,axis=0),-1,axis=1)#
    s4=scoreboard
    s5=np.roll(np.roll(scoreboard,0,axis=0),1,axis=1)#
    s6=np.roll(np.roll(scoreboard,1,axis=0),-1,axis=1)#
    s7=np.roll(np.roll(scoreboard,1,axis=0),0,axis=1)#
    s8=np.roll(np.roll(scoreboard,1,axis=0),1,axis=1)#
def best_score():
    global checkerboardnext
    for i in range(201):
        for j in range(201):
            best=0
            if s0[i][j]>=best:
                best=s0[i][j]
                checkerboardnext[i][j]=a0[i][j]
            if s1[i][j]>=best:
                best=s1[i][j]
                checkerboardnext[i][j]=a1[i][j]
            if s2[i][j]>=best:
                best=s2[i][j]
                checkerboardnext[i][j]=a2[i][j]
            if s3[i][j]>=best:
                best=s3[i][j]
                checkerboardnext[i][j]=a3[i][j]

            if s5[i][j]>=best:
                best=s5[i][j]
                checkerboardnext[i][j]=a5[i][j]
            if s6[i][j]>=best:
                best=s6[i][j]
                checkerboardnext[i][j]=a6[i][j]
            if s7[i][j]>=best:
                best=s7[i][j]
                checkerboardnext[i][j]=a7[i][j]
            if s8[i][j]>=best:
                best=s8[i][j]
                checkerboardnext[i][j]=a8[i][j]
            if s4[i][j]>=best:
                best=s4[i][j]
                checkerboardnext[i][j]=a4[i][j]
def evolution():
    global checkerboard,checkerboardnext
    for p in range(120): 
        #print(p)
        T.append(p)
        C.append(np.sum(1-checkerboard)/201**2)
        neighbourhood()
        evaluation()
        best_score()
        checkerboard=checkerboardnext
C=[]
T=[]
Fract=[]
bparamiter=[] 
b=1.9
#checkerboard=np.zeros((201,201))+1
#checkerboard[100][100]=0    
B=np.arange(start=1.25,stop=2.25,step=0.05)
checkerboardnext=np.zeros((201,201))
for b in B:
    Initialize()
    evolution()
    tail=C[-20:]
    print("b: ",b ,"defector fraction: ",np.mean(tail))
    Fract.append(np.mean(tail))
    bparamiter.append(b)
    
plt.plot(bparamiter,Fract , color='black', linestyle='-', linewidth=1)

plt.xlabel('b', fontsize=14)
plt.ylabel('Fraction of defectors', fontsize=14)
plt.title('Evolution f(b)', fontsize=20)
plt.grid(True)
plt.savefig("final.png")