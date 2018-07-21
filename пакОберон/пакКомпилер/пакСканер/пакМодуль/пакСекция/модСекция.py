# coding:utf8
"""
Модуль базового типа секции для всех секций
"""

if True:
	from ...пакСлово import тСлово

class тСекция:
	def __init__(сам, пДанные):
		def Слова_Проверить():
			бУсл = type(пДанные['слова']) == dict
			стрОш = "В секцию  должен передаваться словарь слов, type=" + str(type(пДанные['слова']))
			assert бУсл, стрОш

		Слова_Проверить()
		сам.__секция = пДанные['секция']
		сам.слова_модуля = пДанные['слова'] # Все слова модуля
		сам.слова_секции = пДанные['слова_секции'] # все слова секции
		сам.бСекцияЕсть = False # Признак наличия секции
		сам.__слово_конец = None # последнее слово в секции

	def СловаСекции_Получить(сам):
		"""
		Выбирает слова по секции.
		Дальше работает только с ними.
		"""
		слова_секции = {}  # будущий словарь слов
		# заголовок секции уже отброшен
		цСчёт = 0
		for цСчётСлова in range(0, сам.цСловаМодуля):
			слово = сам.слова_модуля[цСчётСлова]
			if сам.__слово_конец != слово:
				слова_секции[цСчёт] = слово
				цСчёт += 1
			else:
				слова_секции[цСчёт] = слово
				break
		сам.слова_секции = {}
		сам.слова_секции = слова_секции

		слова_модуля = {}  # будущий словарь слов
		счёт = 0
		# Включаем заголовок следующей секции и до конца
		for цСчётСлова in range(цСчёт+1, сам.цСловаМодуля):
			слово = сам.слова_модуля[цСчётСлова]
			слова_модуля[счёт] = слово
			счёт += 1
		сам.слова_модуля = {}
		сам.слова_модуля = слова_модуля

	def СловаСекции_Обрезать(сам):
		"""
		Уменьшает слова секции на 1 с головы.
		"""
		новый_список = {}
		for ключ in range(1, len(сам.слова_секции)):
			новый_список[ключ-1]=сам.слова_секции[ключ]
		сам.слова_секции = {}
		сам.слова_секции = новый_список

	def СловаМодуля_Печать(сам):
		"""
		Печатает все слова, оставшиеся модулю
		"""
		print("Слова модуля в секции", сам.__секция)
		for ключ in сам.слова_модуля:
			слово = сам.слова_модуля[ключ]
			print(слово)

	def СловаСекции_Печать(сам):
		"""
		Печатает все слова, доставшиеся импорту
		"""
		print("Слова секции в секции", сам.__секция)
		for ключ in сам.слова_секции:
			слово = сам.слова_секции[ключ]
			print(слово)

	@property
	def цСловаМодуля(сам):
		return len(сам.слова_модуля)

	@property
	def цСловаСекции(сам):
		return len(сам.слова_секции)

	def Конец_Уст(сам, пСлово):
		"""
		Принудительно ограничивает присвоение слова конца секции.
		Можно сделать только один раз.
		"""
		assert пСлово != None, "тСекция: слово_конец уже установлено" + сам.__слово_конец.стрИсх
		assert type(пСлово) == тСлово, "тСекция: пСлово должно быть тСлово, type="+str(type(пСлово))
		сам.__слово_конец = пСлово

	@property
	def слово_конец(сам):
		return сам.__слово_конец
