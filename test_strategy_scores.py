# -*- coding: utf-8 -*-
"""
Created on Thu May 14 06:55:06 2020
@author: lcovarrubias, eledgarmurillo

"""
# TEST Strategy Scores
import pylab as pylab
import numpy as numpy
import minoritymodel as minmod

T = 200
s = 2
m = 7
N = 101
fig = pylab.figure(1,figsize=(8,4))
sim = minmod.System(T=1,N=N, m=m,s=s)
S = numpy.zeros([N,s,T])
for t in range(T):
    for i in range(N):
        u=sim.Users[i]
        for j in range(s):
            S[i,j,t] = u.Strategies[j].score
    sim.run()
S = S.reshape([N*s,T])
for i in range(N*s):
    pylab.plot(S[i,:])
pylab.xlabel(r'$t$')
pylab.ylabel(r'$strategy\ scores$')
fig.set_tight_layout(True)