# coding: utf8
"""
Модуль предоставляет класс для разбора типа.
Простой тип может содержать определения других подтипов и членов.
"""

if True:
	from пакКомпилер.пакСлово import тСлово
	from пакКомпилер.пакМодуль.пакТипы.модРод import тРод

	from . модТипВстроен import тТипВстроен
	from . модТипМассив import тТипМассив
	from . модТипЗапись import тТипЗапись

	from пакКомпилер.пакМодуль.пакПоле.модПоле import тПоле

class тТип:
	def __init__(сам, пКорень, пСловаСекции):
		сам.__имя = "" # Имя типа в установить в пустую строку
		сам.__бЭкспорт = False
		сам.__род = тРод.сБезРода # Род записи -- один из встроенных, ARRAY, RECORD, PROCEDURE
		сам.__предок = тРод.сБезТипа # Тип предка -- один из наследуемых
		сам.__бУказатель = False # тип имеет модификатор указатель
		сам.массив_тип = тРод.сБезТипа # устанавливает тип массива (если тип -- массив)
		сам.поля = {} # словарь полей типа
		assert len(пСловаСекции) > 1, "тТипБазовый: Неполное определение секции"
		сам.__слова_секции = пСловаСекции # Список слов типа
		сам.массив_размерность = {} # заполняется при определении массива
		сам.запись_поля = {} # словарь полей типа RECORD
		сам.__Имя_Проверить()
		сам.__Экспорт_Проверить()
		сам.__Определитель_Проверить()
		сам.__Указатель_Проверить()
		сам.__Род_Проверить()
		сам.__Разделитель_Обрезать()

	def __Имя_Проверить(сам):
		"""
		Проверяет имя типа. Должно быть именем и
		не должно быть END.
		Имя НЕ МОЖЕТ быть составным
		"""
		бРезульт = False
		имя = сам.Слово_Проверить()
		слово_имя = сам.слова_секции[0]
		if слово_имя.ЕслиИмя():
			сам.СловаСекции_Обрезать()
			сам.__имя = имя
			бРезульт = True
		else:
			assert слово_имя.ЕслиИмя(), "тТип: имя типа должно быть допустимым именем, имя=" + имя

	def Предок_Проверить(сам):
		"""
		Проверяет предка записи. Должно быть разрешённой строкой и
		не должно быть END.
		Кроме того, имя может быть составным
		"""
		стрОш = "тТип: имя типа должно быть допустимым именем, имя="
		бРезульт = False
		имя = сам.Слово_Проверить()
		слово_имя = сам.слова_секции[0]
		assert слово_имя.ЕслиСтр_Допустимо(), стрОш + имя
		assert сам.__предок == тРод.сБезТипа, "тТип: предок уже назначен, предок=" + сам.__предок
		сам.__предок = ""
		while (имя == ".") or (слово_имя.ЕслиСтр_Допустимо()):
			сам.СловаСекции_Обрезать()
			сам.__предок += имя
			имя = сам.Слово_Проверить()
			слово_имя = сам.слова_секции[0]
			бРезульт = True
		return бРезульт

	def Элемент_Проверить(сам, пПоле):
		"""
		Проверяет предка записи. Должно быть разрешённой строкой и
		не должно быть END.
		Кроме того, имя может быть составным
		"""
		стрОш = "тПеременные: тип элемента переменной должен быть допустимым именем, имя="
		имя = сам.Слово_Проверить()
		слово_имя = сам.слова_секции[0]
		assert слово_имя.ЕслиСтр_Допустимо(), стрОш + имя
		assert сам.массив_тип == тРод.сБезТипа, "тТип: элемент массива уже назначен, элемент=" + сам.массив_тип
		элемент = ""
		while (имя == ".") or (слово_имя.ЕслиСтр_Допустимо()):
			сам.СловаСекции_Обрезать()
			элемент += имя
			имя = сам.Слово_Проверить()
			слово_имя = сам.слова_секции[0]
		return элемент

	def __Экспорт_Проверить(сам):
		"""
		Проверяет является ли тип экспортируемым.
		"""
		строка_экспорт = сам.Слово_Проверить()
		if строка_экспорт == "*": # есть экспорт
			сам.СловаСекции_Обрезать()
			сам.__бЭкспорт = True
		elif строка_экспорт == "=":
			pass # это определение типа
		else:
			assert False, "тТип: Символ экспорта допустим '*' или '=',    строка=" + строка_экспорт

	def __Определитель_Проверить(сам):
		"""
		Проверяет является ли слово в начале слов секции типа -- "=".
		После обрезания, должно быть первым.
		"""
		строка_опр = сам.Слово_Проверить()
		if строка_опр == "=": # правильное выражение определения типа
			сам.СловаСекции_Обрезать()
		else: # если определение типа
			сам.Ошибка_Печать(слово_опр, "тТип: Отсутствует определитель (=) в объявлении типа")

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
		строка_род = сам.Слово_Проверить()
		assert сам.слова_секции[0].ЕслиСтр_Допустимо(), "тТип: род типа должен быть допустимым именем, строка=" + строка_род
		if строка_род in тРод.тип_встроен: # текущий тип основан на встроенном типе
			тип = тТипВстроен(сам)
		elif строка_род == тРод.сМассив: # текущий тип основан на массиве
			тип = тТипМассив(сам)
		elif строка_род == тРод.сЗапись: # текущий тип основан на записе
			тип = тТипЗапись(сам)
			сам.__род = тРод.сЗапись
		elif строка_род == тРод.сПроцедура: # текущий тип основан на процедуре
			тип = тТипПроцедура(сам)
			сам.__род = тРод.сПроцедура
		elif сам.слова_секции[0].ЕслиСтр_Допустимо():
			"""
			Здесь конструкция вида:
			POINTER TO мЧт.Ввод
			Тип устанавливается вручную.
			"""
			сам.Предок_Проверить()
		else:
			assert False, "тТип: неизвестный тип записи, род=" + строка_род

	def __Указатель_Проверить(сам):
		"""
		Если тип является указателем, то устанавливается соответствующий признак.
		Иначе, просто пропускается.
		"""
		строка_род = сам.Слово_Проверить()
		if строка_род in тРод.сУказатель: # модификатор типа, а не сам тип
			сам.__бУказатель = True
			сам.СловаСекции_Обрезать()
			# дальше ОБЯЗАТЕЛЬНО следует ключевое слово "TO"
			строка_из = сам.Слово_Проверить()
			if строка_из == "TO": # следование за POINTER
				сам.СловаСекции_Обрезать()
			else:
				assert False, "тТип: за POINTER не следует TO, слово=" + строка_из

	def __Разделитель_Обрезать(сам):
		"""
		В простых типах последнее слово ";"
		Поэтому его необходимо обрезать
		"""
		строка_раздел = сам.Слово_Проверить()
		if строка_раздел == ";":
			сам.СловаСекции_Обрезать()
		else:
			assert False, "тТип: неправильный разделитель типа, строка=" + строка_раздел

	def Предок_Уст(сам, пПредок):
		assert type(пПредок) == str, "тТип: пПредок должен быть str, type="+str(type(пПредок))
		assert пПредок != "", "тТип: пПредок не может быть пустой строкой"
		assert not (пПредок in "0123456789#!@%$^&*()-=+<>?/.`~№;:"), "Имя предка не может начинаться с этой литеры, пПредок=" + пПредок
		assert сам.__предок == тРод.сБезТипа, "тТип: тип уже установлен, тип="+сам.__предок
		сам.__предок = пПредок

	def СловаСекции_Обрезать(сам):
		"""
		Уменьшает слова секции на 1 с головы.
		"""
		новый_список = {}
		for ключ in range(1, len(сам.__слова_секции)):
			новый_список[ключ-1]=сам.__слова_секции[ключ]
		сам.__слова_секции = {}
		сам.__слова_секции = новый_список

	@property
	def бЭкспорт(сам):
		return сам.__бЭкспорт

	@property
	def слова_секции(сам):
		return сам.__слова_секции

	@property
	def имя(сам):
		return сам.__имя

	@property
	def предок(сам):
		return сам.__предок

	def Слово_Проверить(сам):
		"""
		Проверяет первое слово в словаре слов секции на допустимость.
		"""
		слово = сам.слова_секции[0]
		assert type(слово) == тСлово, "тТипБазовый: слово должно быть тСлово, тип="+str(type(слово))
		строка = слово.строка
		assert type(строка) == str, "тТипБазовый: строка должна быть 'str', type=" + str(type(строка))
		assert строка != "", "тТипБазовый: строка не может быть пустой"
		return строка

	def Паспорт_Печать(сам):
		print("тТип: имя_типа=", сам.__имя)
		print("      экспорт =", сам.__бЭкспорт)
		print("    указатель =", сам.__бУказатель)
		print("          предок =", сам.__предок)
		if сам.__род != тРод.сБезРода:
			print("             род =", сам.__род)
		if сам.__предок == тРод.сМассив:
			for ключ in range(len(сам.массив_размерность)):
				print("      ключ ", ключ, ":",сам.массив_размерность[ключ])
			print("      элем    =", сам.массив_тип)
		if сам.__предок == тРод.сЗапись:
			for ключ in range(len(сам.запись_поля)):
				сам.запись.поля[ключ].Паспорт_Печать()
		print()
