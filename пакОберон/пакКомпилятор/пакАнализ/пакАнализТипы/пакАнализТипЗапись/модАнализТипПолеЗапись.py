# coding: utf8
"""
Модуль для типа поле-переменная.
"""

if True:
	from пакОберон.пакКомпилятор.пакСущность.пакСлово import тСлово
	from пакОберон.пакКомпилятор.пакСущность.пакРод import тРод
	from .модАнализТипПолеБазовый import тАнализТипПолеБазовый
	from .модАнализТипПолеВстроен   import тАнализТипПолеВстроен
	from .модАнализТипПолеПерем   import тАнализТипПолеПерем
	from .модАнализТипПолеМассив  import тАнализТипПолеМассив

class тАнализТипПолеЗапись(тАнализТипПолеБазовый):
	def __init__(сам, пДанные):
		тАнализТипПолеБазовый.__init__(сам, пДанные)
		сам.__имя = "" # имя записи
		сам.__бЭкспорт = False # экспорт в полях низкого уровня не вычисляется
		сам.__бЭкспорт_бПрисвоено = False # Защёлка присвоения экспорта
		сам.__бЭкспорт = False # бЭкспорт будет выясняться самими силами поля
		сам.__бСсылка_бПрисвоено = False # Защёлка присвоения ссылки
		сам.__бСсылка = False
		сам.__предок = тРод.сБезПредка

		сам.ИмяПоле_Проверить()
		сам.бЭкспорт_Проверить()
		сам.Двоеточие_Обрезать()
		сам.__ЗАПИСЬ_Проверить()
		if сам.__СкобкаЛевая_Обрезать():
			сам.Предок_Проверить()
			print("тАнализТипПолеЗапись: 0003 предок записи=", сам.предок)
			сам.__СкобкаПрав_Обрезать()
		while not сам.__ЕслиКОНЕЦ_Обрезать():
			слово_конец = сам.слова_секции[0]
			print("тАнализТипПолеЗапись: 0004 конец записи=", слово_конец.строка, слово_конец.стрИсх)
			сам.__Поля_Проверить()
		сам.Разделитель_Обрезать()

	def __ЗАПИСЬ_Проверить(сам):
		слово_запись = сам.слова_секции[0]
		строка_запись = слово_запись.Проверить()
		if строка_запись != "RECORD":
			assert False, "тАнализТипПолеЗапись: пропущено ключевое слово RECORD?"+слово_запись.стрИсх
		сам.СловаСекции_Обрезать()

	def __СкобкаЛевая_Обрезать(сам):
		"""
		В этой позиции может быть скобка, а может и нет. Надо проверять.
		"""
		бРезультат = False
		слово_скобка = сам.слова_секции[0]
		строка_скобка = слово_скобка.Проверить()
		if строка_скобка == "(":
			бРезультат = True
			сам.СловаСекции_Обрезать()
		return бРезультат

	def __СкобкаПрав_Обрезать(сам):
		слово_скобка = сам.слова_секции[0]
		строка_скобка = слово_скобка.Проверить()
		if строка_скобка != ")": # закрытие имени предка
			assert False, "тАнализТипПолеЗапись: пропущена закрывающая скобка предка?"+слово_скобка.стрИсх
		сам.СловаСекции_Обрезать()

	def __Поля_Проверить(сам):
		"""
		В записях ВСЕГДА встречается окончание "END" даже без
		вложенных полей.
		Если вложенных полей нет -- значит разбор полей не вызываем.
		Поэтому здесь проверяем в цикле все поля, пока не закончатся
		Внутри поля-записи могут быть другие поля-записи.
		Если до END встречается RECORD -- значит надо рекурсивно вызывать себя.
		"""
		def ИмяПоле_Проверить():
			"""
			Проверяет имя поля в записи, должно быть простым.
			Поскольку имён полей с одним типом может быть несколько -- каждое
			поле в группе добавляется под своим номером.
			"""
			слово_имя = сам.слова_секции[сам.__индекс]
			имя = слово_имя.Проверить()
			if слово_имя.ЕслиИмя_Строго():
				print("тАнализТипПолеЗапись: 0501 Имя поля=", имя, слово_имя.стрИсх)
				#сам.СловаСекции_Обрезать()
				сам.__индекс += 1
				return имя
			else:
				assert False, "тАнализТипПолеЗапись: 0790 имя поля недопустимо="+имя+слово_имя.стрИсх

			слово_поле = сам.слова_секции[0]
		def бЭкспорт_Проверить():
			"""
			Проверяет является ли поле экспортируемым.
			"""
			слово_экспорт = сам.слова_секции[сам.__индекс]
			строка_экспорт = слово_экспорт.Проверить()
			бЭкспорт = False
			if строка_экспорт == "*": # есть экспорт
				#сам.СловаСекции_Обрезать()
				бЭкспорт = True
				сам.__индекс += 1
				print("тАнализТипПолеЗапись: 5571 экспорт поля=", сам.__бЭкспорт)
			elif строка_экспорт == "," or строка_экспорт == ":":
				pass # это определение списка полей
			else:
				assert False, "тАнализТипПолеЗапись: 5570 Символ экспорта допустим '*' или '='" + слово_экспорт.стрИсх
			return бЭкспорт
		def Двоеточие_Обрезать():
			"""
			Здесь может быть только ":"
			"""
			слово_двоеточ = сам.слова_секции[сам.__индекс]
			строка_двоеточ = слово_двоеточ.Проверить()
			if строка_двоеточ == ":": # есть двоеточие
				#сам.СловаСекции_Обрезать
				сам.__индекс += 1
			else: # а это уже непонятно что
				assert False, "тАнализЗаписьПоле: разделитель должен быть ':'" + слово_двоеточ.стрИсх

		сам.__индекс = 0
		парам = {}
		парам['слова'] = сам.слова_секции
		парам['секция']="TYPE_FIELD"
		парам['имя']=ИмяПоле_Проверить()
		парам['экспорт']=бЭкспорт_Проверить()
		Двоеточие_Обрезать()
		слово_поле = сам.слова_секции[сам.__индекс]
		строка_поле = слово_поле.Проверить()
		if строка_поле in тРод.тип_встроен:
			поле = тАнализТипПолеВстроен(парам)
			сам.__поле = поле
			сам.слова_секции = {}
			сам.слова_секции = поле.слова_секции
		elif слово_поле.ЕслиИмя_Строго():
			поле = тАнализТипПолеПерем(парам)
			сам.__поле = поле
			сам.слова_секции = {}
			сам.слова_секции = поле.слова_секции
		elif строка_поле == "ARRAY":
			поле = тАнализТипПолеМассив(парам)
			сам.__поле = поле
			сам.слова_секции = {}
			сам.слова_секции = поле.слова_секции
		elif строка_поле == "RECORD":
			поле = тАнализТипПолеЗапись(парам)
			сам.__поле = поле
		else:
			assert False, "ХХХ Неизвестный тип поля"
		сам.слова_секции = {}
		сам.слова_секции = поле.слова_секции

	def __ЕслиКОНЕЦ_Обрезать(сам) -> bool:
		"""
		Здесь может встретиться как "END", так и начало втсроенной записи полей.
		"""
		бКонец = False
		слово_конец = сам.слова_секции[0]
		строка_конец = слово_конец.Проверить()
		print("тАнализТипПолеЗапись: ********** конец?", строка_конец)
		if строка_конец == "END": # есть окончание
			сам.СловаСекции_Обрезать()
			бКонец = True
			print("тАнализТипПолеЗапись: 8951 если конец записи=", строка_конец, слово_конец.стрИсх)
		return бКонец
