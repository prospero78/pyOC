# coding:utf8
"""
Модуль описывает поле ранее описанного типа в составе записи.
"""
if True:
	from ..пакСлово import тСлово
	from пакОберон.пакКомпилятор.пакСущность.пакРод import тРод
	from . модПолеВстроен import тПолеВстроен
	from . модПолеМассив import тПолеМассив
	from . модПолеЗапись import тПолеЗапись
	from . модПолеБаза import тПолеБаза

class тПоле(тПолеБаза):
	def __init__(сам, пОберон, пДанные):
		сам.__конс = пОберон.конс

		сам.__бОшВнутр = False
		сам.__бОшИсх = False

		тПолеБаза.__init__(сам, пОберон, пДанные)
		if сам.бОшВнутр_ПолеБаза:
			сам.__бОшВнутр = True
			стрОш = "тПоле.__init__(): ошибка компилятора. При вызове тПолеБаза"
			сам.__конс.ОшВнутр(стрОш)
			return
		if сам.бОшИсх_ПолеБаза:
			сам.__бОшИсх = True
			стрОш = "тПоле.__init__(): ошибка исходника. При вызове тПолеБаза"
			сам.__конс.Ошибка(стрОш)
			return
		сам.поля ={} # если вдруг поле окажется составным
		сам.массив_размерность = {} # размерность массива поля (если поле массив)
		сам.массив_тип = тРод.сБезТипа # Тип элемента массива])
		сам.__индекс = 0 # не будем обрезать поля, пусть этим занимаются сами поля
		print("тПоле:_", сам.слова_секции[0].стрИсх)
		сам.__Имя_Проверить()
		сам.__Экспорт_Проверить()
		сам.__Двоеточие_Проверить()
		сам.__Род_Проверить()
		#сам.__Разделитель_Обрезать()

	def __Имя_Проверить(сам):
		"""
		Получает имя поля.
		"""
		слово_имя = сам.слова_секции[сам.__индекс]
		имя = слово_имя.строка
		if слово_имя.ЕслиИмя_Строго():
			#сам.Имя_Уст(имя)
			#сам.СловаСекции_Обрезать()
			сам.__индекс += 1
		else:
			сам.__бОшИсх = True
			стрОш = "тПоле: имя поля должно быть допустимым именем" + слово_имя.стрИсх
			сам.__конс.Ошибка(стрОш)
			return

	def __Экспорт_Проверить(сам):
		"""
		Проверяет является ли поле экспортируемым.
		"""
		слово_экспорт = сам.слова_секции[сам.__индекс]
		строка_экспорт = слово_экспорт.строка
		if строка_экспорт == "*": # есть экспорт
			#сам.СловаСекции_Обрезать()
			сам.__индекс += 1
			#сам.__бЭкспорт_Уст(True)
		elif строка_экспорт == ":":
			pass # это определение поля
		else:
			сам.__бОшИсх = True
			стрОш = "тПоле: Символ экспорта допустим '*' или '='" + слово_экспорт.стрИсх
			сам.__конс.Ошибка(стрОш)

	def __Двоеточие_Проверить(сам):
		"""
		Здесь может быть только ":"
		"""
		слово_двоеточ = сам.слова_секции[сам.__индекс]
		строка_двоеточ = слово_двоеточ.строка
		if строка_двоеточ == ":": # есть двоеточие
			#сам.СловаСекции_Обрезать()
			сам.__индекс += 1
		else: # а это уже непонятно что
			сам.__бОшИсх = True
			стрОш = "тПоле: разделитель должна быть ':'" + слово_двоеточ.стрИсх
			сам.__конс.Ошибка(стрОш)
			return

	def __Род_Проверить(сам):
			"""
			Пытается вычислить поле в простой записи.
			слово тип может быть как встроенным, так и определяемое пользователем.
			"""
			слово_тип = сам.слова_секции[0]
			строка_тип = слово_тип.строка
			парам = {}
			парам['секция'] = "VAR"
			парам['слова'] = сам.слова_секции
			парам['имя'] =сам.имя
			парам['бЭкспорт'] = сам.бЭкспорт
			if строка_тип in тРод.тип_встроен:
				сам.__ПредокВстроен_Проверить()
			elif строка_тип == "ARRAY":
				поле = тПолеМассив(парам)
			elif строка_тип == "RECORD":
				поле = тПолеЗапись(парам)
			elif слово_тип.ЕслиСтр_Допустимо() and (строка_тип != "END"):
				# если пользовательский тип
				сам.Предок_Проверить()

	def __ПредокВстроен_Проверить(сам):
		слово_тип = сам.слова_секции[0]
		строка_тип = слово_тип.Проверить()
		if not слово_тип.ЕслиСтр_Допустимо():
			сам.__бОшВнутр = True
			стрОш = "тПоле: тип поля должен быть разрешённым именем" + слово_тип.стрИсх
			сам.__конс.ОшВнутр(стрОш)
			return
		#assert строка_тип != "END", "тПоле: тип поля не можеть быть 'END', тип=" + строка_тип
		if строка_тип == "BOOLEAN":
			сам.Предок_Уст("BOOLEAN")
		elif строка_тип == "CHAR":
			сам.Предок_Уст("CHAR")
		elif строка_тип == "INTEGER":
			сам.Предок_Уст("INTEGER")
		elif строка_тип == "REAL":
			сам.Предок_Уст("REAL")
		elif строка_тип == "BYTE":
			ссам.Предок_Уст("BYTE")
		elif строка_тип == "SET":
			сам.Предок_Уст("SET")
		else:
			сам.__бОшИсх = True
			стрОш = "тПолеВстроен: Неверный встроенный тип" + слово_тип.стрИсх
			сам.__конс.Ошибка(стрОш)
			return
		сам.СловаСекции_Обрезать()

	def Поля_Проверить(сам, пПолеЗапись):
		"""
		В записях ВСЕГДА встречается окончание "END" даже без
		вложенных полей.
		Поэтому здесь проверяем в цикле все поля, пока не закончатся
		Здесь подполям передаётся ссылка НА ЭТО поле
		Процедура помещена сюда, так как по другому получается
		циклический импорт.
		"""
		слово_конец = сам.секция.слова_секции[0]
		строка_конец = слово_конец.Проверить()
		# если типы не встроенные (у встроенных типов нет полей)
		while строка_конец != "END": # нет окончания описания типа
			поле = тПоле(сам.секция, сам)
			сам.поля[len(сам.поля)] = поле
			слово_конец = сам.секция.слова_секции[0]
			строка_конец = слово_конец.Проверить()

	def Паспорт_Печать(сам):
		сам.__конс.Печать("       Поле: ", сам.__имя)
		сам.__конс.Печать("         экспорт= ", сам.__бЭкспорт)
		м("      указатель =", сам.__бУказатель)
		сам.__конс.Печать("           тип  =", сам.__тип)
		if сам.__тип == тРод.сМассив:
			for ключ in range(0, len(сам.массив_размерность)):
				сам.__конс.Печать("          ключ ", ключ, ":",сам.массив_размерность[ключ])
			сам.__конс.Печать("          элем    =", сам.массив_тип)
		if сам.__тип == тРод.сЗапись:
			сам.__конс.Печать("Поля:")
			for ключ in сам.поля:
				сам.поля[ключ].Паспорт_Печать()
		сам.__конс.Печать()

	@property
	def бОшВнутр(сам):
		return сам.__бОшВнутр

	@property
	def бОшИсх(сам):
		return сам.__бОшИсх
