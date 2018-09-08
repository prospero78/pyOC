"""
Рамка содержит элементы средней части окна.
"""

from tkinter import Frame as тРамка, Text as тТекст, Scrollbar as тСкроллБар

class тРамкаСред(тРамка):
	def __init__(сам, root, master):
		сам.__root = root
		сам.__master = master
		тРамка.__init__(сам, master)
		сам.pack(expand=True, fill='both')

		сам.текстКод = тТекст(сам, font="Consolas 11")
		скроллВерт   = тСкроллБар(сам, command=сам.текстКод.yview)
		скроллВерт.pack(side="right", fill="y")

		сам.текстКод.config(yscrollcommand=скроллВерт.set)
		сам.текстКод.pack(expand=True, fill='both')
