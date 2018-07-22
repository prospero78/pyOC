# coding: utf8
"""
Модуль предоставляет класс для разбора типа.
Простой тип может содержать определения других подтипов и членов.
"""

if True:
	from ....пакСлово import тСлово
	from .модРод import тРод

	from . модТипВстроен import тТипВстроен
	from . модТипМассив import тТипМассив
	from . модТипЗапись import тТипЗапись

	#from пакКомпилер.пакМодуль.пакПоле.модПоле import тПоле
	from .модТипБазовый import тТипБазовый

class тТип(тТипБазовый):
	def __init__(сам, пДанные):
		тТипБазовый.__init__(сам, пДанные)
		if пДанные['секция']!="TYPE":
			assert False, "тТип: ошибочное использование типа в другой секции, секция=" + пДанные['секция']
		сам.__род = тРод.сБезРода # Род записи -- один из встроенных, ARRAY, RECORD, PROCEDURE
		сам.__врем_предок = тРод.сБезТипа # Тип предка -- один из наследуемых
		сам.__врем_имя = "" # Временная переменная
		сам.__врем_бУказ = False # временный признак POINTER TO
		сам.__врем_бЭкспорт = False # Временное хранение экспорта
		сам.массив_тип = тРод.сБезТипа # устанавливает тип массива (если тип -- массив)
		сам.поля = {} # словарь полей типа
		assert len(сам.слова_секции) >= 2, "тТип: Неполное определение секции"
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
		имя = слово_имя.Проверить()
		if слово_имя.ЕслиИмя_Строго():
			сам.СловаСекции_Обрезать()
			сам.__врем_имя = имя
			бРезульт = True
		else:
			assert False, "тТип: имя типа должно быть допустимым именем" + слово_имя.стрИсх

	def __Экспорт_Проверить(сам):
		"""
		Проверяет является ли тип экспортируемым.
		"""
		слово_экспорт = сам.слова_секции[0]
		строка_экспорт = слово_экспорт.Проверить()
		if строка_экспорт == "*": # есть экспорт
			сам.СловаСекции_Обрезать()
			сам.__врем_бЭкспорт = True
		elif строка_экспорт == "=":
			pass # это определение типа
		else:
			assert False, "тТип: Символ экспорта допустим '*' или '='" + слово_экспорт.стрИсх

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
			assert False, "тТип: Отсутствует определитель (=) в объявлении типа" + слово_опр.стрИсх

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
			assert строка_из == "TO", "тТип: за POINTER не следует TO" + слово_из.стрИсх
			сам.СловаСекции_Обрезать()
			сам.__врем_бУказ = True
		else:
			сам.__врем_бУказ = False # Обязательно принудительно сбросить. Временный признак

	def __ЧастныйПредок_Проверить(сам, пСлово):
		"""
		Проверяет предка записи. Должно быть разрешённой строкой и
		НЕ ДОЛЖНО быть END.
		Кроме того, имя может быть составным
		"""
		# пСлово уже обрезано при рассмотрении типа
		assert type(пСлово) == тСлово, "тТип: пСлово должно быть тСлово, type="+str(type(пСлово))
		стрОш = "тТип: имя типа должно быть допустимым именем"
		assert пСлово.ЕслиСтр_Допустимо(), стрОш + пСлово.строка + пСлово.стрИсх
		assert сам.__врем_предок == тРод.сБезТипа, "тТип: предок уже назначен, предок=" + сам.__врем_предок+ слово_имя.стрИсх
		сам.__врем_предок = ""
		имя = пСлово.Проверить()
		# так как это слово уже обрезано -- пропускаем обрезание словаря
		if (имя == ".") or (пСлово.ЕслиСтр_Допустимо()):
			сам.__врем_предок += имя
			слово_имя = сам.слова_секции[0]
			имя = слово_имя.Проверить()
			бРезульт = True

		# проверить до конца имя типа
		while (имя == ".") or (слово_имя.ЕслиСтр_Допустимо()):
			сам.СловаСекции_Обрезать()
			сам.__врем_предок += имя
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
		стрОш = "тПеременные: тип элемента переменной должен быть допустимым именем"
		assert слово_имя.ЕслиСтр_Допустимо(), стрОш + слово_имя.стрИсх
		assert сам.массив_тип == тРод.сБезТипа, "тТип: элемент массива уже назначен, элемент=" + сам.массив_тип
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
		парам['секция']  = "TYPE"
		парам['слова']   = сам.слова_секции
		парам['имя']     = сам.__врем_имя
		парам['бЭкспорт']= сам.__врем_бЭкспорт
		парам['бУказ']   = сам.__врем_бУказ

		слово_тип = сам.слова_секции[0]
		строка_род = слово_тип.Проверить()
		# тип не может начинаться на "." или цифру, или спецсимвол
		assert слово_тип.ЕслиСтр_Допустимо(), "тТип: род типа должен быть допустимым именем" + слово_тип.стрИсх
		if строка_род in тРод.тип_встроен: # текущий тип основан на встроенном типе
			тип = тТипВстроен(парам)
		elif строка_род == тРод.сМассив: # текущий тип основан на массиве
			тип = тТипМассив(парам)
		elif строка_род == тРод.сЗапись: # текущий тип основан на записе
			print("Тип запись", слово_тип.стрИсх)
			тип = тТипЗапись(парам)
			сам.__род = тРод.сЗапись
		elif строка_род == "PROCEDURE": # текущий тип основан на процедуре
			print("Тип процедура", слово_тип.стрИсх)
			тип = тТипПроцедура(парам)
			сам.__род = тРод.сПроцедура
		elif слово_тип.ЕслиСтр_Допустимо(): # Пользовательский тип
			print("Тип частный", слово_тип.стрИсх)
			сам.__ЧастныйПредок_Проверить(слово_тип)
			тип = сам
		else:
			assert False, "тТип: неизвестный тип записи" + слово_тип.стрИсх
		сам.слова_секции = {}
		сам.слова_секции = тип.слова_секции

	def __Разделитель_Обрезать(сам):
		"""
		В простых типах последнее слово ";"
		Поэтому его необходимо обрезать
		"""
		слово_раздел = сам.слова_секции[0]
		if слово_раздел.род == тСлово.кТочкаЗапятая:
			сам.СловаСекции_Обрезать()
		else:
			assert False, "тТип: неправильный разделитель типа" + слово_раздел.стрИсх

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
		return сам.__врем_предок

	def Паспорт_Печать(сам):
		print("тТип: имя_типа=", сам.__имя)
		print("      экспорт =", сам.__бЭкспорт)
		print("    указатель =", сам.__бУказатель)
		print("          предок =", сам.__врем_предок)
		if сам.__род != тРод.сБезРода:
			print("             род =", сам.__род)
		if сам.__врем_предок == тРод.сМассив:
			for ключ in range(len(сам.массив_размерность)):
				print("      ключ ", ключ, ":",сам.массив_размерность[ключ])
			print("      элем    =", сам.массив_тип)
		if сам.__врем_предок == тРод.сЗапись:
			for ключ in range(len(сам.запись_поля)):
				сам.запись.поля[ключ].Паспорт_Печать()
		print()
