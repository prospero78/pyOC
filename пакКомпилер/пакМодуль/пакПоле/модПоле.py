# coding:utf8
"""
Модуль описывает поле ранее описанного типа в составе записи.
"""
if True:
	from пакКомпилер.пакСлово import тСлово
	from пакКомпилер.пакМодуль.пакТипы.модРод import тРод
	from . модПолеВстроен import тПолеВстроен

class тПоле:
	def __init__(сам, пТипЗапись):
		сам.тип = пТипЗапись.тип  # ссылка на тТип
		сам.запись = пТипЗапись   # ссылка на тТипЗапись
		сам.__имя = ""
		сам.__тип = ""
		сам.__поле_словарь =  {} # если вдруг поле окажется составным
		сам.__бЭкспорт = False
		print("      Поле:")
		сам.__Имя_Проверить()
		сам.__Экспорт_Проверить()
		сам.__Двоеточие_Обрезать()
		сам.__Род_Проверить() # основная работа по родам полей

	def Разделитель_Обрезать(сам):
		"""
		В полях может встречаться как разделитель ";", так и
		окончание описания типа "END"+";".
		"""
		строка_раздел = сам.Слово_Проверить()
		if строка_раздел == ";": # закрытие имени предка
			сам.СловаСекции_Обрезать()
		elif строка_раздел == "END":
			pass # ничего не делаем, так как эти строки будет обрабатывать тип.
		else:
			assert False, "тПоле: разделитель поля должен быть ';',  строка=" + строка_раздел

	def __Двоеточие_Обрезать(сам):
		"""
		Здесь может быть только ":"
		Даже для описания встроенных в типы записей
		"""
		строка_двоеточ = сам.тип.Слово_Проверить()
		if строка_двоеточ == ":": # есть двоеточие
			сам.тип.СловаСекции_Обрезать()
		else: # а это уже непонятно что
			assert строка_двоеточ != тСлово, "тПоле: строка должна быть ':',    строка=" + строка_двоеточ

	def __Имя_Проверить(сам):
		"""
		Получает имя поля.
		"""
		слово_имя = сам.тип.слова_секции[0]
		assert слово_имя != тСлово, "тПоле: имя поля должно быть тСлово, тип="+str(type(слово_имя))
		if слово_имя.ЕслиИмя():
			сам.__имя = сам.тип.Слово_Проверить()
			сам.тип.СловаСекции_Обрезать()
			print("            имя= ", сам.__имя)
		else:
			assert False, "Имя поля внутри типа должно быть именем, " + слово_имя.строка

	def Тип_Проверить(сам):
		"""
		Получает тип поля.
		Для внешнего потребления.
		"""
		слово_тип = сам.тип.слова_секции[0]
		assert слово_тип != тСлово, "тПоле: тип поля должно быть тСлово, тип="+str(type(слово_тип))
		if слово_тип.ЕслиИмя():
			сам.__тип = сам.тип.Слово_Проверить()
			сам.тип.СловаСекции_Обрезать()
		else:
			assert False, "Тип поля внутри типа должно быть именем, " + слово_тип.строка
		print("            тип= ", сам.__тип)

	def __Род_Проверить(сам):
			"""
			Пытается вычислить поле в простой записи.
			слово тип может быть как встроенным, так и определяемое пользователем.
			"""
			строка_тип = сам.тип.Слово_Проверить()
			if строка_тип in тРод.тип_встроен:
				поле = тПолеВстроен(сам)
			elif строка_тип == "ARRAY":
				поле = тПолеМассив(сам)

	def __Экспорт_Проверить(сам):
		"""
		Проверяет является ли поле экспортируемым.
		Эта процедура продублирована из тТипБазовый, так как
		у поля свой признак экспорта, а типа свой.
		"""
		строка_экспорт = сам.тип.Слово_Проверить()
		if строка_экспорт == "*": # есть экспорт
			сам.тип.СловаСекции_Обрезать()
			сам.__бЭкспорт = True
		elif строка_экспорт == ":":
			# это определение внутреннего поля, экспорт уже установлен как надо
			pass
		else:
			assert False, "тПоле: Символ экспорта допустим '*' или '=',    строка=" + строка_экспорт
		print("        экспорт= ", сам.__бЭкспорт)

	def Тип_Уст(сам, пТип):
		"""
		Тип поля должен быть типом в тРод.
		"""
		assert type(пТип) == str, "Тип поля должен быть типом str, тип=" + str(type(пТип))
		сам.__тип = пТип
		print("            тип= ", сам.__тип)
