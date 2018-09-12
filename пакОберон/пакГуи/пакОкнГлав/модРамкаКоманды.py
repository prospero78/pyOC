# coding: utf8
"""
Предоставляет рамку для инструментов. Содержит основные конпки.
"""

from tkinter import LabelFrame as тРамкаНадпись, Button as тКнопка

class тРамкаКоманды(тРамкаНадпись):
	def __init__(сам, root, master):
		сам.__root = root
		тРамкаНадпись.__init__(сам, master)
		сам.pack(side="top", expand=True, fill='x')

		шрифт = "Consolas 9"
		сам.кнпНовый = тКнопка(сам, text=" \u271a ", font=шрифт)
		сам.кнпНовый.pack(side='left')

		сам.кнпПуск = тКнопка(сам, text=" \u25b6 ", font=шрифт)
		сам.кнпПуск.pack(side='left')

		сам.кнпПауза = тКнопка(сам, text=" \u23f8 ", font=шрифт)
		сам.кнпПауза.pack(side='left')

		сам.кнпСтоп = тКнопка(сам, text=" \u2b1b ", font=шрифт)
		сам.кнпСтоп.pack(side='left')

		сам.кнпЗакрыть = тКнопка(сам, text=" \u2716 ", font=шрифт)
		сам.кнпЗакрыть.pack(side='right')

		#сам.кнпСССР = тКнопка(сам, text=" \u262d ", font=шрифт)
		#сам.кнпСССР.pack(side='left')
