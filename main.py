#!/usr/bin/env python3
# coding: utf8
'''
Пробуем сделать генератор AST для Оберона-07
from numba import jit
@jit(nogil=True, cache=True)
'''

from пакОберон import тОберон

def Выполнить():
	"""
	Запускает весь процесс.
	"""
	ос = тОберон()
	ос.Старт()

if __name__ == '__main__':
	Выполнить()
