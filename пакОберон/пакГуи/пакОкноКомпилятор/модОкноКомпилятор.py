# coding: utf8
"""
Модуль предоставляет окно пошаговой компиляции для визуализации процесса.
"""
if True:
	from пакОберон.пакКомпилятор.пакСущность.пакОшибка import тОшибка
	from пакОберон.пакКомпилятор import тКомпилер
	from tkinter import Toplevel as тОкно, LabelFrame as тРамкаНадп, \
			Button as тКнопка, Text as тРедактор, Scrollbar as тСкроллБар

class тОкноКомпилятор(тОкно):
	def __init__(сам, пОберон):

		сам.__оберон = пОберон
		сам.__компил = None

		тОкно.__init__(сам)
		сам.title("Отладка компилятора")
		сам.protocol("WM_DELETE_WINDOW",сам.Скрыть)
		сам.minsize(600,300)
		сам.withdraw()

		if True: # рамкаВерх
			рамкаВерх = тРамкаНадп(сам, text="Сканер")
			рамкаВерх.pack(side='top', fill='x')

			сам.кнпНачать = тКнопка(рамкаВерх, text="Начать", command=сам.Компил_Начать)
			сам.кнпНачать.pack(side='left')

			сам.кнпШаг = тКнопка(рамкаВерх, text="Шаг", state='disable', command = сам.Компил_Шаг)
			сам.кнпШаг.pack(side='left')

			сам.кнпЗакончить = тКнопка(рамкаВерх, text="Закончить", state='disable', \
					command = сам.Компил_Закончить)
			сам.кнпЗакончить.pack(side='left')

		if True: # рамкаКод
			рамкаКод = тРамкаНадп(сам, text="Сущности")
			рамкаКод.pack(side='top', fill='both', expand=True)

			сам.редКод = тРедактор(рамкаКод)

			скроллВерт = тСкроллБар(рамкаКод, command=сам.редКод.yview)
			скроллВерт.pack(side="right", fill="y")

			сам.редКод.config(yscrollcommand=скроллВерт.set)
			сам.редКод.pack(fill='both', expand=True)

	def Компил_Шаг(сам):
		сам.__компил.Шаг()

	def Компил_Начать(сам):
		сам.__компил = тКомпилер(сам.__оберон, сам.__оберон.дисп.стрИмяФайла)
		сам.кнпНачать['state'] = 'disable'
		сам.кнпШаг['state'] = 'normal'
		сам.кнпЗакончить['state'] = 'normal'

	def Компил_Закончить(сам):
		сам.__компил = None
		сам.кнпНачать['state'] = 'normal'
		сам.кнпШаг['state'] = 'disable'
		сам.кнпЗакончить['state'] = 'disable'

	def Показать(сам):
		сам.deiconify()
		сам.grab_set()

	def Скрыть(сам):
		сам.withdraw()
		сам.grab_release()
