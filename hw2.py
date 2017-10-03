# -*- coding: utf-8 -*-
"""

hw2 for Intro of CFD

"""


def func(x):
	f = x*x*x-5*x
	return f
	
def fst_exact(x):
	f = 3*x*x-5
	return f

def sec_exact(x):
	f = 6*x
	return f
	
def fst_forw(x, dx):
	f = (func(x+dx)-func(x))/dx
	return f
		
def fst_back(x, dx):
	f = (func(x)-func(x-dx))/dx	
	return f
	
def fst_cent(x, dx):
	f = (func(x+dx)-func(x-dx))/(2*dx)
	return f

def sec_forw(x, dx):
	f = (func(x+2*dx)-2*func(x+dx)+func(x))/(dx*dx)
	return f

def sec_back(x, dx):
	f = (func(x)-2*func(x-dx)+func(x-2*dx))/(dx*dx)
	return f

def sec_cent(x, dx):
	f = (func(x+dx)-2*func(x)+func(x-dx))/(dx*dx)
	return f

step = [0.00001, 0.0001, 0.001, 0.01, 0.1, 0.2, 0.3]
axis = [0.5, 1.5]

for x in axis:
	for dx in step:
		print "dy/dx  , forword , x = %.1f, step = %.5f, df/dx   = %.3f, error = %.8f" %(x, dx, fst_forw(x, dx),(fst_forw(x,dx)-fst_exact(x))/fst_exact(x))  
		print "dy/dx  , backword, x = %.1f, step = %.5f, df/dx   = %.3f, error = %.8f" %(x, dx, fst_back(x, dx),(fst_back(x,dx)-fst_exact(x))/fst_exact(x))
		print "dy/dx  , central , x = %.1f, step = %.5f, df/dx   = %.3f, error = %.8f" %(x, dx, fst_cent(x, dx),(fst_cent(x,dx)-fst_exact(x))/fst_exact(x))
		print "d2y/dx2, forword , x = %.1f, step = %.5f, d2f/dx2 = %.3f, error = %.8f" %(x, dx, sec_forw(x, dx),(sec_forw(x,dx)-sec_exact(x))/sec_exact(x))  
		print "d2y/dx2, backword, x = %.1f, step = %.5f, d2f/dx2 = %.3f, error = %.8f" %(x, dx, sec_back(x, dx),(sec_back(x,dx)-sec_exact(x))/sec_exact(x))
		print "d2y/dx2, central , x = %.1f, step = %.5f, d2f/dx2 = %.3f, error = %.8f" %(x, dx, sec_cent(x, dx),(sec_cent(x,dx)-sec_exact(x))/sec_exact(x))

		

