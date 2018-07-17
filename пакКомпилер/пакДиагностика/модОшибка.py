# coding: utf8
"""
Содержит код для показа ошибки с текстом и позиции в тесте + выход.
"""
import sys

from ..пакИсходник.модКоордФикс import тКоордФикс
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
			бУсл = isinstance(пКоорд, тКоордФикс)
			стрОш = "тОшибка: Параметр пКоорд должен наследовать тКоордФикс, isinstance="+str(пКоорд)
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

		сам.конс.Печать("-" * (пКоорд.цПоз + len(str(пКоорд.цСтр))+2) + "^" + \
				" (стр=" + str(пКоорд.цСтр) + " поз=" + str(пКоорд.цПоз) + ")")
		сам.конс.Ошибка(пСообщ)
		сам.конс.Исх_Печать(str(пКоорд.цСтр) + " " + пСтрокаИсх)
