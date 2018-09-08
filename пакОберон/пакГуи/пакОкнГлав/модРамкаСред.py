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
		сам.теги = [] # теги для подсветки текста
		сам.Расцветить()

	def Теги_Добавить(сам, теги:tuple) -> None:
		for тег in теги:
			сам.текстКод.tag_config('_'+тег+'_', font=("Consolas", 11, 'bold'), foreground="#d01010")
		сам.теги=теги
		сам.текстКод.tag_config('_normal_', font=("Consolas", 11), foreground="black", background="gray")
		сам.теги.append('_normal_')

	def Расцветить(сам):
		for тег in сам.теги:
			сам.текстКод.tag_remove("_"+тег+"_",1.0,'end')
		#сам.текстКод.tag_add('_normal_',1.0,'end')

		код = сам.текстКод.get("1.0","end")
		код = код.split("\n")
		# проход по всему списку тегов
		for тег in сам.теги:
			дл = len(тег)
			имя = "_"+тег+"_"
			цСтр=0
			for строка in код:
				поз = 0
				цСтр += 1
				while True:
					поз = строка.find(тег, поз)
					if поз == -1:
						break
					else:
						сам.текстКод.tag_add(имя, str(цСтр)+'.'+str(поз),  str(цСтр)+'.'+str(поз+дл))
						поз += дл
		сам.after(250, сам.Расцветить)
