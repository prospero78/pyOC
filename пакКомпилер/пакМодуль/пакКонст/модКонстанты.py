# coding: utf8
"""
Содержит тип для обработки констант.
"""
if True:
	from пакКомпилер.пакСлово import тСлово

class тКонстанты:
	def __init__(сам, root, пСловаМодуля):
		сам.__root = root
		assert type(пСловаМодуля) == dict, "В секцию CONST должен передаваться словарь тегов, type="+type(пСловаМодуля)
		сам.__слова_модуля = пСловаМодуля # Все слова, чо передаются сюда
		сам.__слова_секции = {} # Слова содержащие константы
		сам.__бКонстСекция = False # Признак наличия секции констант
		сам.__бКонстОдин = False # Признак того, что в этом пространстве секций констант больше нет
		сам.__слово_конец = None # где заканчивается секция констант
		сам.__конст = {} # Содержит словарь констант
		сам.ошибка = root.ошибка

	@property
	def слова_модуля(сам):
		return сам.__слова_модуля

	def ЕслиКонстанты(сам):
		"""
		Первое слово в списке слов должно быть CONST.
		Если нет -- значит в исходнике нет констант.
		"""
		слово = сам.__слова_модуля[0]
		if слово.строка =='CONST':
			# укоротить слова
			слова_модуля = {}
			for счёт in range(1, len(сам.__слова_модуля)):
				слово = сам.__слова_модуля[счёт]
				слово._Номер_Уст(счёт-1)
				слова_модуля[счёт-1] = слово
			сам.__слова_модуля = {}
			сам.__слова_модуля = слова_модуля
			сам.__бКонстСекция = True
		return сам.__бКонстСекция

	def ЕслиСекцияНеПусто(сам):
		"""
		Может быть следующее слово:  TYPE VAR PROCEDURE BEGIN
		(* END модуля уже отброшено *)
		"""
		бНеПусто = False # признак что-то есть в секции
		# первый слово после CONST, а сам CONST уже распознан и отброшен
		слово = сам.__слова_модуля[0]
		assert type(слово) == тСлово, "тКонст: Слово должно быть тСлово, type="+type(слово)
		# проверим на внезапный конец секции
		маркер = not (слово.строка in ["TYPE", "VAR", "PROCEDURE", "BEGIN"])

		if маркер: # секция импорта пустая
			бНеПусто = True
		return бНеПусто

	def ЕслиКонстОграничен(сам):
		"""
		Ищет разделитель окончания констант.
		Сканируем слова все подряд.
		Может быть следующий слово-маркер окончаня: TYPE VAR PROCEDURE BEGIN
		Первое слово всегда должно быть именем константы и не может быть маркером
		Произвольное слово может быть ";" и не может быть маркером
		"""
		слова_всего = len(сам.__слова_модуля)-1
		цСловаСчёт = 0 # первый слово после CONST, а сам CONST уже распознали и отбросили
		слово = сам.__слова_модуля[цСловаСчёт]
		маркер = (слово.строка in ["TYPE", "VAR", "PROCEDURE", "BEGIN"])
		# ищем имя константы
		while (not маркер) and (цСловаСчёт < слова_всего):
			цСловаСчёт += 1
			слово = сам.__слова_модуля[цСловаСчёт]
			assert type(слово) == тСлово, "тКонст: Слово должно быть тСлово, type="+type(слово)
			маркер = (слово.строка in ["TYPE", "VAR", "PROCEDURE", "BEGIN"])
		цСловаСчёт -= 1
		слово = сам.__слова_модуля[цСловаСчёт]
		сам.__слово_конец = слово
		if слово.строка != ";":
			# Константы -- могут занимать весь модуль, без других секций
			сам.ошибка.Печать("Тег должен быть ';', слово="+слово.слово)

	def СловаСекции_Получить(сам):
		"""
		Выбирает слова по секции констант.
		Дальше работает только с ними.
		"""
		слова_секции = {}  # будущий словарь слов
		for цСчётСлова in range(0, сам.__слово_конец.номер+1): # CONST уже отброшено
			слово = сам.__слова_модуля[цСчётСлова]
			слово._Номер_Уст(цСчётСлова)
			#print("#", цСчётСлова, "num",слово.номер, слово.имя)
			слова_секции[цСчётСлова] = слово
		сам.__слова_секции = слова_секции

		слова_модуля = {}  # будущий словарь тегов
		счёт = 0
		for цСчётСлова in range(сам.__слово_конец.номер+1, len(сам.__слова_модуля)): # Пропускаем IMPORT
			слово = сам.__слова_модуля[цСчётСлова]
			слово._Номер_Уст(счёт)
			#print("+",цСчётСлова, слово.номер, слово.имя)
			слова_модуля[счёт] = слово
			счёт += 1
		сам.__слова_модуля = {}
		сам.__слова_модуля = слова_модуля

	def Константы_Разбить(сам):
		"""
		У нас уже есть словарь констант. Теперь их надо разбить на части.
		Тег 1 -- имя
		Тег 2 -- =
		Тег N -- ;
		"""
		#print("keys=", сам.__слова_секции.keys())
		#for i in сам.__слова_секции:
		#   print(i, сам.__слова_секции[i])
		цСчётСлова = 0 # Счётчик констант
		счёт = 0
		while счёт < сам.цСловаВсего-1:
			#print(счёт, ам.цСловаВсего)
			слово = сам.__слова_секции[счёт] # Должно быть имя константы
			if (not слово.ЕслиИмя_Строго()):
				#print(слово.имя, " номер", слово.номер)
				сам.ошибка.Коорд("Неправильное имя константы", слово.коорд, слово.стр)
			else:
				конст = {}
				конст["tag"] = слово
				конст["exp"] = {}
				счёт += 1
				слово = сам.__слова_секции[счёт] # Должно быть "=" или "*"
				# проверим на экспорт
				if слово.строка == "*":
					конст["export"] = "True"
					счёт += 1
					слово = сам.__слова_секции[счёт] # Должно быть новое имя
				elif слово.строка == "=":
					конст["export"] = "False"
				else:
					сам.ошибка.Коорд("Ошибка в присвоении константы", слово.коорд, слово.стр)

				# проверим на присвоение
				if слово.строка != "=":
					сам.ошибка.Коорд("Неправильное присвоение константы", слово.коорд, слово.стр)
				else: # всё правильно, заполняем словарь константы
					счёт += 1
					слово = сам.__слова_секции[счёт] # Должно быть что-то
					счёт_выраж = 0
					while слово.строка != ";" and счёт < len(сам.__слова_секции)-1:
						конст["exp"][счёт_выраж] = слово
						счёт_выраж += 1
						счёт += 1
						слово = сам.__слова_секции[счёт] # Должно быть новое имя
					сам.__конст[цСчётСлова] = конст
					цСчётСлова += 1
					счёт += 1
		if слово.строка != ";":
			assert слово.слово == ";", "Неправильно закончился разбор констант, слово(;)="+слово.слово

	def Теги_Печать(сам):
		print("\nтКонст.Теги_Печать()")
		for keys in сам.__слова_модуля:
			слово = сам.__слова_модуля[keys]
			print(слово)

	def Конст_Печать(сам):
		print("\nтКонст.Конст_Печать()")
		for keys in сам.__слова_секции:
			слово = сам.__слова_секции[keys]
			print(keys, слово)

	def КонсСлов_Печать(сам):
		"""
		Печатает словари констант
		"""
		for i in сам.__конст:
			конст = сам.__конст[i]
			имя = конст['tag'].имя
			print(i, имя, "Экспорт=",конст['export'], конст['tag'].коорд)
			стр = ""
			выраж = конст["exp"]
			for i1 in выраж:
				стр = стр + " " + выраж[i1].имя
			print("      ", стр)

	def Обработать(сам):
		"""
		Проводит разбор секции CONST.
		"""
		if сам.ЕслиКонстанты():
			print("Есть секция констант!")
			if сам.ЕслиСекцияНеПусто():
				print("Секция констант не пустая!")
				#сам.Теги_Печать()
				сам.ЕслиКонстОграничен()
				#сам.Теги_Печать()
				сам.СловаСекции_Получить()
				#сам.Конст_Печать()
				сам.Константы_Разбить()
				#сам.КонсСлов_Печать()
			else:
				print("Секция констант пустая!")
		else:
			print("Нет секции констант!")

	@property
	def цСловаВсего(сам):
		return len(сам.__слова_секции)
