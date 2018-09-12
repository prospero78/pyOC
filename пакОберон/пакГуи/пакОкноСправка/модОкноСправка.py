# coding: utf8
"""
Модуль предоставляющий окно справочной системы
"""

from tkinter import Toplevel as тОкно

class тОкноСправка(тОкно):
	def __init__(сам, пОберон):
		тОкно.__init__(сам)
		сам.title("Справка по компилятору")
		сам.withdraw()

	def Показать(сам):
		сам.deiconify()
