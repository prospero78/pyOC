# coding: utf8
"""
Предоставляет тип сканера для обработки текста на входе.
Сканер служит для первичного сканирования текста.
Он же проверяет правильность поступления слов из исходного текста.
"""
if True:
	from .пакИсходник import тИсходник

class тСканер:
	def __init__(сам):
		сам.исх    = тИсходник("Hello.o7")

	def Выполнить(сам):
		сам.исх.Обработать()
