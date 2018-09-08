"""
Верхняя рамка с кноками меню.
"""

from tkinter import Frame as тРамка, Menubutton as тКнпМну, Menu as тМеню

class тРамкаВерх(тРамка):
	def __init__(сам, root, предок):
		сам.__root = root
		сам.__предок = предок
		тРамка.__init__(сам, предок, relief='sunken', border=1)
		сам.pack(side="top", expand=True, fill='x')


		сам.кнпФайл = тКнпМну(сам, text=root.рес.winMain['mnuFile'], relief='raised')
		сам.кнпФайл.pack(side='left')

		сам.мнуФайл = тМеню(сам.кнпФайл, tearoff = 0)
		сам.мнуФайл.add_command(label=root.рес.winMain['mnuOpen'], command = сам.Файл_Открыть)
		сам.мнуФайл.add_separator()
		сам.мнуФайл.add_command(label=root.рес.winMain['mnuExit'], command = root.дисп.Приложение_Закрыть)

		сам.кнпФайл['menu'] = сам.мнуФайл

		сам.кнпАнализ = тКнпМну(сам, text=root.рес.winMain['mnuAnaliz'], relief='raised')
		сам.кнпАнализ.pack(side='left')

	def Файл_Открыть(сам, событие=None):
		from tkinter import filedialog as fd
		file_name = fd.askopenfilename(filetypes=(("Оберон файлы", "*.o7"),
													 ("Текстовые файлы", "*.txt;*.me"),
																("Все файлы", "*.*") ))
		f = open(file_name, 'r', encoding='utf-8')
		сИсх = f.read()
		f.close()
		сам.__root.дисп.Исх_Открыть(сИсх)
