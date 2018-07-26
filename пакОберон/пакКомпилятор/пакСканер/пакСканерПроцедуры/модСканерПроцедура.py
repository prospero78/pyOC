# coding:utf8
"""
Модуль описывает тип процедуры. По сути, микромодуль.
"""

if True:
	from пакОберон.пакКомпилятор.пакСущность.пакСлово import тСлово
	from . модПроцПараметр import тПроцПараметр
	from . модПроцБазовая import тПроцБазовая
	from пакОберон.пакКомпилятор.пакАнализ.пакАнализПроцедуры import тАнализКонстанты
	from ...пакСекции  import тТипы
	from ...пакСекции import тПеременные
	#from пакКомпилер.пакМодуль.пакТипы.модТипБазовый import тТипБазовый

class тПроцедура(тПроцБазовая):
	def __init__(сам, пДанные):
		тПроцБазовая.__init__(сам, пДанные)
		сам.__слова_проц = {} # Слова в своей процедуре
		сам.__бВозврат = False # признак возврата значения
		сам.__тВозврат = "" # Тип возвращаемого значения
		сам.__проц_конец = None # указатель на окончание своей процедуры
		сам.__конст = {} # Возможные константы в процедуре
		сам.__типы = {}  # Возможные типы в процедуре
		сам.__перем = {} # Возможные переменные в процедуре
		сам.__проц = {} # Возможные процедуры в процедуре
		сам.параметры = {} # словарь параметров передаваемых в процедуру
		сам.__Процедура_Проверить()# ***
		if сам.__СкобкаЛев_Открыть():
			сам.__Параметры_Проверить()
			сам.__СкобкаПрав_Закрыть()
			if сам.__Двоеточие_Обрезать():
				сам.__Возврат_Проверить()
		сам.__Разделитель_Обрезать()
		сам.__КонецСвой_Найти()
		сам.__СловаПроц_Получить()
		сам.__Константы_Проверить()
		сам.__Типы_Проверить()
		сам.__Переменные_Проверить()
		сам.__ПроцедурыВнутр_Проверить()

	def __СловаПроц_Получить(сам):
		"""
		Выбирает слова по своей процедуре.
		Дальше работает только с ними.
		"""
		слова_проц = {}  # будущий словарь слов секции процедур
		цСчёт = 0
		ключи = []
		for ключ in сам.слова_секции.keys():
			слово = сам.слова_секции[ключ]
			if слово != сам.__проц_конец:
				слова_проц[цСчёт] = слово
				ключи.append(ключ)
			else:
				слова_проц[цСчёт] = слово
				ключи.append(ключ)
				break
			цСчёт += 1
		слова_проц[цСчёт+1] = слово
		сам.__слова_проц = слова_проц

		for ключ in ключи:
			сам.слова_секции.pop(ключ)

	def __КонецСвой_Найти(сам):
		"""
		Разбор тела процедуры будет неправильным, если нет своего конца.
		Свой конец надо искать после нахождения своего имени.
		"""
		цКонец =  0
		бЕсть = True
		слово0 = None
		слово1 = None
		слово2 = None
		while бЕсть:
			слово0 = сам.слова_секции[цКонец]
			if слово0.строка =="END":
				слово1 = сам.слова_секции[цКонец+1]
				if слово1.строка == сам.имя:
					слово2 = сам.слова_секции[цКонец+2]
					if слово2.строка == ";": # это точно конец процедуры
						бЕсть = False
			цКонец += 1
			if цКонец >10:
				break
		сам.__проц_конец = слово2

	def __ПроцедурыВнутр_Проверить(сам):
		"""
		Процедура, по сути -- микромодуль, может содержать процедуры.
		Надо проверить.
		"""
		#TODO: процедур может быть несколько
		if len(сам.__слова_проц) > 0:
			парам = {}
			парам['секция'] = "СЕКЦИЯ"
			парам['слова'] = сам.__слова_проц
			сам.__проц[len(сам.__проц)] = тПроцедуры(парам)
			сам.__слова_проц = {}
			сам.__слова_проц = сам.__проц.слова_модуля

	def __Переменные_Проверить(сам):
		"""
		Процедура, по сути -- микромодуль, может содержать переменные.
		Надо проверить.
		"""
		парам = {}
		парам['секция'] = "СЕКЦИЯ"
		парам['слова'] = сам.__слова_проц
		сам.__перем = тПеременные(парам)
		сам.слова_проц = {}
		сам.слова_проц = сам.__перем.слова_модуля
		for ключ in сам.__слова_проц:
			print("тПроцедура:", сам.__слова_проц[ключ])

	def __Типы_Проверить(сам):
		"""
		Процедура, по сути -- микромодуль, может содержать типы.
		Надо проверить.
		"""
		парам = {}
		парам['слова'] = сам.__слова_проц
		парам['секция'] = "СЕКЦИЯ"
		сам.__типы = тТипы(парам)
		сам.__слова_проц = {}
		сам.__слова_проц = сам.__типы.слова_модуля

	def __Константы_Проверить(сам):
		"""
		Процедура, по сути -- микромодуль, может содержать констаты.
		Надо проверить.
		"""
		парам = {}
		парам['секция'] = "СЕКЦИЯ"
		парам['слова'] = сам.__слова_проц
		сам.__конст = тКонстанты(парам)
		сам.__слова_проц = {}
		сам.__слова_проц = сам.__конст.слова_модуля

	def __Разделитель_Обрезать(сам):
		"""
		В простых типах последнее слово ";"
		Поэтому его необходимо обрезать
		"""
		слово_раздел = сам.слова_секции[0]
		строка_раздел = слово_раздел.Проверить()
		if строка_раздел == ";":
			сам.СловаСекции_Обрезать()
		else:
			assert False, "тПроцедура: неправильный разделитель" + слово_раздел.стрИсх

	def __Двоеточие_Обрезать(сам):
		"""
		Здесь может быть, а может и не быть ":"
		"""
		бДвоеточие = False
		слово_двоеточ = сам.слова_секции[0]
		строка_двоеточ = слово_двоеточ.Проверить()
		if строка_двоеточ == ":": # есть двоеточие
			сам.СловаСекции_Обрезать()
			бДвоеточие = True
		return бДвоеточие

	def __Возврат_Проверить(сам):
		"""
		Проверяет тип возврата процедуры. Должно быть разрешённой строкой.
		Кроме того, имя может быть составным
		"""
		стрОш = "тПроцедура: тип возврата должен быть допустимым именем"
		слово_возврат = сам.слова_секции[0]
		строка_возврат = слово_возврат.Проверить()
		assert слово_возврат.ЕслиСтр_Допустимо(), стрОш + слово_возврат.стрИсх
		while not ((строка_возврат == ";") or (строка_возврат == ")")):
			сам.СловаСекции_Обрезать()
			сам.__тВозврат += строка_возврат
			слово_возврат = сам.слова_секции[0]
			строка_возврат = слово_возврат.Проверить()
			бРезульт = True
		assert сам.__тВозврат != "", "тПроцедура: тип возврата не может быть пустой строкой"
		return бРезульт

	def __Процедура_Проверить(сам):
		"""
		Проверяет наличие слова PROCEDURE среди слов секции
		"""
		слово_проц = сам.слова_секции[0]
		строка_проц = слово_проц.Проверить()
		бУсл = строка_проц == "PROCEDURE"
		стрОш = "тПроцедура: процедура должна начинаться с PROCEDURE" + слово_проц.стрИсх
		assert бУсл, стрОш
		сам.СловаСекции_Обрезать()

	def __СкобкаЛев_Открыть(сам):
		"""
		Проверяет на открытие левой скобки (значит есть входные параметры)
		В этой позиции может быть скобка, а может и нет. Надо проверять.
		"""
		бРезультат = False
		слово_скобка = сам.слова_секции[0]
		строка_скобка = слово_скобка.Проверить()
		if строка_скобка == "(":
			бРезультат = True
			сам.СловаСекции_Обрезать()
		return бРезультат

	def __СкобкаПрав_Закрыть(сам):
		"""
		Проверяет на закрытие правой скобки
		В этой позиции должна быть скобка.
		"""
		слово_скобка = сам.слова_секции[0]
		строка_скобка = слово_скобка.Проверить()
		if строка_скобка == ")":
			сам.СловаСекции_Обрезать()
		else:
			assert False, "тПроцедура: Параметры должны заканчиваться ')'" +слово_скобка.стрИсх

	def __Параметры_Проверить(сам):
		"""
		Получает параметры процедуры.
		Крутит до тех пор, пока не станет ")"
		"""
		слово_закрыть = сам.слова_секции[0]
		строка_закрыть = слово_закрыть.Проверить()
		while (строка_закрыть != ")"): # есть зарытие параметров
			парам = {}
			парам['слова']=сам.слова_секции
			парам['имя']=""
			парам['бЭкспорт']= False
			парам['секция']="PROCEDURE"

			параметр = None
			параметр = тПроцПараметр(парам)
			сам.параметры[len(сам.параметры)] = параметр
			сам.слова_секции = {}
			сам.слова_секции = параметр.слова_секции

			слово_закрыть = сам.слова_секции[0]
			строка_закрыть = слово_закрыть.Проверить()

	def СловаСекции_Обрезать(сам):
		"""
		Уменьшает слова секции на 1 с головы.
		"""
		новый_список = {}
		for ключ in range(1, len(сам.слова_секции)):
			новый_список[ключ-1]=сам.слова_секции[ключ]
		сам.слова_секции = None
		сам.слова_секции = новый_список

	def Паспорт_Печать(сам):
		print("тПроцедура: надо доделать Паспорт_Печать()")
