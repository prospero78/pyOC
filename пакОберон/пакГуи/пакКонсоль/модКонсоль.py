# coding: utf8
"""
Предоставляет тип консоли для служебной и отладочной печати.
"""

from tkinter import LabelFrame as тРамкаНадпись, Text as тТекст,\
		Scrollbar as тПолзунок

class тКонсоль(тРамкаНадпись):
	def __init__(сам, пОберон, пПредок):
		сам.__оберон = пОберон
		тРамкаНадпись.__init__(сам, пПредок, text = пОберон.рес.winMain['log'])
		сам.pack(side="bottom", expand=True, fill='x')

		ползунок = тПолзунок(сам)
		ползунок.pack(side='right', fill='y')

		цвет_фон = "#000"
		цвет_лит = "#EEE"
		сам.редЛог = тТекст(сам, relief='sunken', border=3, height=10,\
									background=цвет_фон, foreground=цвет_лит,\
									font="Consolas 11")
		сам.редЛог.pack(expand = True, fill = 'both')

		# первая привязка
		ползунок['command'] = сам.редЛог.yview
		# вторая привязка
		сам.редЛог['yscrollcommand'] = ползунок.set

		сам.редЛог.tag_config('_normal_', font=("Consolas", 11, "normal"), foreground="#FFF", \
				background="#000")

		сам.редЛог.tag_config('_head_', font=("Consolas", 11, "bold"), foreground="#FFF", \
				background="#00F")

	def Печать(сам, пСообщ:str)->None:
		if type(пСообщ) == str:
			сам.редЛог.insert("end", пСообщ+"\n", "_normal_")
		else:
			сам.Ошибка("тКонсоль.Печать(): пСообщ должен быть str, type="+str(type(пСообщ)))

	def Шапка_Печать(сам)->None:
		рес = сам.__оберон.рес

		сам.редЛог.insert('end', "\n         ", "_normal_")
		сам.редЛог.insert('end', "     " + рес.app['name']+"     ", "_head_")
		сам.редЛог.insert('end', "\n", "_normal_")

		сам.редЛог.insert('end', "         ", "_normal_")
		сам.редЛог.insert('end', " KBK Techniks ltd. 2018 BSD-2 ", "_head_")
		сам.редЛог.insert('end', "\n", "_normal_")

		сам.редЛог.insert('end', "         ", "_normal_")
		сам.редЛог.insert('end', " "+рес.app['date']+" "+рес.app['time']+" "+рес.app['build']+"  " +рес.app['build_num']+" ", "_head_")
		сам.редЛог.insert('end', "\n\n", "_normal_")
