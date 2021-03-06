# coding: utf8
"""
Предоставляет тип консоли для служебной и отладочной печати.
"""

import sys
from tkinter import LabelFrame as тРамкаНадпись, Text as тТекст,\
		Scrollbar as тПолзунок

from пакОберон.пакКомпилятор.пакСущность.пакОшибка import тОшибка

class тКонсоль(тРамкаНадпись):
	def __init__(сам, пОберон, пПредок, пОтладка):
		сам.__оберон = пОберон
		сам.__бОтладка = пОтладка
		# устанавлявает состояние ошибки исходник
		# внутренняя ошибка компилятора
		тРамкаНадпись.__init__(сам, пПредок, text = пОберон.рес.winMain['log'])
		сам.pack(side="bottom", fill='x')

		ползунок = тПолзунок(сам)
		ползунок.pack(side='right', fill='y')

		цвет_фон = "#000"
		цвет_лит = "#EEE"
		сам.редЛог = тТекст(сам, relief='sunken', border=3, height=20,\
									background=цвет_фон, foreground=цвет_лит,\
									font="Consolas 11")
		сам.редЛог.pack(expand = True, fill = 'both')

		# первая привязка
		ползунок['command'] = сам.редЛог.yview
		# вторая привязка
		сам.редЛог['yscrollcommand'] = ползунок.set

		сам.редЛог.tag_config('_normal_', font=("Consolas", 11, "normal"), \
				foreground="#FFF", background="#000")

		сам.редЛог.tag_config('_head_', font=("Consolas", 11, "bold"), foreground="#FFF", \
				background="#00F")

		сам.редЛог.tag_config('_source_', font=("Consolas", 11, ), foreground="#0F0", \
				background="#000")

		сам.редЛог.tag_config('_error_', font=("Consolas", 11, ), foreground="#FB0", \
				background="#404")

		сам.редЛог.tag_config('_errin_', font=("Consolas", 11, "italic"), foreground="#FF0", \
				background="#800")

		сам.редЛог.tag_config('_debug_', font=("Consolas", 11, ), foreground="#666", \
				background="#000")

	@property
	def бОтладка(сам)->bool:
		return сам.__бОтладка

	def Проверить(сам, пбУсл:bool, пСообщ:str)->None:
		if type(пбУсл) != bool:
			сам.ОшВнутр("тКонсоль.Проверить(): ошибка компилятора. пбУсл должен быть bool, type="+ \
					str(type(пбУсл)))
			if type(пОшибка) != str:
				сам.Ошибка("тКонсоль.Проверить(): ошибка компилятора. пСообщ должен быть str, type="+ \
						str(type(пСообщ)))
		if not пбУсл:
			сам.Ошибка(пСообщ)

	def Ошибка(сам, пОшибка:str)->None:
		if type(пОшибка) != str:
			сам.ОшВнутр("Консоль.Ошибка(): ошибка компилятора. пОшибка должен быть str, type="+str(type(пОшибка)))
			return
		сам.редЛог.insert("end", пОшибка, "_error_")
		сам.редЛог.insert('end', " \n\n", "_normal_")

	def ОшВнутр(сам, пОшибка:str)->None:
		if type(пОшибка) != str:
			сам.редЛог.insert("end", "тКонсоль.ОшВнутр(): пСообщ должен быть str, type="+str(type(пСообщ)), "_errin_")
			сам.редЛог.insert('end', " \n", "_normal_")
			return
		сам.редЛог.insert("end", пОшибка, "_errin_")
		сам.редЛог.insert('end', " \n", "_normal_")

	def Печать(сам, пСообщ:str)->None:
		if type(пСообщ) != str:
			сам.ОшВнутр("тКонсоль.Печать(): ошибка компилятора. пСообщ должен быть str, type="+str(type(пСообщ)))
			return
		сам.редЛог.insert("end", пСообщ, "_normal_")
		сам.редЛог.insert('end', "\n", "_normal_")

	def Отладить(сам, пСообщ:str)->None:
		if type(пСообщ) != str:
			сам.ОшВнутр("тКонсоль.Печать(): ошибка компилятора. пСообщ должен быть str, type="+str(type(пСообщ)))
			return
		if сам.бОтладка:
			сам.редЛог.insert("end", пСообщ, "_debug_")
			сам.редЛог.insert('end', "\n", "_normal_")

	def Исх_Печать(сам, пСообщ:str)->None:
		if type(пСообщ) != str:
			сам.Ошибка("тКонсоль.Исх_Печать(): ошибка компилятора. пСообщ должен быть str, type="+\
					str(type(пСообщ)))
			return
		сам.редЛог.insert("end", пСообщ+"\n", "_source_")
		сам.редЛог.insert('end', "\n", "_normal_")

	def Шапка_Печать(сам)->None:
		рес = сам.__оберон.рес

		сам.редЛог.insert('end', "\n         ", "_normal_")
		сам.редЛог.insert('end', "     " + рес.app['name']+"      ", "_head_")
		сам.редЛог.insert('end', "\n", "_normal_")

		сам.редЛог.insert('end', "         ", "_normal_")
		сам.редЛог.insert('end', " KBK Techniks ltd. 2018  BSD-2 ", "_head_")
		сам.редЛог.insert('end', "\n", "_normal_")

		сам.редЛог.insert('end', "         ", "_normal_")
		сам.редЛог.insert('end', " "+рес.app['date']+" "+рес.app['time']+" "+рес.app['build']+"  " +рес.app['build_num']+" ", "_head_")
		сам.редЛог.insert('end', "\n\n", "_normal_")

	def Очистить(сам):
		сам.редЛог.delete('1.0','end')
