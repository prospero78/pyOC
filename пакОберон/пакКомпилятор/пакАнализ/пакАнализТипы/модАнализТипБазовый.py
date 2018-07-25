# coding:utf8
"""
Содержит базовый тип для всех родов записей
"""

if True:
	from пакОберон.пакКомпилятор.пакСущность.пакСлово import тСлово
	from пакОберон.пакКомпилятор.пакСущность.пакРод import тРод

class тАнализТипБазовый:
	def __init__(сам, пДанные):
		def Слова_Проверить():
			бУсл = type(пДанные['слова']) == dict
			стрОш = "тАнализТипБазовый: В секцию  должен передаваться словарь слов, type=" + str(type(пДанные['слова']))
			assert бУсл, стрОш
			бУсл = пДанные['секция'] == "анализ"
			assert бУсл, "тАнализТипБазовый: ошибочное использование типа в секции анализа, секция=" + пДанные['секция']

		Слова_Проверить()
		сам.слова_секции = пДанные['слова']
		сам.__имя = "" # имя типа
		сам.__бЭкспорт = False # Признак экспорта типа
		сам.__бСсылка_бПрисвоено = False # Защёлка присвоения ссылки
		сам.__бСсылка = False
		сам.__предок = ""
		сам.элем = "" # Нужно для распознавания массива

	def Ошибка_Печать(сам, пСлово, пСообщ):
		строка_исх = сам.__корень.исх.строки(пСлово.коорд.стр)
		сам.консоль.Печать(сам.__корень.исх.строки(пСлово.коорд.стр))
		сам.ошибка.Коорд(пСообщ, пСлово.коорд, пСлово.строка)

	def Имя_Проверить(сам):
		"""
		Проверяет имя типа, должно быть простым.
		"""
		слово_имя = сам.слова_секции[0]
		имя = слово_имя.Проверить()
		print("тАнализТипБазовый: 5581 Имя типа=", имя, слово_имя.стрИсх)
		if слово_имя.ЕслиИмя_Строго():
			сам.__имя = имя
			сам.СловаСекции_Обрезать()
		else:
			assert False, "тАнализТипБазовый: 7780 имя типа недопустимо="+имя+слово_имя.стрИсх

	def __Род_Проверить(сам):
		"""
		Устанавливает род типа:
		1. Алиас встроенного типа
		2. Массив
		3. Запись
		4. Указатель
		5. Процедура
		Обрезать слова секции нельзя. Иначе потом не узнаем
		какой тип алиаса используется.
		"""
		тип_встроен = ["BOOLEAN", "CHAR", "INTEGER", "REAL", "BYTE", "SET"]
		строка_род = сам.Слово_Проверить()
		if строка_род in тип_встроен:
			сам.__род = тРод.сВстроен
		elif строка_род == "ARRAY":
			сам.__род = тРод.сМассив
		elif строка_род == "RECORD":
			сам.__род = тРод.сЗапись
		elif строка_род == "POINTER":
			сам.__род = тРод.сУказатель
		elif строка_род == "PROCEDURE":
			сам.__род = тРод.сПроцедура
		else:
			assert False, "тАнализТипБазовый: Неизвестный род типа, род="+строка_род

	def СловаСекции_Обрезать(сам):
		"""
		Уменьшает слова секции на 1 с головы.
		"""
		новый_список = {}
		for ключ in range(1, len(сам.слова_секции)):
			новый_список[ключ-1]=сам.слова_секции[ключ]
		сам.слова_секции = {}
		сам.слова_секции = новый_список

	def Предок_Проверить(сам):
		"""
		Проверяет предка типа. Должно быть разрешённой строкой
		Кроме того, имя может быть составным
		У полей два разделителя -- ";" или ")"
		===== Улучшенная проверенная версия =======
		"""
		слово_имя = сам.слова_секции[0]
		имя = слово_имя.Проверить()
		стрОш = "тТипБазовый: имя типа должно быть допустимым именем"
		assert слово_имя.ЕслиСтр_Допустимо(), стрОш + слово_имя.строка + слово_имя.стрИсх
		if сам.__предок != "":
			assert False, "тАнализТипБазовый: элемент массива уже назначен  " + сам.элем + слово_имя.стрИсх
		сам.__предок = ""
		while (имя == ".") or (слово_имя.ЕслиСтр_Допустимо()):
			сам.СловаСекции_Обрезать()
			сам.__предок += имя
			слово_имя = сам.слова_секции[0]
			имя = слово_имя.Проверить()
			 # Такое может быть в определении 1) массива 2) предка записи
			if имя == ";" or имя ==")":
				break
			if not (слово_имя.ЕслиСтр_Допустимо() or имя=="."):
				assert False, стрОш + слово_имя.строка + слово_имя.стрИсх

	def Определитель_Проверить(сам):
		"""
		Проверяет является ли слово в начале слов секции типа -- "=".
		После обрезания, должно быть первым.
		"""
		слово_опр = сам.слова_секции[0]
		строка_опр = слово_опр.Проверить()
		if слово_опр.род == тСлово.кРавно: # правильное выражение определения типа
			сам.СловаСекции_Обрезать()
		else: # если определение типа
			assert False, "тАнализТипБазовый: 0906 Отсутствует определитель \"=\" в объявлении типа" + слово_опр.стрИсх

	def Разделитель_Обрезать(сам):
		"""
		В типах последнее слово ";"
		Поэтому его необходимо обрезать
		"""
		слово_раздел = сам.слова_секции[0]
		if слово_раздел.род == тСлово.кТочкаЗапятая:
			сам.СловаСекции_Обрезать()
		else:
			# В типе всегда есть разделитель в конце
			assert False, "тТипБазовый: неправильный разделитель типа" + слово_раздел.стрИсх

	def Имя_Уст(сам, пИмя):
		"""
		Устанавливает имя с проверкой.
		Разрешаетися устанавливать один раз.
		Процедура с защёлкой.
		"""
		assert type(пИмя) == str, "тАнализТипБазовый: пИмя должен быть str, type=" + str(type(пИмя))
		assert пИмя != "", "тАнализТипБазовый: пИмя не может быть пустым"
		assert сам.__имя == "", "тАнализТипБазовый: имя уже присвоено, имя=" + сам.__имя
		сам.__имя = пИмя

	def бЭкспорт_Проверить(сам):
		"""
		Проверяет является ли тип экспортируемым.
		"""
		слово_экспорт = сам.слова_секции[0]
		строка_экспорт = слово_экспорт.Проверить()
		if строка_экспорт == "*": # есть экспорт
			сам.СловаСекции_Обрезать()
			сам.__бЭкспорт = True
		elif строка_экспорт == "=":
			pass # это определение типа
		else:
			assert False, "тАнализТипБазовый: 0909 Символ экспорта допустим '*' или '='" + слово_экспорт.стрИсх
		print("тАнализТипБазовый: 0908 экспорт типа=", сам.__бЭкспорт)

	def бУказатель_Проверить(сам):
		"""
		Проверяет наличие POINTER TO
		Если тип является указателем, то устанавливается соответствующий признак.
		Иначе, просто пропускается.
		"""
		слово_указ = сам.слова_секции[0]
		строка_указ = слово_указ.Проверить()
		if строка_указ == "POINTER": # модификатор типа, а не сам тип
			print("тАнализТип: 5578 указатель=", слово_указ.строка)
			сам.СловаСекции_Обрезать()
			"""
			======== Проверяет, что после POINTER __ОБЯЗАТЕЛЬНО__ TO ==========
			"""
			слово_из = сам.слова_секции[0]
			строка_из = слово_из.Проверить()
			assert строка_из == "TO", "тАнализТип: за POINTER не следует TO" + слово_из.стрИсх
			print("тАнализТип: 5579 указатель-2 =", слово_из.строка)
			сам.СловаСекции_Обрезать()
			сам.__бУказатель = True
		else:
			сам.__бУказатель = False # Обязательно принудительно сбросить. Временный признак

	def бЭксорт_Уст(сам, пЭкспорт):
		"""
		Устанавливает экспорт с проверкой.
		Разрешаетися устанавливать один раз.
		Процедура с защёлкой.
		"""
		assert type(пЭкспорт) == BOOLEAN, "тАнализТипБазовый: пЭкспорт должен быть BOOLEAN, type=" + str(type(пЭкспорт))
		assert сам.__бЭкспорт_бПрисвоено == False, "тАнализТипБазовый: пЭкспорт уже присвоен, экспорт=" + сам.__бЭкспорт
		сам.__бЭкспорт_бПрисвоено = True
		сам.__бЭкспорт = пЭкспорт

	@property
	def бЭкспорт(сам):
		return сам.__бЭкспорт

	def бСсылка_Уст(сам, пСсылка):
		"""
		Устанавливает ссылку с проверкой.
		Разрешаетися устанавливать один раз.
		Процедура с защёлкой.
		"""
		assert type(пСсылка) == bool, "тАнализТипБазовый: пСсылка должен быть BOOLEAN, type=" + str(type(пСсылка))
		assert сам.__бСсылка_бПрисвоено == False, "тАнализТипБазовый: пСсылка уже присвоен, экспорт=" + сам.__бСсылка
		сам.__бСсылка_бПрисвоено = True
		сам.__бСсылка = пСсылка

	@property
	def бСсылка(сам):
		return сам.__бСсылка

	def Предок_Уст(сам, пПредок):
		"""
		Устанавливает имя с проверкой.
		Разрешаетися устанавливать один раз.
		Процедура с защёлкой.
		"""
		assert type(пПредок) == str, "тАнализТипБазовый: пПредок должен быть str, type=" + str(type(пПредок))
		if пПредок == "":
			assert False, "тАнализТипБазовый: пПредок не может быть пустым"
		assert сам.__предок == "", "тАнализТипБазовый: имя уже присвоено, имя=" + сам.__предок
		сам.__предок = пПредок

	@property
	def предок(сам):
		return сам.__предок

	@property
	def имя(сам):
		return сам.__имя
