"""
Рамка содержит элементы средней части окна.
"""

from tkinter import Frame as тРамка, Text as тТекст, Scrollbar as тСкроллБар, \
	Label as тНадпись

class тРамкаСред(тРамка):
	def __init__(сам, root, master):
		сам.__root = root
		сам.__master = master
		тРамка.__init__(сам, master)
		сам.pack(side='top', expand=True, fill='both')

		рамкаСтатус = тРамка(сам, relief='sunken', border=3)
		рамкаСтатус.pack(side='bottom', fill='x')

		надСтрока = тНадпись(рамкаСтатус, text="Строка", relief='ridge', border=3, \
								font = "Consolas 10")
		надСтрока.pack(side='left')

		сам.__надНомерСтрока = тНадпись(рамкаСтатус, text="0000", relief='sunken', \
								border=3, font = "Consolas 10")
		сам.__надНомерСтрока.pack(side='left')

		надПозиция = тНадпись(рамкаСтатус, text="   Поз", relief='ridge', border=3, \
								font = "Consolas 10")
		надПозиция.pack(side='left')

		сам.__надНомерПоз = тНадпись(рамкаСтатус, text="0000", relief='sunken', \
								border=3, font = "Consolas 10")
		сам.__надНомерПоз.pack(side='left')

		сам.текстКод = тТекст(сам, font="Consolas 11")
		скроллВерт   = тСкроллБар(сам, command=сам.текстКод.yview)
		скроллВерт.pack(side="right", fill="y")

		сам.текстКод.config(yscrollcommand=скроллВерт.set)

		сам.текстКод.pack(expand=True, fill='both')

		сам.теги = [] # теги для подсветки текста
		сам.Расцветить()

	def Теги_Добавить(сам, теги:tuple) -> None:
		for тег in теги:
			сам.текстКод.tag_config('_'+тег+'_', font=("Consolas", 11, 'bold'), foreground="#d01010")
		сам.теги=теги
		сам.текстКод.tag_config('_normal_', font=("Consolas", 11), foreground="black", background="gray")
		сам.теги.append('normal')
		# сам.текстКод.tag_config('_line_num_', font=("Courier", 11), foreground="#AFF", background="gray")
		# сам.теги.append('line_num')

	def Расцветить(сам):
		for тег in сам.теги:
			сам.текстКод.tag_remove("_"+тег+"_",1.0,'end')
		#сам.текстКод.tag_add('_normal_',1.0,'end')

		# получить весь текст из элемента
		код = сам.текстКод.get("1.0","end")
		сам.after(250, сам.Расцветить)
		if len(код) < 2:
			return
		# разелить построчно
		код = код.split("\n")
		# проход по всему списку тегов
		for тег in сам.теги:
			дл = len(тег)
			тег_имя = "_"+тег+"_"
			цСтр=0
			for строка in код:
				цСтр += 1
				# # ============ подсветка номера строки =========
				# стрНом = str(цСтр)
				# while len(стрНом)<4:
					# стрНом = "0"+стрНом
				# строка = стрНом +строка
				# стрИсх = сам.текстКод.get(str(цСтр)+'.0', str(цСтр)+'.4')
				# стрНомер = стрИсх[:4]
				# if стрНом != стрНомер: # была вставлена или удалена строка
					# сам.текстКод.delete(str(цСтр)+'.0', str(цСтр)+'.4')
					# сам.текстКод.insert(str(цСтр)+'.0', стрНом)
				# сам.текстКод.tag_add("_line_num_", str(цСтр)+'.0',  str(цСтр)+'.4')
				# # =============================================
				поз = 0
				while True:
					поз = строка.find(тег, поз)
					if поз == -1:
						break
					else:
						сам.текстКод.tag_add(тег_имя, str(цСтр)+'.'+str(поз),  str(цСтр)+'.'+str(поз+дл))
						поз += дл

	def Исх_Вставить(сам, пИсх):
		сам.текстКод.delete('1.0','end')
		сам.текстКод.insert('end',пИсх)

		сам.after(250, сам.Расцветить)
		# пИсх = пИсх.split("\n")
		# цСтр = 0
		# for стрИсх in пИсх:
			# цСтр += 1
			# стрНом = str(цСтр)
			# while len(стрНом)<4:
				# стрНом = "0"+стрНом
			# стрИсх = стрНом + стрИсх +"\n"
			# сам.текстКод.insert("end", стрИсх)
