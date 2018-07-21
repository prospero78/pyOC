# coding: utf8
"""
Модуль предоставляет тип тМодуль.
Содержит процедуры по разбору модуля.

Модуль -- это контейнер с жёсткой структурой.
Обязательно содержит:
1. Заголовок модуля
2. Окончание модуля.

Возможно содержит:
1. Секция импорта
2. Секцию констант
3. Секцию типов
4. Секцию переменных
5. Секцию процедур
6. Секция инициализации модуля.
"""

if True:
	from ..пакСлово import тСлово
	from .пакСекция import тСекцияМодуль

	from .пакСекции import тИмпорт
	from .пакСекции import тКонстанты
	from .пакСекции import тТипы
	from .пакСекции import тПеременные
	from .пакСекции import тПроцедуры

class тМодуль(тСекцияМодуль):
	"""
		Тип представляет иерархию модуля с секциями.
	"""
	def __init__(сам, пДанные):
		тСекцияМодуль.__init__(сам, пДанные)

		# содержимое словаря не контролируется
		сам.__бМодульОдин = False # Признак, что MODULE встречается один раз

		#сам.импорт = тИмпорт(сам.слова_модуля)
		сам.__импорт = {} # объекты импорта
		сам.__конст  = {} # объекты констант
		сам.__типы   = {} # объекты типов
		сам.__перем  = {} # объекты переменных
		сам.__проц   = {} # объекты процедур
		сам.__начало = {} # объекты в корне модуля

		сам.__Обработать()

	def Модуль_Контроль(сам):  # Проверить правильность объявления модуля.
		'''
		Контроль на правильное открытие и закрытие модуля.
		'''
		def НачалоМодуль_Проверить():
			"""
			слово MODULE  в исходнике должен идти первым.
			"""
			слово = сам.слова_модуля[0]
			# проверить, что слово является тСлово
			assert type(слово) == тСлово, "Слово должно быть тСлово, type="+type(слово)
			assert слово.строка == "MODULE", "тМодуль: В файле отсутствует MODULE" + слово.стрИсх
			сам.__СловаМодуля_Обрезать()
		def Имя_Проверить():
			"""
			Второй слово должно быть правильное имя модуля.
			"""
			слово = сам.слова_модуля[0]
			assert type(слово) == тСлово, "Слово должно быть тСлово, type="+type(слово)
			assert слово.ЕслиИмя_Строго(), "Нарушение имени модуля"+слово.стрИсх
			# запомним имя модуля
			сам.__имя = слово.строка
			сам.__СловаМодуля_Обрезать()
		def НачалоРазделитель_Проверить():
			"""
			Третьим тегом идёт окончание заголовка модуля.
			"""
			слово = сам.слова_модуля[0]
			assert type(слово) == тСлово, "Слово должно быть тСлово, type="+type(слово)
			assert слово.строка == ";", "Нарушение окончания имени модуля"+слово.стрИсх
			сам.__СловаМодуля_Обрезать()
		def КонецМодуль_Найти():
			"""
			Вычисляет окончание модуля.
			"""
			цСчётОбр = сам.цСловаМодуля-1
			while цСчётОбр >= 0:
				слово_точка = сам.слова_модуля[цСчётОбр]
				стрТочка = слово_точка.строка
				assert type(слово_точка) == тСлово, "тМодуль: Слово должно быть тСлово, type="+type(слово_точка)
				# Между ними -- возможно имя модуля
				слово_конец = сам.слова_модуля[цСчётОбр-2]
				стрКонец = слово_конец.строка
				if стрТочка == "." and стрКонец == "END":
					слово_имя = сам.слова_модуля[цСчётОбр-1]
					стрИмя = слово_имя.строка
					if стрИмя == сам.__имя:
						сам.Конец_Уст(сам.слова_модуля[цСчётОбр-2])
						break
					else: # имя модуля в начале и конце -- не совпало
						assert False, "тМодуль: Имя модуля не совпадает, модуль="+сам.__имя + \
									слово_имя.стрИсх
				цСчётОбр -= 1

			if цСчётОбр == -1:
				assert False, "тМодуль: Нет окончания модуля "+сам.__имя

			# теперь отбросим окончание модуля.
			счёт_новый = 0
			слова = {}
			# Исключаем концовку модуля (END MyModule.)
			for счёт in range(0, цСчётОбр-2):
				слово = сам.слова_модуля[счёт]
				слова[счёт_новый] = слово
				счёт_новый += 1
			сам.слова_модуля = слова
		def МодульОдин_Проверить():
			# Слово MODULE должно быть одно.
			счётчик_модуль = 0
			for номер_тега in сам.слова_модуля:
				слово = сам.слова_модуля[номер_тега]
				assert type(слово) == тСлово, "Слово должно быть тСлово, type="+type(слово)
				if слово.строка == "MODULE":
					счётчик_модуль += 1
					assert счётчик_модуль < 2, "тМодуль: MODULE в файле должно быть только один раз!"+ слово.стрИсх

		НачалоМодуль_Проверить()
		Имя_Проверить()
		НачалоРазделитель_Проверить()
		КонецМодуль_Найти()
		МодульОдин_Проверить()

	def Секции_Разбить(сам):
		'''
			Разбитие на глобальные секции:
			MODULE
				IMPORT
				CONST
				TYPE
				VAR
				PROCEDURE
			BEGIN [module]
			END [module]
		'''
		парам = {}
		парам['секция'] = "IMPORT"
		парам['слова'] = сам.слова_модуля
		импорт = тИмпорт(парам)
		сам.__импорт = импорт.слова_секции
		сам.слова_модуля = {}
		сам.слова_модуля = импорт.слова_модуля

		парам['секция'] = "CONST"
		парам['слова'] = сам.слова_модуля
		конст = тКонстанты(парам)
		сам.__конст = конст.слова_секции
		сам.слова_модуля = {}
		сам.слова_модуля = конст.слова_модуля

		парам['секция'] = "TYPE"
		парам['слова'] = сам.слова_модуля
		типы = тТипы(парам)
		сам.__типы = типы.слова_секции
		сам.слова_модуля = {}
		сам.слова_модуля = типы.слова_модуля

		парам['секция'] = "VAR"
		парам['слова'] = сам.слова_модуля
		перем = тПеременные(парам)
		сам.__перем = перем.слова_секции
		сам.слова_модуля = {}
		сам.слова_модуля = перем.слова_модуля

		парам['секция'] = "PROCEDURE"
		парам['слова'] = сам.слова_модуля
		процедуры =тПроцедуры(парам)
		сам.__проц = процедуры.слова_секции
		сам.слова_модуля = {}
		сам.слова_модуля = процедуры.слова_секции

		сам.__начало = процедуры.слова_модуля

	def __Обработать(сам):
		сам.Модуль_Контроль()
		#сам.Слова_Печать()
		сам.Секции_Разбить()

	@property
	def имя(сам):
		return сам.__имя

	def __СловаМодуля_Обрезать(сам):
		"""
		Уменьшает слова секции на 1 с головы.
		"""
		новый_список = {}
		for ключ in range(1, len(сам.слова_модуля)):
			новый_список[ключ-1]=сам.слова_модуля[ключ]
		сам.слова_модуля = {}
		сам.слова_модуля = новый_список
