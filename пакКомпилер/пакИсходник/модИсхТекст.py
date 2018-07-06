# coding: utf8
"""
Обеспечивает хранение исходного текста и его обработку.
"""

class тИсхТекст:
	def __init__(сам, пКорень, пИмяФайла):
		def Исх_Загрузить():
			try:
				файл = open(сам.__имя_файла,'r', encoding='utf-8')
				сам.__исх = файл.read()+" "*4
				файл.close()
			except FileNotFoundError:
				стрСообщ = "Не могу найти файл, файл=" + сам.__имя_файла
				сам.ошибка.Печать(стрСообщ)
				#файл.close()
		сам.__исх = ""
		сам.__имя_файла = пИмяФайла
		Исх_Загрузить()

	def Лит(сам, поз):
		return сам.__исх[поз]

	def __call__(сам):
		return сам.__исх

	@property
	def длина(сам):
		return len(сам.__исх)
