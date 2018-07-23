# coding: utf8
"""
Модуль предоставляет класс для разбора типа.
Простой тип может содержать определения других подтипов и членов.
"""

if True:
	from пакОберон.пакКомпилятор.пакСущность.пакСлово import тСлово
	from пакОберон.пакКомпилятор.пакСущность.пакРод import тРод

	from . модАнализТипВстроен import тАнализТипВстроен
	from . модАнализТипМассив import тАнализТипМассив
	from . модАнализТипЗапись import тАнализТипЗапись
	from . модАнализТипПроцедура import тАнализТипПроцедура

	#from пакКомпилер.пакМодуль.пакПоле.модПоле import тПоле
	from .модАнализТипБазовый import тАнализТипБазовый

class тАнализТип(тАнализТипБазовый):
	def __init__(сам, пДанные):
		тАнализТипБазовый.__init__(сам, пДанные)
		сам.__род = тРод.сБезРода # Род записи -- один из встроенных, ARRAY, RECORD, PROCEDURE
		сам.__предок = тРод.сБезТипа # Тип предка -- один из наследуемых
		сам.__имя = "" # Временная переменная
		сам.__бУказатель = False # временный признак POINTER TO
		сам.__бЭкспорт = False # Временное хранение экспорта
		сам.массив_тип = тРод.сБезТипа # устанавливает тип массива (если тип -- массив)
		сам.поля = {} # словарь полей типа
		сам.__тип = None # ссылка на полученный тип
		assert len(сам.слова_секции) >= 2, "тАнализТип: Неполное определение секции"
		сам.массив_размерность = {} # заполняется при определении массива
		сам.запись_поля = {} # словарь полей типа RECORD
		сам.__Имя_Проверить()
		сам.__Экспорт_Проверить()
		сам.__Определитель_Проверить()
		сам.__Указатель_Проверить()
		сам.__Род_Проверить()

	def __Имя_Проверить(сам):
		"""
		Проверяет имя типа. Должно быть именем и
		не должно быть END.
		Имя НЕ МОЖЕТ быть составным
		"""
		бРезульт = False
		слово_имя = сам.слова_секции[0]
		print("тАнализТип: имя типа=", слово_имя.строка)
		имя = слово_имя.Проверить()
		if слово_имя.ЕслиИмя_Строго():
			сам.СловаСекции_Обрезать()
			сам.__имя = имя
			бРезульт = True
		else:
			assert False, "тАнализТип: имя типа должно быть допустимым именем" + слово_имя.стрИсх

	def __Экспорт_Проверить(сам):
		"""
		Проверяет является ли тип экспортируемым.
		"""
		слово_экспорт = сам.слова_секции[0]
		print("тАнализТип: экспорт типа=", слово_экспорт.строка)
		строка_экспорт = слово_экспорт.Проверить()
		if строка_экспорт == "*": # есть экспорт
			сам.СловаСекции_Обрезать()
			сам.__бЭкспорт = True
		elif строка_экспорт == "=":
			pass # это определение типа
		else:
			assert False, "тАнализТип: Символ экспорта допустим '*' или '='" + слово_экспорт.стрИсх

	def __Определитель_Проверить(сам):
		"""
		Проверяет является ли слово в начале слов секции типа -- "=".
		После обрезания, должно быть первым.
		"""
		слово_опр = сам.слова_секции[0]
		строка_опр = слово_опр.Проверить()
		if слово_опр.род == тСлово.кРавно: # правильное выражение определения типа
			сам.СловаСекции_Обрезать()
		else: # если определение типа
			assert False, "тАнализТип: Отсутствует определитель \"=\" в объявлении типа" + слово_опр.стрИсх

	def __Указатель_Проверить(сам):
		"""
		Проверяет наличие POINTER TO
		Если тип является указателем, то устанавливается соответствующий признак.
		Иначе, просто пропускается.
		"""
		слово_указ = сам.слова_секции[0]
		строка_указ = слово_указ.Проверить()
		if строка_указ == "POINTER": # модификатор типа, а не сам тип
			сам.СловаСекции_Обрезать()
			"""
			======== Проверяет, что после POINTER __ОБЯЗАТЕЛЬНО__ TO ==========
			"""
			слово_из = сам.слова_секции[0]
			строка_из = слово_из.Проверить()
			assert строка_из == "TO", "тАнализТип: за POINTER не следует TO" + слово_из.стрИсх
			сам.СловаСекции_Обрезать()
			сам.__бУказатель = True
		else:
			сам.__бУказатель = False # Обязательно принудительно сбросить. Временный признак

	def __ЧастныйПредок_Проверить(сам, пСлово):
		"""
		Проверяет предка записи. Должно быть разрешённой строкой и
		НЕ ДОЛЖНО быть END.
		Кроме того, имя может быть составным
		"""
		# пСлово уже обрезано при рассмотрении типа
		assert type(пСлово) == тСлово, "тАнализТип: пСлово должно быть тСлово, type="+str(type(пСлово))
		стрОш = "тАнализТип: имя типа должно быть допустимым именем"
		assert пСлово.ЕслиСтр_Допустимо(), стрОш + пСлово.строка + пСлово.стрИсх
		assert сам.__предок == тРод.сБезТипа, "тАнализТип: предок уже назначен, предок=" + сам.__предок+ слово_имя.стрИсх
		сам.__предок = ""
		имя = пСлово.Проверить()
		# так как это слово уже обрезано -- пропускаем обрезание словаря
		if (имя == ".") or (пСлово.ЕслиСтр_Допустимо()):
			сам.__предок += имя
			слово_имя = сам.слова_секции[0]
			имя = слово_имя.Проверить()
			бРезульт = True
			сам.СловаСекции_Обрезать()

		слово_имя = сам.слова_секции[0]
		имя = слово_имя.Проверить()
		# проверить до конца имя типа
		while (имя == ".") or (слово_имя.ЕслиСтр_Допустимо()):
			сам.СловаСекции_Обрезать()
			сам.__предок += имя
			слово_имя = сам.слова_секции[0]
			имя = слово_имя.Проверить()
			бРезульт = True
		# теперь надо обрезать окончание типа
		сам.__Разделитель_Обрезать()

	def Элемент_Проверить(сам, пПоле):
		"""
		Проверяет предка записи. Должно быть разрешённой строкой и
		не должно быть END.
		Кроме того, имя может быть составным
		"""
		слово_имя = сам.слова_секции[0]
		имя = слово_имя.Проверить()
		стрОш = "тАнализТип: тип элемента переменной должен быть допустимым именем"
		assert слово_имя.ЕслиСтр_Допустимо(), стрОш + слово_имя.стрИсх
		assert сам.массив_тип == тРод.сБезТипа, "тАнализТип: элемент массива уже назначен, элемент=" + сам.массив_тип
		элемент = ""
		while (имя == ".") or (слово_имя.ЕслиСтр_Допустимо()):
			сам.СловаСекции_Обрезать()
			элемент += имя
			слово_имя = сам.слова_секции[0]
			имя = слово_имя.Проверить()
		return элемент

	def __Род_Проверить(сам):
		"""
		Проверяет род встреченного типа. Возможны варианты:
		1. Алиас встроенного типа.

		2.Массив чего-либо

		3. Пустая запись, должна заканчиваться "END;" (просто запись без членов -- бесполезна,
			но для расширения в шине сообщений -- бывает может пригодиться), скорей всего с
			множеством полей.

		4. Запись с полями, множественные уровни вложенности. Рекурсивный анализ.
			Заканчивается на "END;", но после слова "RECORD" идёт не "END"

		5. ....
		"""

		парам = {}
		парам['секция']  = "анализ"
		парам['слова']   = сам.слова_секции

		print("тАнализТип: Длина секции типов =", len(сам.слова_секции))
		слово_тип = сам.слова_секции[0]
		строка_род = слово_тип.Проверить()
		# тип не может начинаться на "." или цифру, или спецсимвол
		assert слово_тип.ЕслиСтр_Допустимо(), "тАнализТип: род типа должен быть допустимым именем" + слово_тип.стрИсх
		if строка_род in тРод.тип_встроен: # текущий тип основан на встроенном типе
			print("тАнализТип.род = Тип встроенный", слово_тип.стрИсх)
			сам.__тип = тАнализТипВстроен(парам)
			сам.Предок_Уст(сам.__тип.предок)
		elif строка_род == тРод.сМассив: # текущий тип основан на массиве
			print ("тАнализТип.род = Тип массив", слово_тип.стрИсх)
			сам.__тип = тАнализТипМассив(парам)
		elif строка_род == тРод.сМассив: # текущий тип основан на записе
			print("тАнализТип.род = Тип запись", слово_тип.стрИсх)
			сам.__тип = тАнализТипЗапись(парам)
		elif строка_род == "PROCEDURE": # текущий тип основан на процедуре
			print("тАнализТип.род = Тип процедура", слово_тип.стрИсх)
			сам.__тип = тАнализТипПроцедура(парам)
		elif слово_тип.ЕслиСтр_Допустимо(): # Пользовательский тип
			print("тАнализТип.род = Тип частный", слово_тип.стрИсх)
			сам.__ЧастныйПредок_Проверить(слово_тип)
		else:
			assert False, "тАнализТип: неизвестный тип записи" + слово_тип.стрИсх
		if сам.__тип != None:
			сам.слова_секции = {}
			сам.слова_секции = сам.__тип.слова_секции

	def __Разделитель_Обрезать(сам):
		"""
		В простых типах последнее слово ";"
		Поэтому его необходимо обрезать
		"""
		слово_раздел = сам.слова_секции[0]
		if слово_раздел.род == тСлово.кТочкаЗапятая:
			сам.СловаСекции_Обрезать()
		else:
			assert False, "тАнализТип: неправильный разделитель типа \";\"" + слово_раздел.стрИсх

	def СловаСекции_Обрезать(сам):
		"""
		Уменьшает слова секции на 1 с головы.
		"""
		новый_список = {}
		for ключ in range(1, len(сам.слова_секции)):
			новый_список[ключ-1]=сам.слова_секции[ключ]
		сам.слова_секции = {}
		сам.слова_секции = новый_список

	@property
	def бЭкспорт(сам):
		return сам.__бЭкспорт

	@property
	def имя(сам):
		return сам.__имя

	@property
	def предок(сам):
		return сам.__предок

	def Паспорт_Печать(сам):
		print("+ тАнализТип: имя_типа=", сам.имя)
		print("|      экспорт =", сам.__бЭкспорт)
		print("|    указатель =", сам.__бУказатель)
		print("|       предок =", сам.__предок)
		if сам.__предок == тРод.сМассив:
			for ключ in range(len(сам.массив_размерность)):
				print("|      ключ ", ключ, ":",сам.массив_размерность[ключ])
			print("|      элем    =", сам.массив_тип)
		elif сам.__предок == тРод.сЗапись:
			for ключ in range(len(сам.запись_поля)):
				сам.запись.поля[ключ].Паспорт_Печать()
		print("+" + "-"*35+"\n")
