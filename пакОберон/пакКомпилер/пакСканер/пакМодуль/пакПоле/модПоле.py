# coding:utf8
"""
Модуль описывает поле ранее описанного типа в составе записи.
"""
if True:
	from ...пакСлово import тСлово
	from ..пакСекции.пакТипы.модРод import тРод
	from . модПолеМассив import тПолеМассив
	from . модПолеЗапись import тПолеЗапись
	from . модПолеБаза import тПолеБаза

class тПоле(тПолеБаза):
	def __init__(сам, пДанные):
		тПолеБаза.__init__(сам, пДанные)
		сам.поля ={} # если вдруг поле окажется составным
		сам.массив_размерность = {} # размерность массива поля (если поле массив)
		сам.массив_тип = тРод.сБезТипа # Тип элемента массива])
		#сам.__Род_Проверить() # основная работа по родам полей
		сам.__Имя_Проверить()
		сам.__Экспорт_Проверить()
		сам.__Двоеточие_Обрезать()
		сам.__Род_Проверить()
		сам.__Разделитель_Обрезать()

	def __Имя_Проверить(сам):
		"""
		Получает имя поля.
		"""
		слово_имя = сам.слова_секции[0]
		print("Имя поля", слово_имя.стрИсх)
		имя = слово_имя.Проверить()
		if слово_имя.ЕслиИмя_Строго():
			сам.Имя_Уст(имя)
			сам.СловаСекции_Обрезать()
		else:
			assert False, "тПоле: имя поля должно быть допустимым именем" + слово_имя.стрИсх

	def __Экспорт_Проверить(сам):
		"""
		Проверяет является ли поле экспортируемым.
		"""
		слово_экспорт = сам.слова_секции[0]
		строка_экспорт = слово_экспорт.Проверить()
		if строка_экспорт == "*": # есть экспорт
			сам.СловаСекции_Обрезать()
			сам.__бЭкспорт_Уст(True)
		elif строка_экспорт == ":":
			pass # это определение поля
		else:
			assert False, "тПолеБаза: Символ экспорта допустим '*' или '='" + слово_экспорт.стрИсх

	def __Двоеточие_Обрезать(сам):
		"""
		Здесь может быть только ":"
		"""
		слово_двоеточ = сам.слова_секции[0]
		строка_двоеточ = слово_двоеточ.Проверить()
		if строка_двоеточ == ":": # есть двоеточие
			сам.СловаСекции_Обрезать()
		else: # а это уже непонятно что
			assert False, "тПолеБаза: разделитель должна быть ':'" + слово_двоеточ.стрИсх

	def __Разделитель_Обрезать(сам):
		"""
		В полях может и не встречаться как разделитель ";", так и
		окончание описания типа "END"+";".
		Обработку "END" оставляем на совести типа.
		"""
		слово_раздел = сам.слова_секции[0]
		строка_раздел = слово_раздел.Проверить()
		if строка_раздел == ";": # закрытие имени предка
			сам.СловаСекции_Обрезать()

	def __Род_Проверить(сам):
			"""
			Пытается вычислить поле в простой записи.
			слово тип может быть как встроенным, так и определяемое пользователем.
			"""
			слово_тип = сам.слова_секции[0]
			строка_тип = слово_тип.Проверить()
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
		assert слово_тип.ЕслиСтр_Допустимо(), "тПоле: тип поля должен быть разрешённым именем" + слово_тип.стрИсх
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
			assert False, "тПолеВстроен: Неверный встроенный тип" + слово_тип.стрИсх
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
		print("       Поле: ", сам.__имя)
		print("         экспорт= ", сам.__бЭкспорт)
		print("      указатель =", сам.__бУказатель)
		print("           тип  =", сам.__тип)
		if сам.__тип == тРод.сМассив:
			for ключ in range(0, len(сам.массив_размерность)):
				print("          ключ ", ключ, ":",сам.массив_размерность[ключ])
			print("          элем    =", сам.массив_тип)
		if сам.__тип == тРод.сЗапись:
			print("Поля:")
			for ключ in сам.поля:
				сам.поля[ключ].Паспорт_Печать()
		print()
