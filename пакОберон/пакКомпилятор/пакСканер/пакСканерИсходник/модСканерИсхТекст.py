# coding: utf8
"""
Обеспечивает хранение исходного текста и его обработку.
"""

from numba import jit
class тСканерИсхТекст:
	def __init__(сам, пИмяФайла:str) -> None:
		"""

		:param пИмяФайла: str
		"""
		def Исх_Загрузить():
			try:
				файл = open(сам.__имя_файла,'r', encoding='utf-8')
				сам.__исх = файл.read()+" "*4
				сам.__исх = сам.__исх.replace("\t", "   ")
				файл.close()
			except FileNotFoundError:
				стрСообщ = "Не могу найти файл, файл=" + сам.__имя_файла
				assert False, стрСообщ
				#файл.close()
		сам.__исх:str = ""
		сам.__имя_файла:str = пИмяФайла
		Исх_Загрузить()

	@jit
	def Лит(сам, цПоз:int) -> int:
		"""
		Возвращает позицию литеры в строке
		:param поз: int
		:return: int
		"""
		return сам.__исх[цПоз]

	def __call__(сам) -> str:
		"""

		:return:str
		"""
		return сам.__исх

	@property
	def длина(сам) -> str:
		"""
		Возвращает число литер в исходнике
		:return: int
		"""
		return len(сам.__исх)
