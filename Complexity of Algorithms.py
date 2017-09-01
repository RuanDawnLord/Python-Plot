# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 16:37:38 2017

@author: xzr0001
"""
import pylab
import numpy

x = numpy.linspace(1,100,1000) # 100 linearly spaced numbers

pylab.ylim([1,60])
pylab.xlim([1,20])


pylab.plot(x, numpy.log2(x), label='log2(N)')
pylab.plot(x, numpy.multiply(x,numpy.log2(x)), label='Nlog2(N)')
pylab.plot(x, x, label='N')
pylab.plot(x, numpy.square(x), label='N^2')
pylab.plot(x, numpy.power(x, 3), label='N^3')
pylab.plot(x, numpy.power(2, x), label='2^N')

pylab.legend(loc='upper right')
pylab.title("Algorithm Complexity on N")
pylab.show()