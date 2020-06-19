# -*- coding: utf-8 -*-
"""
Created on Thu May 14 06:55:06 2020
@author: lcovarrubias, eledgarmurillo

"""
# TEST Variance
import pylab as pylab
import numpy as numpy
import minoritymodel as minmod

fig = pylab.figure(1,figsize=(6,4))

for n in range(5):
    sim = minmod.System(T=1000,N=101, m=3,s=2)
    sim.run()
    pylab.plot(sim.Prices)

pylab.xlabel(r'$t$')
pylab.ylabel(r'$Prices$')
fig.set_tight_layout(True)
pylab.savefig('figs/test/prices.png', format='png',bbox_inches='tight')

fig.clf()
N = 101
syms = ['ro-','gs-','bd-']
s = [2, 4, 6]
for i in range(len(s)):
    Y = []
    X = []
    for m in range(1,15):
        x = []
        y = []
        for t in range(10):
            sim = minmod.System(T=200,N=N, m=m,s=s[i])
            sim.run()
            x.append(float(2**m)/float(N))
            y.append(numpy.var(sim.D)/float(N))
        X.append(numpy.mean(x))
        Y.append(numpy.mean(y))
        print('m='+str(m))
    pylab.plot(X,Y,syms[i],label='s='+str(s[i]))
    print('s='+str(s[i]))

pylab.xscale('log')
pylab.yscale('log')
pylab.xlabel(r'$2^{m}/N$')
pylab.ylabel(r'$\sigma^2/N$')
pylab.legend(loc='best')
fig.set_tight_layout(True)
pylab.savefig('figs/test/variance-vs-m.png', format='png',bbox_inches='tight')

fig.clf()

X = []
Y = []
N = 101
for m in range(1,10):
    x = []
    y = []
    for t in range(10):
        sim = minmod.System(T=200,N=N, m=m)
        sim.run()
        x.append(float(2**m)/float(N))
        y.append(numpy.mean(sim.SuccessRates))
    X.append(numpy.mean(x))
    Y.append(numpy.mean(y))
    print('m='+str(m))

pylab.plot(X,Y,'o-')
pylab.xscale('log')
pylab.xlabel(r'$2^{m}/N$')
pylab.ylabel(r'$success\ rate$')
pylab.savefig('figs/test/success_rate-vs-m.png', format='png',bbox_inches='tight')
pylab.close(fig)