# coding: utf8
"""
Этот тест для проверки аннотаций в питон 3.7
Якобы, ускоряет до невозможности))
========================
С использованием "from __future__ import annotations"
fib numba 0.180006742477417 s
fib numba 0.0 s
fib numba 0.0 s
fib CPython3.7 88.17543029785156 s
fib CPython3.7 88.3654260635376 s
fib CPython3.7 87.42534399032593 s
fib Anot3.7 88.51550817489624 s
fib Anot3.7 88.41537475585938 s
fib Anot3.7 88.13545227050781 s
===================================
Без использования "from __future__ import annotations"
ОДНАКО!!!
Этот код работает даже немного быстрей!!!
Короче, использовать нумбу, и достаточно))
"""

#from __future__ import annotations

from numba.decorators import jit
from time import time
from math import sqrt, sin, cos

@jit
def fibn(num=1):
	i = 0
	i1 = 0.01
	while True:
		var0 = i1 * 1000.0 / sqrt(i1) + (i1 * 0.123)
		var0 = sin(var0) + cos(var0)
		i += 1
		if i>=num:
			break
	i1 += 0.01

def fibp(num=1):
	i = 0
	i1 = 0.01
	while True:
		var0 = i1 * 1000.0 / sqrt(i1) + (i1 * 0.123)
		var0 = sin(var0) + cos(var0)
		i += 1
		if i>=num:
			break
	i1 += 0.01

def fiba(num:int = 1)->None:
	i:int = 0
	i1:float = 0.01
	var0:float
	while True:
		var0 = i1 * 1000.0 / sqrt(i1) + (i1 * 0.123)
		var0 = sin(var0) + cos(var0)
		i += 1
		if i>=num:
			break
	i1 += 0.01

def FrNumba(var2):
	time2_beg = time()
	fibn(var2)
	time2_end = time()
	time2 = time2_end - time2_beg
	print ("fib numba", time2, 's')

def FrPython(var2):
	time2_beg = time()
	fibp(var2)
	time2_end = time()
	time2 = time2_end - time2_beg
	print ("fib CPython3.7", time2*10, 's')

def FrAnot(var2:int)->None:
	time2_beg:float = time()
	fiba(var2)
	time2_end:float = time()
	time2:float = time2_end - time2_beg
	print ("fib Anot3.7", time2*10, 's')

if __name__ == '__main__':
	for i in range(3):
		FrNumba (100000000)
	for i in range(3):
		FrPython(10000000)
	for i in range(3):
		FrAnot  (10000000)
	input()
