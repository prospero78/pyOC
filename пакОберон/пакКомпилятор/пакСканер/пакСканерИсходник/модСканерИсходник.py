# coding: utf8
"""
Модуль предоставляет тип Исходника.
Производит первоначальное чтение, разбивает на типовые цепочки литер,
отбрасывает мусор
"""

if True:
	from numba import jit
	from пакОберон.пакКомпилятор.пакСущность.пакКоорд import тКоордФикс, тКоордИзм
	from .модСканерИсхСтроки import тСканерИсхСтроки
	from .модСканерИсхТекст import тСканерИсхТекст
	from пакОберон.пакКомпилятор.пакСущность.пакСлово import тСлово

class тСканерИсходник:
	def __init__(сам, пИмяФайла : str):
		"""
		:param пИмяФайла: str
		"""
		def ИмяФайла_Проверить():
			"""
			1. Имя файла должно быть строкой
			2. Имя файла не может быть пустым
			"""
			############## 1 ##########
			бУсл = type(пИмяФайла) == str
			стрСообщ = "тИсходник.__init__(): пИмяФайла должно быть строкой, type(пИмяФайла)=" + \
						str(type(пИмяФайла))
			assert бУсл, стрСообщ

			############ 2 ############
			бУсл = пИмяФайла != ""
			стрСообщ = "тИсходник.__init__(): пИмяФайла не должно быть пустым"
			assert бУсл, стрСообщ

		ИмяФайла_Проверить()

		сам.__исх  = тСканерИсхТекст(пИмяФайла)   # хранит текст исходного кода
		сам.строки = тСканерИсхСтроки(сам.__исх())# список строк исходного текста
		сам.слова_модуля = {}      # список слов в тексте
		сам.коорд = тКоордИзм(1, 0) # общая позиция в исходном тексте
		сам.__указ = 0          # бегунок в исходнике
		сам.модуль    = None    # модуль слов для компиляции
		сам.__Обработать()
	@jit(nogil=True, cache=True)
	def __Слово_Добав(сам, пСлово : тСлово):
		"""
		Процедура добавляет слово с атрибутами положения в исходном тексте.
		Строки исходника остаются отдельно.
		"""
		слово = тСлово(сам, пСлово)
		сам.слова_модуля[сам.цСловаВсего] = слово
		сам.коорд.Поз_Доб()

	def НаСлова_Разделить(сам):
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

	@jit(nogil=True, cache=True)
	def СловаМодуля_Печать(сам):
		print("тСканерИсходник: всего слов модуля", сам.цСловаВсего)
		for ключ in сам.слова_модуля:
			слово = сам.слова_модуля[ключ]
			print(слово)

	@jit(nogil=True, cache=True)
	def Парам_Получ(сам) -> dict:
		парам = {}
		парам['секция'] = "MODULE"
		парам['слова'] = сам.слова_модуля
		парам['слова_секции'] = {}
		return парам

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
			while лцСловоНомер < len(сам.слова_модуля):
				слово = сам.слова_модуля[лцСловоНомер]
				if слово.строка == "(*": # начался пропуск слов
					бКоммент = True
					лцУровень += 1
				elif слово.строка == "*)":
					лцУровень -= 1

				# пропуск слов внутри комментария
				if лцУровень == 0 and слово.строка != "*)":
					слова[лцНомерЧистый] = слово
					лцНомерЧистый += 1

				лцСловоНомер += 1
			# проверка на сбалансированность уровня вложения
			бУсл = лцУровень == 0
			стрОш = "Открытие и закрытие комментариев в модуле не сбалансировано, лцУровень=" + str(лцУровень)
			assert бУсл, стрОш
			сам.слова_модуля = слова
			return бКоммент
		while Коммент_Выкинуть():
			pass

	def Модуль_Обработать(сам):
		def Парам_Получить():
			парам = {}
			парам['секция'] = "MODULE"
			парам['слова'] = сам.слова_модуля
			парам['слова_секции'] = {}
			return парам
		модуль = тМодуль(Парам_Получить())
		сам.модуль = модуль

	def __Обработать(сам):
		#сам.строки.ПоСтр_Печать()
		сам.НаСлова_Разделить()
		#сам.Слова_Печать()
		сам.Комментарии_Выкинуть()
		#сам.__конс.Печать("===Чистые слова===")
		#сам.Слова_Печать()
		#сам.Модуль_Обработать()

	@property
	def цСловаВсего(сам):
		return len(сам.слова_модуля)
