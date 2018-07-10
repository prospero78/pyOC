# coding: utf8
"""
Содержит код для показа ошибки с текстом и позиции в тесте + выход.
"""
import sys

from ..пакИсходник.модКоординаты import тКоорд
from .модКонсоль import тКонсоль

class тОшибка:
	def __init__(сам, пКорень):
		сам.конс = пКорень.конс

	def Печать(сам, пСообщ):
		'''
		Выводит текст ошибки, если такая встретится в исходном тексте.
		'''
		def Сообщ_Проверить():
			бУсл = isinstance(пСообщ, str)
			стрОш = "тОшибка: Параметр 'пСообщ' должен быть строкой, isinstance="+str(type(пСообщ))
			сам.конс.Проверить(бУсл, стрОш)

		Сообщ_Проверить
		сам.конс.Ошибка(пСообщ)

	def Коорд(сам, пСообщ, пКоорд, пСтрокаИсх):
		'''
		Выводит текст ошибки, если такая встретится в тексте.
		'''
		def Коорд_Проверить():
			бУсл = isinstance(пКоорд, тКоорд)
			стрОш = "тОшибка: Параметр пКоорд должен наследовать тКоорд, isinstance="+str(пКоорд)
			сам.конс.Проверить(бУсл, стрОш)

			бУсл = пКоорд != None
			стрОш = "тОшибка: Параметр 'пКоорд' не может быть пустым значением"
			сам.конс.Проверить(бУсл, стрОш)

		def Сообщ_Проверить():
			бУсл = isinstance(пСообщ , str)
			стрОш = "тОшибка: Параметр 'пСообщ' должен быть строкой, isinstance="+str(пСообщ)
			сам.конс.Проверить(бУсл, стрОш)

		def СтрИсх_Проверить():
			бУсл = isinstance(пСтрокаИсх , str)
			стрОш = "тОшибка: Параметр 'пСтрокаИсх' должен быть строкой, isinstance="+str(пСтрокаИсх)
			сам.конс.Проверить(бУсл, стрОш)

		Коорд_Проверить()
		Сообщ_Проверить()
		СтрИсх_Проверить()

		сам.конс.Исх_Печать(str(пКоорд.стр) + " " + пСтрокаИсх)
		сам.конс.Печать("-" * (пКоорд.поз + len(str(пКоорд.стр))+1) + "^" + \
				" (стр=" + str(пКоорд.стр) + " поз=" + str(пКоорд.поз) + ")")
		сам.конс.Ошибка(пСообщ)
