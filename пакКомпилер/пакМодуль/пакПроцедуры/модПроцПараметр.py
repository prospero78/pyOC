# coding: utf8
"""
Модуль описывает структуру -- параметр процедуры
"""

class тПроцПараметр:
	def __init__(сам, пПроц):
		сам.проц = пПроц # родительская процедура
		сам.бСсылка = False # является ли параметр ссылочным
		сам.параметры = {} # параметров в поле может быть несколько
		сам.__предок = "" # Предок-тип параметров процедуры в группе
		сам.__Ссылка_Проверить()
		сам.__Имя_Проверить()
		while сам.__Запятая_Проверить():
			сам.__Имя_Проверить()
		сам.__Двоеточие_Обрезать()
		сам.__Предок_Проверить()
		сам.__Разделитель_Обрезать()

	def __Разделитель_Обрезать(сам):
		"""
		В простых типах последнее слово ";"
		Поэтому его необходимо обрезать
		"""
		строка_раздел = сам.проц.Слово_Проверить()
		if строка_раздел == ";":
			сам.проц.СловаСекции_Обрезать()
		elif строка_раздел == ")":
			pass # это конец полей параметров процедуры
		else:
			assert False, "тПроцПараметр: неправильный разделитель поля, строка=" + строка_раздел

	def __Предок_Проверить(сам):
		"""
		Проверяет предка параметров процедуры. Должно быть разрешённой строкой.
		Кроме того, имя может быть составным
		"""
		стрОш = "тПроцПараметр: тип параметра должно быть допустимым именем, имя="
		бРезульт = False
		имя = сам.проц.Слово_Проверить()
		слово_имя = сам.проц.слова_секции[0]
		assert слово_имя.ЕслиСтр_Допустимо(), стрОш + имя
		сам.__предок = ""
		while not ((имя == ";") or (имя == ")")):
			сам.проц.СловаСекции_Обрезать()
			сам.__предок += имя
			имя = сам.проц.Слово_Проверить()
			слово_имя = сам.проц.слова_секции[0]
			бРезульт = True
		assert сам.__предок != "", "тПроцПараметр: тип параметра не может быть пустой строкой"
		print("Предок:", сам.__предок)
		return бРезульт

	def __Двоеточие_Обрезать(сам):
		"""
		Здесь может быть только ":"
		"""
		строка_двоеточ = сам.проц.Слово_Проверить()
		if строка_двоеточ == ":": # есть двоеточие
			сам.проц.СловаСекции_Обрезать()
		else: # а это уже непонятно что
			assert False, "тПроцПараметр: разделитель должен быть ':',    строка=" + строка_двоеточ
		print("Двоеточие обрезано")

	def __Запятая_Проверить(сам):
		"""
		Проверяет не следует ли запятая за именем параметра
		Если их несколько
		"""
		бЗапятая = False
		запятая = сам.проц.Слово_Проверить()
		if запятая == ",":
			сам.проц.СловаСекции_Обрезать()
			бЗапятая = True
		elif запятая == ":":
			pass # это началось описание типа
		else:
			assert False, "тПроцПараметр: допустимая строка ',' или ':', имя=" + запятая
		print("    запятая:", запятая)
		return бЗапятая

	def __Имя_Проверить(сам):
		"""
		Проверяет имя параметра.
		Имя НЕ МОЖЕТ быть составным
		"""
		имя = сам.проц.Слово_Проверить()
		слово_имя = сам.проц.слова_секции[0]
		if слово_имя.ЕслиИмя():
			сам.проц.СловаСекции_Обрезать()
			сам.параметры[len(сам.параметры)] = имя
		else:
			assert False, "тПроцПараметр: имя параметра должно быть допустимым именем, имя=" + имя
		print("    Имя:", имя)

	def __Ссылка_Проверить(сам):
		"""
		Проверяет является ли параметр ссылочным.
		"""
		строка_ссылка = сам.проц.Слово_Проверить()
		if строка_ссылка == "VAR":
			сам.бСсылка = True
			сам.проц.СловаСекции_Обрезать()
		print("    бСсылка=", сам.бСсылка)
