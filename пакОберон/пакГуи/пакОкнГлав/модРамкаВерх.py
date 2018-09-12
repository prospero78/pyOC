# coding: utf8
"""
Верхняя рамка с кноками меню.
"""

from tkinter import Frame as тРамка, Menubutton as тКнпМну, Menu as тМеню

class тРамкаВерх(тРамка):
	def __init__(сам, пОберон, предок):
		сам.__оберон = пОберон
		сам.__предок = предок
		тРамка.__init__(сам, предок, relief='sunken', border=1)
		сам.pack(side="top", expand=True, fill='x')


		сам.кнпФайл = тКнпМну(сам, text=пОберон.рес.winMain['mnuFile'], relief='raised')
		сам.кнпФайл.pack(side='left')

		сам.мнуФайл = тМеню(сам.кнпФайл, tearoff = 0)
		сам.мнуФайл.add_command(label=пОберон.рес.winMain['mnuOpen'], command = сам.Файл_Открыть)
		сам.мнуФайл.add_separator()
		сам.мнуФайл.add_command(label=пОберон.рес.winMain['mnuExit'], command = пОберон.дисп.Приложение_Закрыть)

		сам.кнпФайл['menu'] = сам.мнуФайл

		сам.кнпАнализ = тКнпМну(сам, text=пОберон.рес.winMain['mnuAnaliz'], relief='raised')
		сам.кнпАнализ.pack(side='left')

		сам.кнпСправка = тКнпМну(сам, text=пОберон.рес.winMain['mnuHelp'], relief='raised')
		сам.кнпСправка.pack(side='left')

		сам.мнуСправка = тМеню(сам.кнпСправка, tearoff = 0)
		сам.мнуСправка.add_command(label=пОберон.рес.winMain['mnuHelpShow'], command = сам.Справка_Показать)

		сам.кнпСправка['menu'] = сам.мнуСправка

	def Файл_Открыть(сам, событие=None):
		from tkinter import filedialog as fd
		file_name = fd.askopenfilename(filetypes=(("Оберон файлы", "*.o7"),
													 ("Текстовые файлы", "*.txt;*.me"),
																("Все файлы", "*.*") ))
		if file_name:
			f = open(file_name, 'r', encoding='utf-8')
			сИсх = f.read()
			f.close()
			сам.__оберон.дисп.Исх_Открыть(сИсх)

	def Справка_Показать(сам, событие=None):
		сам.__оберон.гуи.окнСправка.Показать()
