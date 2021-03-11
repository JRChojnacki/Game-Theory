# -*- coding: utf-8 -*-
"""
Created on Sat May 23 14:55:20 2020

@author: Janek
"""
import imageio
import numpy as np
from PIL import Image, ImageDraw 
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
def display():
    global checkerboard,checkerboardnext
    
    for p in range(200):
        checkerboard0=np.copy(checkerboard)
        print(p)
        neighbourhood()
        evaluation()
        best_score()
        img = Image.new("RGB",(201,201),(255,255,255))
        draw = ImageDraw.Draw(img)
        for y in range(201):
            for x in range(201):
                if checkerboard0[y][x] and checkerboardnext[y][x]:
                    draw.point((y,x),fill=(255,255,255))
                if (not checkerboard0[y][x]) and checkerboardnext[y][x]:
                    draw.point((y,x),fill=(0,0,255))
                if (checkerboard0[y][x]) and (not checkerboardnext[y][x]):
                    draw.point((y,x),fill=(255,0,0))
                if (not checkerboard0[y][x]) and (not checkerboardnext[y][x]):
                    draw.point((y,x),fill=(0,0,0))
        checkerboard=checkerboardnext
        img.save('test{}.png'.format(p),"PNG")
        filenames2.append('test{}.png'.format(p))
b=2.1
checkerboard=np.zeros((201,201))+1
checkerboard[100][100]=0    
checkerboardnext=np.zeros((201,201))

filenames2=[]
images2=[]
display()
for filename in filenames2:
    images2.append(imageio.imread(filename))
imageio.mimsave('C:/Users/Janek/Desktop/ComputerModeling/GameTheory/b21.gif', images2)
#for i in range(3):
#    neighbourhood()
#    evaluation()
#    best_score()
#    checkerboard=checkerboardnext