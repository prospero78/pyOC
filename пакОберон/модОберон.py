# coding: utf8
"""
Предосталвяет главный класс всего компилятора Оберона
"""
if True:
	from .пакКомпилятор import тКомпилер
	from .пакРесурс import тРесурс
	from .пакГуи import тГуи
	from .пакДиагностика.модКонсоль import тКонсоль
	#from .пакДиагностика import тОшибка

class тОберон:
	def __init__(сам)->None:
		сам.компилер = тКомпилер()
		сам.рес    = тРесурс(сам)
		сам.гуи    = тГуи(сам)
		сам.конс   = тКонсоль(сам)
		#сам.ошибка = тОшибка(сам)

	def Выполнить(сам):
		"""
		По умолчанию начинает компиляцию тестового примера.
		"""
		сам.конс.Печать(сам.рес.Компилировать)
		сам.компилер.Выполнить()
		сам.гуи.Пуск()
