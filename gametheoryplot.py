# -*- coding: utf-8 -*-
"""
Created on Tue May 26 17:19:43 2020

@author: Janek
"""
import matplotlib.pyplot as plt
T=[1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.1,2.2,1.25,1.35,1.45,1.55,1.65,1.75,1.85,1.95,2.05,2.15]
S=[0.01,0.1068325,0.084355,0.52883625,0.56792625,0.53032,0.7560875,0.75722625,1.010025,1.010025,1.010025,0.04619625,0.09225875,0.0850775,0.5334,0.56297375,0.53793,0.75566375,0.765195,1.010025,1.010025]
plt.scatter(T, S, color='black')
# plots with a red line
plt.xlabel('b ', fontsize=14)
plt.ylabel('Fraction of players', fontsize=14)
plt.title('Evolution of the fraction of defectors \n in the pupulation', fontsize=20)
plt.grid(True)
#plt.savefig("Entropy1.png")