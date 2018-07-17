# coding: utf8
"""
Модуль предоставляет тип Исходника.
Производит первоначальное чтение, разбивает на типовые цепочки литер,
отбрасывает мусор
"""

if True:
	from .модКоордФикс import тКоордФикс
	from .модКоордИзм import тКоордИзм
	from .модИсхСтроки import тИсхСтроки
	from .модИсхТекст import тИсхТекст
	from пакКомпилер.пакСлово import тСлово
	from пакКомпилер.пакМодуль import тМодуль

class тИсходник:
	def __init__(сам, пКорень, пИмяФайла):
		def ИмяФайла_Проверить():
			"""
			1. Имя файла должно быть строкой
			2. Имя файла не может быть пустым
			"""
			############## 1 ##########
			бУсл = type(пИмяФайла) == str
			стрСообщ = "тИсходник.__init__(): пИмяФайла должно быть строкой, type(пИмяФайла)=" + \
						str(type(пИмяФайла))
			сам.__конс.Проверить(бУсл, стрСообщ)

			############ 2 ############
			бУсл = пИмяФайла != ""
			стрСообщ = "тИсходник.__init__(): пИмяФайла не должно быть пустым"
			сам.__конс.Проверить(бУсл, стрСообщ)

		сам.__корень = пКорень
		сам.__конс = пКорень.конс

		ИмяФайла_Проверить()

		сам.__исх  = тИсхТекст(пКорень, пИмяФайла)   # хранит текст исходного кода
		сам.строки = тИсхСтроки(пКорень, сам.__исх())# список строк исходного текста
		сам.__слова = {}      # список слов в тексте
		сам.коорд = тКоордИзм(1, 0) # общая позиция в исходном тексте
		сам.__указ = 0          # бегунок в исходнике
		сам.__модули    = {}    # перечень модулей для компиляции
		сам.__ошибка    = пКорень.ошибка

	def __Слово_Добав(сам, пСлово):
		"""
		Процедура добавляет слово с атрибутами положения в исходном тексте.
		Строки исходника остаются отдельно.
		"""
		слово = тСлово(сам, пСлово)
		сам.__слова[сам.цСловаВсего] = слово
		сам.коорд.Поз_Доб()

	def НаТеги(сам):
		def Пробел(лит):
			if лит == ' ':
				сам.коорд.Поз_Доб()
			elif лит == '\t':
				for i in range(3):
					сам.коорд.Поз_Доб()
		def Запятая(лит):
			if лит ==',':
				сам.__Слово_Добав(',')
		def ТочкаЗапятая(лит):
			if лит == ';':
				сам.__Слово_Добав(';')
		def Плюс(лит):
			if лит == '+':
				сам.__Слово_Добав('+', )
		def Минус(лит):
			if лит == '-':
				сам.__Слово_Добав('-')
		def Деление(лит):
			if лит == '/':
				сам.__Слово_Добав('/')
		def ЛеваяСкобка(лит):
			if лит == '(':
				if лит + сам.__исх.Лит(сам.__указ+1) != "(*":
					сам.__Слово_Добав('(')
				else:
					сам.__Слово_Добав('(*')
					сам.коорд.Поз_Доб()
					сам.__указ += 1
		def ПраваяСкобка(лит):
			if лит == ')':
				сам.__Слово_Добав(')')
		def НоваяСтрока(лит):
			if лит == '\n':
				сам.коорд.Стр_Доб()
				сам.коорд.Поз_Сброс()
		def Умножить(лит):
			if лит == '*':
				if лит + сам.__исх.Лит(сам.__указ+1) == "*)":
					сам.__Слово_Добав('*)')
					сам.коорд.Поз_Доб()
					сам.__указ += 1
				else:
					сам.__Слово_Добав('*')
		def Двоеточие(лит):
			if лит == ':':
				if лит + сам.__исх.Лит(сам.__указ+1) == ":=":
					сам.__Слово_Добав(':=')
					сам.коорд.Поз_Доб()
					сам.__указ += 1
				else:
					сам.__Слово_Добав(':')
		def ПереводКаретки(лит):
			if лит == '\r':
				сам.коорд.поз += 1
		def ЕслиСущность(лит):
			"""
			Если началось число или имя сущности.
			"""
			# если "_" или буква -- то это только имя
			сущн = ""
			if лит=="_" or лит.isalpha():
				while лит.isalpha() or лит.isdigit() or лит=="_":
					сущн += лит
					сам.__указ += 1
					сам.коорд.Поз_Доб()
					лит = сам.__исх.Лит(сам.__указ)
				else:
					# откат на одну позицию
					сам.__указ -= 1
					сам.коорд.цПоз = сам.коорд.цПоз - len(сущн)
					сам.__Слово_Добав(сущн)
					сам.коорд.цПоз = сам.коорд.цПоз + len(сущн)-1

			# возможно это число
			elif лит.isdigit():
				while лит.isdigit() or лит == ".":
					сущн += лит
					сам.__указ += 1
					сам.коорд.Поз_Доб()
					лит = сам.__исх.Лит(сам.__указ)
				else:
					# откат на одну позицию
					сам.__указ -= 1
					сам.коорд.цПоз = сам.коорд.цПоз - len(сущн)
					сам.__Слово_Добав(сущн)
					сам.коорд.цПоз = сам.коорд.цПоз + len(сущн)-1
		def Равно(лит):
			if лит =='=':
				сам.__Слово_Добав('=')
		def Точка(лит):
			if лит =='.':
				сам.__Слово_Добав('.')
		def Кавычка2(лит):
			"""
			Вычисляет строки.
			"""
			if лит == '"':
				стр = ''
				лит = ""
				while лит !='"':
					сам.__указ += 1
					сам.коорд.Поз_Доб()
					лит = сам.__исх.Лит(сам.__указ)
					стр += лит
				сам.__Слово_Добав(стр)
				сам.коорд.Поз_Доб()

		исх_длина = сам.__исх.длина - 1
		while сам.__указ-1 < исх_длина:
			лит = сам.__исх.Лит(сам.__указ)
			Пробел(лит)
			Запятая(лит)
			ТочкаЗапятая(лит)
			ЛеваяСкобка(лит)
			ПраваяСкобка(лит)
			НоваяСтрока(лит)
			Умножить(лит)
			Двоеточие(лит)
			ПереводКаретки(лит)
			ЕслиСущность(лит)
			Равно(лит)
			Точка(лит)
			Кавычка2(лит)
			Плюс(лит)
			Минус(лит)
			Деление(лит)
			сам.__указ += 1

	def Слова_Печать(сам):
		for ключ in сам.__слова:
			слово = сам.__слова[ключ]
			сам.__конс.Печать(str(слово))

	def Комментарии_Выкинуть(сам):
		"""
		Выкидывать по кругу комментарии, пока не будут выкинуты полностью.
		"""
		def Коммент_Выкинуть():
			"""
			Нагло выкидывает комментарий из слов.
			Должен контролировать непарное открытие и закрытие комментариев.
			"""
			бКоммент = False
			лцСловоНомер = 0
			лцНомерЧистый = 0
			слова = {} # чистый список слов
			лцУровень = 0 # уровен вложенных комментариев
			while лцСловоНомер < len(сам.__слова):
				слово = сам.__слова[лцСловоНомер]
				if слово.строка == "(*": # начался пропуск слов
					бКоммент = True
					лцУровень += 1
				elif слово.строка == "*)":
					лцУровень -= 1

				# пропуск слов внутри комментария
				if лцУровень == 0 and слово.строка != "*)":
					слово._Номер_Уст(лцНомерЧистый)
					слова[лцНомерЧистый] = слово
					лцНомерЧистый += 1

				лцСловоНомер += 1
			# проверка на сбалансированность уровня вложения
			бУсл = лцУровень == 0
			стрОш = "Открытие и закрытие комментариев в модуле не сбалансировано, лцУровень=" + str(лцУровень)
			сам.__конс.Проверить(бУсл, стрОш)
			сам.__слова = слова
			return бКоммент
		while Коммент_Выкинуть():
			pass

	def Модуль_Обработать(сам):
		модуль = тМодуль(сам.__корень, сам.__слова)
		сам.__модули[0] = модуль
		модуль.Обработать()

	def Обработать(сам):
		#сам.строки.ПоСтр_Печать()
		сам.НаТеги()
		#print('===Грязные слова===')
		#сам.Слова_Печать()
		сам.Комментарии_Выкинуть()
		#сам.__конс.Печать("===Чистые слова===")
		#сам.Слова_Печать()
		сам.Модуль_Обработать()

	@property
	def цСловаВсего(сам):
		return len(сам.__слова)


	@property
	def корень(сам):
		return сам.__корень
