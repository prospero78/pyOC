# coding: utf8
"""
Модуль предоставляет тип слова для построения AST.
Настройка пакета слов.
Слово -- кусочек текста в исходнике.
Обладает несколькими свойствами:
1. Литеры (само слово)
2. Координаты.
3. Строка, в которой он находится.
"""

from пакКомпилер.пакИсходник.модКоордФикс import тКоордФикс

class тСлово:
	"""
	Тип тСлово описывает слово, как отдельную сущность в составе исходного
	текста, обладает различными атрибутами.
	"""
	кПусто = 0
	кМодульИмя   = кПусто + 1
	кМодульАлиас = кМодульИмя   + 1
	кЗапятая     = кМодульАлиас + 1
	кТочкаЗапятая= кЗапятая + 1
	кИмя         = кТочкаЗапятая + 1
	кКомментНачать=кИмя   + 1
	кКомментЗакончить=кКомментНачать + 1
	кОпределить  = кКомментЗакончить + 1
	кПрисвоить   = кОпределить  + 1
	кСкобкаОткрКругл=кПрисвоить + 1
	кСкобкаЗакрКругл=кСкобкаОткрКругл + 1
	кДеление     = кСкобкаЗакрКругл   + 1
	кУмножить    = кДеление + 1
	кМинус       = кУмножить+ 1
	кПлюс        = кМинус   + 1
	кЧисло       = кПлюс    + 1
	кСтрока      = кЧисло   + 1
	кСравнитьРавно=кСтрока  + 1
	кТочка       = кСравнитьРавно + 1
	запр_имя     = ["MODULE", "IMPORT", "CONST", "TYPE", "BOOLEAN", "BYTE", \
							"INTEGER", "CHAR", "SET", "REAL", "VAR", "POINTER", "TO", \
							"ARRAY", "OF", "BEGIN", "END", "PROCEDURE", "FOR", \
							"WHILE", "DO", "RECORD" ]
	def __init__(сам, пИсх, пСтрока):
		def пСлово_Проверить():
			бУсл = type(пСтрока) == str
			стрСообщ = "тСлово.__init__(): пСтрока должно быть строкой, type(пСтрока)="+str(type(пСтрока))
			сам.__корень.конс.Проверить(бУсл, стрСообщ)

			бУсл = len(пСтрока) > 0
			стрСообщ = "тСлово.__init__(): пСтрока не может быть пустыми"
			сам.__корень.конс.Проверить(бУсл, стрСообщ)
		def Род_Проверить():
			"""
			Устанавливает род слова.
			"""
			if пСтрока == ";":
				сам.__род = тСлово.кТочкаЗапятая
			elif пСтрока == ",":
				сам.__род = тСлово.кЗапятая
			elif пСтрока == "+":
				сам.__род = тСлово.кПлюс
			elif пСтрока == "+":
				сам.__род = тСлово.кПлюс
			elif пСтрока == "-":
				сам.__род = тСлово.кМинус
			elif пСтрока == "/":
				сам.__род = тСлово.кДеление
			elif пСтрока == "(":
				сам.__род = тСлово.кСкобкаОткрКругл
			elif пСтрока == "(*":
				сам.__род = тСлово.кКомментНачать
			elif пСтрока == ")":
				сам.__род = тСлово.кСкобкаЗакрКругл
			elif пСтрока == "*)":
				сам.__род = тСлово.кКомментЗакончить
			elif пСтрока == "*":
				сам.__род = тСлово.кУмножить
			elif пСтрока == ":=":
				сам.__род = тСлово.кПрисвоить
			elif пСтрока == ":":
				сам.__род =  тСлово.кОпределить
			elif пСтрока[0]=="_" or пСтрока[0].isalpha():
				сам.__род =  тСлово.кИмя
			elif пСтрока[0].isdigit() or пСтрока[0] == ".":
				сам.__род =  тСлово.кЧисло
			elif пСтрока == "=":
				сам.__род =  тСлово.кСравнитьРавно
			elif пСтрока == ".":
				сам.__род =  тСлово.кТочка
			elif пСтрока[0] == '"' and пСтрока[-1] == '"':
				сам.__род =  тСлово.кСтрока
			else:
				сам.__корень.конс.Ошибка("Не могу классифицировать строку, строка="+пСтрока)

		сам.__исх = пИсх
		сам.__корень = пИсх.корень
		сам.__род = "" # род слова
		сам.конс = сам.__корень.конс

		пСлово_Проверить()
		сам.__стрСтрока = пСтрока
		Род_Проверить()

		сам.__номер = пИсх.цСловаВсего

		сам.коорд = тКоордФикс(сам.__корень, пИсх.коорд.цСтр, пИсх.коорд.цПоз)

		сам.__стрИсх = пИсх.строки(пИсх.коорд.цСтр)

	@property
	def стрИсх(сам):
		"""
		Возвращает строку исходника, где это слово
		"""
		assert сам.__стрИсх != "", "Строка исходника не может быть пустой"
		стр_ном=str(сам.коорд.цСтр)
		while len(стр_ном) < 4:
			стр_ном = " " + стр_ном
		стр_указ = (len(стр_ном)+1) * "-" + "-" * сам.коорд.цПоз + "^"
		return "\n" + стр_ном + " " + сам.__стрИсх + "\n" + стр_указ

	@property
	def строка(сам):
		"""
		Возвращает строку слова
		"""
		return сам.__стрСтрока

	@property
	def номер(сам):
		"""
		Возвращает порядковый номер слова в исходнике.
		"""
		return сам.__номер

	def _Номер_Уст(сам, пцСлово):
		бУсл = type(пцСлово) == int
		стрОш = "тСлово.__init__(): пцСлово должен быть целым, type(пцСлово)="+str(type(пцСлово))
		сам.__корень.конс.Проверить(бУсл, стрОш)

		бУсл = пцСлово >= 0
		стрОш = "тСлово.__init__(): пцСлово должен быть равен или больше 0, пцСлово="+str(пцСлово)
		сам.__корень.конс.Проверить(бУсл, стрОш)

		сам.__номер = пцСлово

	def ЕслиСтр_Допустимо(сам):
		"""
		Проверяет на допустимость строки, первая литера должна быть "_" или буква.
		1) без специальных символов.
		2) без точки
		3) цифры разрешены
		4) ключевые слова разрешены
		"""
		бВыход = False
		if сам.__стрСтрока[0]=="_" or сам.__стрСтрока[0].isalpha():
			for лит in сам.__стрСтрока:
					# Точка в имени -- допустимо, но здесь её не будет.
					if not (лит in ".~`!@$%^&*()-_=+{}[]|\\<,>?/\"№;:/"):
						бВыход = True
						break
		return бВыход

	def ЕслиИмя_Строго(сам):
		'''
		Проверяет на допустимость литер в слове для обнаружения имени сущности.
		Не допускает зарезервированные слова.
		1) без специаяльных символов
		2) точка разрешена
		3) цифры разрешены
		4) ключевые слова запрещены
		'''
		# имя сущности должно начинаться либо с "_", либо с буквы
		бВыход = False
		if сам.__стрСтрока[0]=="_" or сам.__стрСтрока[0].isalpha():
			if not (сам.__стрСтрока) in тСлово.запр_имя:
				for лит in сам.__стрСтрока:
					# Точка в имени -- допустимо, но здесь её не будет.
					if not (лит in "~`!@$%^&*()-_=+{}[]|\\<,>?/\"№;:/"):
						бВыход = True
						break
		return бВыход

	def __str__(сам):
		стрСлово = сам.__стрСтрока
		while len(стрСлово) < 7:
			стрСлово = " " + стрСлово
		return str(сам.__номер)+"\tслово="+ стрСлово + "\t" + str(сам.коорд)
