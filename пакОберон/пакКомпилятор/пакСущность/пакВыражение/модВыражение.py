# coding: utf8
"""
Модуль предоставляет средства для расчёта выражений
Чтобы вычислять выражения нужно анализировать, что поступает
на вход.
  - Анализ целых чисел.
"""

def Вычислить(слова:dict):
	"""
	Вычисляет значение предоставляемого выражения
	"""
	ключи = слова.keys() # все ключи словаря
	ключ = 0
	while True: # перебираем список ключей
		стрОп = слова[ключ]
		if стрОп == "(": # если ключ -- скобка
			# Пробуем сформировать список для выражения
			выраж = {}
			счёт = 0
			ключ += 1
			стрОп = слова[ключ]
			while стрОп != ")":
				выраж[счёт] = стрОп

def Выраж(слова:dict):
	"""
	Считает простое числовое выражение
	"""
	цРезульт = 0
	for ключ in слова:
		слово = слова[ключ]
		if ЕслиЧисло(слово):
			цРезульт += int(слово)

def ОпСложЦел2(пцЧисло1, пцЧисло2 : тОп): -> int:
	"""
	Скалыдвает два целых числа
	"""
	return пцЧисло1 + пцЧисло2

def ЕслиЧисло(псНечто : str) -> bool:
	"""
	Проверяет является ли число целым.
	"""
	if type(псНечто) != str:
		assert False, "Тип параметра для проверки не имеет str " + str(type(псНечто))

	if ЕслиЦелое(псНечто) or ЕслиДробное(псНечто):
		return True
	else:
		return False

def ЕслиЦелое(псНечто : str) -> bool:
	"""
	Проверяет является ли число целым.
	"""
	if type(псНечто) != str:
		assert False, "Тип параметра для проверки не имеет str " + str(type(псНечто))

	if псНечто.find(".") != -1:
		return False
	try:
		цЧисло = int(псНечто)
	except:
		return False
	return True

def ЕслиДробное(псНечто : str) -> bool:
	"""
	Проверяет является ли число дробным.
	"""
	if type(псНечто) != str:
		assert False, "Тип параметра для проверки не имеет str " + str(type(псНечто))

	if псНечто.find(".") == -1:
		return False
	try:
		дЧисло = float(псНечто)
	except:
		return False
	return True

def ЕслиСтрока(псНечто : str) -> bool:
	"""
	Проверяет является ли псНечто строкой -- должна быть двойные ковычки по краям.
	"""
	if type(псНечто) != str:
		assert False, "Тип параметра для проверки не имеет str " + str(type(псНечто))
	if псНечто[0] == "\"" and псНечто[-1] == "\"":
		return True
	else:
		return False

if __name__=="__main__":
	if True:
		#print("Результ int(3)=", ЕслиЦелое(3) )
		#print("Результ int(3.0)=", ЕслиЦелое(3.0) )
		#print("Результ int(3.1)=", ЕслиЦелое(3.1), int(3.1) )
		#print("Результ int(3.6)=", ЕслиЦелое(3.6), int(3.6) )
		#print("Результ int('3')=", ЕслиЦелое('3') )
		#print("Результ int('3.2')=", ЕслиЦелое('3.2') )
		#print("Результ float('3.2')=", ЕслиДробное('3.2') )
		#print("Результ float('3')=", ЕслиДробное('3') )
		pass

	выраж = {
		0:"(",
		1:"12",
		2:"+",
		3:"13.0",
		4:"-",
		5:"6",
		6:")",
		7:"-",
		8:"3.2"}
	Вычислить(выраж)
