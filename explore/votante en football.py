#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import sys,os,json
from collections import Counter

sys.path.insert(1, '/home/chacoma/librerias/python')
from plotter_lib import *

db = '/home/chacoma/Lineas/football_4/data/'

arx1 =db+'Sample_Game_1/X_DS1_raw.json' 
arx2 =db+'Sample_Game_2/X_DS2_raw.json' 
arx3 =db+'Sample_Game_3/X_DS3_raw.json' 


# In[85]:


arxk = db+"kappas/k1.dat"

kappa = np.loadtxt(arxk, usecols=[1])

l1 = np.nanmean(kappa)-np.nanstd(kappa)
l2 = np.nanmean(kappa)+np.nanstd(kappa)

kmax =max(kappa)


# In[4]:


d = json.load(open(arx1,'r'))

T = len(d["2"])

X1= np.array(d["1"])
X2= np.array(d["2"])

print (T, X1.shape, X2.shape )

del d



#get_ipython().run_line_magic('matplotlib', 'notebook')


fig, ax = plt.subplots( 3,1, figsize=(8,6) )


ps = []

# equipo 1
for i in range(11):
    pi, = ax[0].plot([], [], linewidth=1, c="C0")
    ps.append(pi)

# equipo2
for i in range(11):
    pi, = ax[0].plot([], [], linewidth=1, c="C1")
    ps.append(pi)
    
ax[0].set_xlim(-5,110)
ax[0].set_ylim(-5,75)



#kappa ---------------------------------------------
pi, = ax[1].plot([], [], linewidth=1, c="C3")
ps.append(pi)

pi, = ax[2].plot([], [], linewidth=1, c="C3")
ps.append(pi)


print (len(ps))

tiempo = np.arange(0, len(kappa), 1)

ax[1].axhline(l1, color='green', lw=2, alpha=0.5)
ax[1].axhline(l2, color='green', lw=2, alpha=0.5)

ax[1].set_xlim(0,None)
ax[1].set_ylim(0,kmax)

ax[1].set_xlabel("Time")
ax[1].set_ylabel("v")

# --------------------------------------------------



ax[2].set_xlim(0,None)
ax[2].set_ylim(0,kmax)

def init():

    for i in range(23):
        ps[i].set_data([], [])

    return ps



def animate(i):


	x1= X1[i]
	dx1 = X1[i+1]-x1

	x2= X2[i]
	dx2 = X2[i+1]-x2

	for j in range(11):

		ps[j].set_data( [ x1[j,0],x1[j,0]+dx1[j,0] ], [ x1[j,1],x1[j,1]+dx1[j,1]  ] )
		
		ps[j+11].set_data( [ x2[j,0],x2[j,0]+dx2[j,0] ], [ x2[j,1],x2[j,1]+dx2[j,1]  ] )


	ps[22].set_data( tiempo[i-10:i], kappa[i-10:i] )
	ax[1].set_xlim(i-10,i+10)

	ps[23].set_data( tiempo[i-10:i], kappa[i-10:i] )
	ax[2].set_xlim(i-10,i+10)


	return ps



anim = FuncAnimation(fig, animate, init_func=init,
                               frames=(100), interval=200, blit=True)
#anim.save("test1.gif")
plt.show()





