# coding: utf8
"""
Модуль определяет разбор секции типов.
"""

if True:
	from пакКомпилер.пакСлово import тСлово
	from .модТип import тТип

class тТипы:
	def __init__(сам, пКорень, пСлова):
		def Слова_Проверить():
			бУсл = type(пСлова) == dict
			стрОш = "В секцию типов должен передаваться словарь слов, type=" + str(type(пСлова))
			пКорень.конс.Проверить(бУсл, стрОш)
		
		сам.__корень = пКорень
		
		Слова_Проверить()
		сам.__слова_модуль = пСлова # все пСлова исходника
		
		сам.__слова_типа = {} #  Все пСлова секции TYPE
		
		сам.__типы = {} # словарь по словам каждого типа в модуле
		сам.__бТипыЕсть = False # По умлочанию секции TYPE нет
		сам.__бТипыНеПустые = False # По умолчанию секция TYPE пустая
		сам.ошибка = пКорень.ошибка
		
	def __Слово_TYPE_Обрезать(сам):
		"""
		Первое слово в списке слов должно быть TYPE.
		Если нет -- значит в исходнике нет описания типов.
		Возвращает результат встречи с TYPE
		"""
		слово = сам.__слова_модуль[0]
		if слово.строка =='TYPE':
			# укоротить типы
			слова = {}
			for счёт in range(1, len(сам.__слова_модуль)):
				слово = сам.__слова_модуль[счёт]
				слово._Номер_Уст(счёт-1)
				слова[счёт-1] = слово
			сам.__слова_модуль = {}
			сам.__слова_модуль = слова
			сам.__бТипыЕсть = True
		return сам.__бТипыЕсть

	def __ЕслиТипыНеПустые(сам):
		"""
		Может быть следующее слово:   ; VAR PROCEDURE BEGIN (* END модуля уже отброшено *)
		Секция TYPE может быть пустой, но если есть типы, они должны заканчиваться на ;
		"""
		def Слово_Проверить():
			бУсл = (type(слово) == тСлово)
			стрОш = "Слово должно быть тСлово, type=" + str(type(слово))
			корень.конс.Проверить(бУсл, стрОш)
		корень = сам.__корень
		
		слово = сам.__слова_модуль[0] # первое слово после TYPE, а сам TYPE уже распознан и отброшен
		Слово_Проверить()
		
		# проверим на внезапный конец секции
		бМаркер = (слово.строка in ["VAR", "PROCEDURE", "BEGIN"])
		if not бМаркер: # секция типизации не пустая
			сам.__бТипыНеПустые = True
		return сам.__бТипыНеПустые

	def __ЕслиТипыОграничены(сам):
		"""
		Ищет разделитель окончания типов.
		Сканируем слова все подряд.
		Может быть следующее слово-маркер окончания секции типов: VAR PROCEDURE BEGIN,
		так как типов может быть несколько, то ";" не подходит
		Первое слово всегда должен быть именем типа и не может быть маркером
		Произвольное слово может быть ";" и не может быть маркером
		"""
		def Слово_Проверить():
			бУсл = type(слово) == тСлово
			стрОш = "тТипы: Слово должно быть тСлово, type=" + str(type(слово))
			корень.конс.Проверить(бУсл, стрОш)
		def Маркер():
			сам.__бМаркер = (слово.строка in ["VAR", "PROCEDURE", "BEGIN"])
		корень = сам.__корень
		цСловМодульВсего = len(сам.__слова_модуль) - 1 # отсчёт начинается с нуля
		цСловоСчёт = 0 # первый слово после TYPE, а сам TYPE уже распознали и отбросили
		слово = сам.__слова_модуль[цСловоСчёт]
		Слово_Проверить()
		Маркер()
		while (not сам.__бМаркер) and (цСловоСчёт < цСловМодульВсего ):
			цСловоСчёт += 1
			слово = сам.__слова_модуль[цСловоСчёт]
			
			Слово_Проверить()
			Маркер()
		цСловоСчёт -= 1
		слово = сам.__слова_модуль[цСловоСчёт]
		сам.__слово_конец = слово
		# Проверка на окончание секции типов
		if слово.строка != ";":
			сам.ошибка.Печать("тТипы: слово ограничение секции типов должно быть ';', слово= " + слово.строка)

	def __СловаСекции_Получить(сам):
		"""
		Выбирает слова по секции типов.
		Дальше работает только с ними.
		"""
		слова_секции = {}  # будущий словарь слов секции типов
		for цСчётТип in range(0, сам.__слово_конец.номер+1): # TYPE уже отброшено
			слово = сам.__слова_модуль[цСчётТип]
			слово._Номер_Уст(цСчётТип)
			#print("т+", цСчётТип, "num",слово.номер, слово.слово)
			слова_секции[цСчётТип] = слово
		сам.__слова_типа = слова_секции

		слова_модуля = {}  # будущий словарь слов модуля
		цСчётМодуль = 0
		for цСчёт in range(сам.__слово_конец.номер+1, len(сам.__слова_модуль)):
			слово = сам.__слова_модуль[цСчёт]
			слово._Номер_Уст(цСчётМодуль)
			#print("т-", цСчёт, слово.номер, слово.слово)
			слова_модуля[цСчётМодуль] = слово
			цСчётМодуль += 1
		сам.__слова_модуль = {}
		сам.__слова_модуль = слова_модуля
		
	def __Типы_Разделить(сам):
		"""
		У нас уже есть словарь слов типов. Теперь их надо разбить на части.
		Слово 1 -- имя типа
		Слово 2 -- = (присовение типа)
		Слово 3 -- род типа: POINTER, RECORD, ARRAY
		Дальше варианты по порядку следования слов.
		Необходимо контролировать "=" -- это означает начало нового типа.
		Необходимо контролировать "END" + ";" -- окончание типа.
		Тип может быть СОСТАВНЫМ!
		"""
		def ЕслиИмяТипа():
			счёт = 0
			тип_имя = сам.__слова_типа[счёт]
			print("Имя типа =", тип_имя.строка)
			if not тип_имя.ЕслиИмя():
				сам.ошибка.Коорд("тТипы: Неправильное имя типа в определении", тип_имя.коорд, тип_имя.стр)
			сам.__счёт = счёт
		
		def ЕслиЭкспорт():
			счёт = сам.__счёт
			счёт += 1
			слово_экспорт = сам.__слова_типа[счёт]
			if слово_экспорт.строка == "*":
				бЭкспорт = True
				счёт += 1
				слово_экспорт = сам.__слова_типа[счёт]
				print("   бЭкспорт = True")
			else:
				бЭкспорт = False
			сам.__слово_экспорт = слово_экспорт
			сам.__счёт = счёт
		
		def ЕслиОпределить():
			счёт = сам.__счёт
			слово_опр = сам.__слова_типа[счёт]
			if слово_опр.строка == "=": # если определение типа
				счёт += 1
			else:
				строка = сам.__корень.исх.строки(слово_опр.коорд.стр) 
				print(сам.__корень.исх.строки(слово_опр.коорд.стр), строка)
				сам.ошибка.Коорд("Отсутствует определитель (=) в объявлении типа", слово_опр.коорд, строка)
			сам.__счёт = счёт
			
		def РодТипа():
			def Род_запись():
				def ПредокТипа_Получ(пцСчёт, пСловоПредок):
					"""
					Вычисляет предка для типа
					"""
					стрПредок = ""
					if пСловоПредок.строка == ";": # У типа нет предка
						пцСчёт += 1
					elif пСловоПредок.строка == "(": # У типа есть предок
						пцСчёт += 1
						пСловоПредок = сам.__слова_типа[пцСчёт]
						стрПредок = пСловоПредок.строка
						пцСчёт += 1
						пСловоПредок = сам.__слова_типа[пцСчёт]
						if пСловоПредок.строка != ")":
							сам.ошибка.Коорд("Ошибка в определении предка типа", пСловоПредок.коорд, пСловоПредок.стр)
						пцСчёт +=1
					else:
						сам.ошибка.Коорд("Ошибка в определении предка", пСловоПредок.коорд, пСловоПредок.стр)
					
					return пцСчёт, стрПредок
				пцСчёт += 1
				пСловоПредок = сам.__слова_типа[пцСчёт]
				print(5, пСловоПредок.строка)
				пСловоПредок, пцСчёт = ПредокТипа_Получ(пцСчёт, пСловоПредок)
				print(6, слово_экспорт.строка)
			def Род_указатель():
				def ЕслиТО():
					счёт = сам.__счёт
					счёт += 1
					слово_указ = сам.__слова_типа[счёт]
					#print("Тег <ТО>", слово_указ.строка)
						
					# Кючевое строка TO
					if слово_указ.строка != "TO":
						стрИсх = сам.__корень.исх.строки(слово_указ.коорд.стр) 
						print(сам.__корень.исх.строки(слово_указ.коорд.стр), стрИсх)
						сам.ошибка.Коорд("тТипы: Неполный квалификатор указателя типа", слово_указ.коорд, стрИсх)
					сам.__счёт = счёт
				def ВилкаМодульТочкаТип():
					счёт = сам.__счёт
					счёт += 1
					строка_указ = сам.__слова_типа[счёт]
					#print("Раздел: ", строка_указ.строка)
						
					# Теперь вилка -- может быть имя модуля, а может и имя собственное.
					if not строка_указ.ЕслиИмя():
						стрИсх = сам.__корень.исх.строки(строка_указ.коорд.стр) 
						print(сам.__корень.исх.строки(строка_указ.коорд.стр), стрИсх)
						сам.ошибка.Коорд("Неверное имя базового типа или его модуля для указатели", строка_указ.коорд, стрИсх)
					
					# Теперь может быть точка
					счёт +=1
					слово_разд = сам.__слова_типа[счёт]
					#print(9, " =слово_разд= '"+слово_разд.строка+"'")
					if слово_разд.строка == ".":
						слово_модуль = сам.__слова_типа[счёт-1]
						# имя базового типа в модуле
						счёт += 1
						слово_тип_предок = сам.__слова_типа[счёт]
						print("   Модуль     : "+слово_модуль.строка+"'")
						print("   Тип-предок: "+слово_тип_предок.строка+"'")
					# Может быть уже разделитель типов
					elif слово_разд.строка == ";":
						слово_тип_предок = сам.__слова_типа[счёт-1]
						счёт += 1
					# Может быть имя члена
					elif слово_разд.ЕслиИмя():
						счёт += 1
						слово_тип_предок = сам.__слова_типа[счёт]
					# Все варианты испробованы -- запрещённая сущноть
					else:
						строка = сам.__корень.исх.строки(слово_разд.коорд.стр) 
						print(сам.__корень.исх.строки(слово_разд.коорд.стр), строка)
						сам.ошибка.Коорд("Неверный разделитель в определении базы типа", слово_разд.коорд, строка)
					# Имя типа в другом модуле должно быть именем
					if not слово_тип_предок.ЕслиИмя():
						строка = сам.__корень.исх.строки(слово_тип_предок.коорд.стр) 
						print(сам.__корень.исх.строки(слово_тип_предок.коорд.стр), строка)
						сам.ошибка.Коорд("Неверное имя базового типа в другом модуле", слово_тип_предок.коорд, строка)
					сам.__счёт = счёт
				 
				ЕслиТО()
				# Квалификатор указтеля верный. Должно быть имя типа или модуля
				ВилкаМодульТочкаТип()
			def ЕслиМассив():
				счёт += 1
				тег_массив = сам.__слова_типа[счёт]
				# должно быть число
			счёт = сам.__счёт
			слово_род = сам.__слова_типа[счёт]
			print("   Род типа:", слово_род.строка)
			if слово_род.строка in ["RECORD", "POINTER", "ARRAY"] or слово_род.ЕслиИмя():
				if слово_род.строка == "RECORD":
					Род_запись()
				elif слово_род.строка == "POINTER":
					Род_указатель()
				elif слово_род.строка == "ARRAY":
					ЕслиМассив()
				else: # здесь может быть базовый или пользовательский тип
					слово_род = тег_класс
			else:
				строка = сам.__корень.исх.строки(слово_род.коорд.стр)
				сам.ошибка.Коорд("Неверный квалификатор рода типа", слово_род.коорд, строка)
		# Повторять всё, пока не закончится сеция типов.
		
		# 1. Посмотрим что у нас вообще есть.
		# сам.__СловаСекции_Печать()
		
		# 2. Первое слово должен быть имя
		ЕслиИмяТипа()
		
		# 3. Второе слово должен быть "*" или "="
		ЕслиЭкспорт()
		
		# 4. теперь точно слово "="
		ЕслиОпределить()
		
		# 5. Вычисляем какого рода тип
		РодТипа()

	def СловаМодуля_Печать(сам):
		сам.__корень.конс.Печать("\nтТипы.СловаМодуля_Печать()")
		for ключ in сам.__слова_модуль:
			слово = сам.__слова_модуль[ключ]
			сам.__корень.конс.Печать(слово)

	def СловаСекции_Печать(сам):
		сам.__корень.конс.Печать("\nтТипы.СловаСекции_Печать()")
		for ключ in сам.__слова_типа:
			слово = сам.__слова_типа[ключ]
			сам.__корень.конс.Печать(ключ, слово)

	def Обработать(сам):
		"""
		Проводит разбор секции TYPE.
		"""
		if сам.__Слово_TYPE_Обрезать():
			сам.__корень.конс.Печать("Есть типы!")
		if сам.__ЕслиТипыНеПустые():
			сам.__корень.конс.Печать("Типы не пустые!")
			#сам.Теги_Печать()
			сам.__ЕслиТипыОграничены()
			#сам.Теги_Печать()
			сам.__СловаСекции_Получить()
			#сам.СловаСекции_Печать()
			#сам.Конст_Печать()
			сам.__Типы_Разделить()
		else:
			print("Нет типов!")
