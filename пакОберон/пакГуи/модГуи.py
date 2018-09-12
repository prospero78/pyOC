# coding: utf8
"""
Предоставляет класс графики для компилятора Оберона.
"""

from .пакОкнГлав import тОкнГлав
from .пакОкноСправка import тОкноСправка

class тГуи:
	def __init__(сам, пОберон)->None:
		сам.окнГлав = тОкнГлав(пОберон)
		сам.консоль = сам.окнГлав.консоль
		сам.окнСправка = тОкноСправка(пОберон)

	def Пуск(сам)->None:
		сам.окнГлав.Пуск()
