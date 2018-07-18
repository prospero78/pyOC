# coding:utf8
"""
Модуль базового типа секции для всех секций
"""
class тСекция:
	def __init__(сам, пДанные):
		def Слова_Проверить():
			бУсл = type(пДанные['слова']) == dict
			стрОш = "В секцию  должен передаваться словарь слов, type=" + str(type(пДанные['слова']))
			assert бУсл, стрОш
		Слова_Проверить()
		сам.__модуль = пДанные['секция']
		сам.слова_модуля = пДанные['слова'] # Все слова модуля
		сам.слова_секции = {} # все слова секции
		сам.бСекцияЕсть = False # Признак наличия секции
		сам.слово_конец = None # последнее слово в секции

	def СловаСекции_Получить(сам):
		"""
		Выбирает слова по секции.
		Дальше работает только с ними.
		"""
		слова_секции = {}  # будущий словарь слов
		# заголов секции уже отброшен
		for цСчётСлова in range(0, сам.слово_конец.номер+1):
			слово = сам.слова_модуля[цСчётСлова]
			слово._Номер_Уст(цСчётСлова)
			слова_секции[цСчётСлова] = слово
		сам.слова_секции = слова_секции

		слова_модуля = {}  # будущий словарь тегов
		счёт = 0
		# Пропускаем заголовок секции
		for цСчётСлова in range(сам.слово_конец.номер+1, len(сам.слова_модуля)):
			слово = сам.слова_модуля[цСчётСлова]
			слово._Номер_Уст(счёт)
			слова_модуля[счёт] = слово
			счёт += 1
		сам.слова_модуля = {}
		сам.слова_модуля = слова_модуля

	def СловаМодуль_Печать(сам):
		"""
		Печатает все слова, оставшиеся модулю
		"""
		for ключ in сам.слова_модуля:
			слово = сам.слова_модуля[ключ]
			print(слово)

	def СловаСекции_Печать(сам):
		"""
		Печатает все слова, доставшиеся импорту
		"""
		for ключ in сам.слова_секции:
			слово = сам.слова_секции[ключ]
			print(слово)

	@property
	def модуль(сам):
		сам.__модуль

	@property
	def цСловаМодуляВсего(сам):
		return len(сам.слова_модуля)

	@property
	def слова_модуль(сам):
		return сам.слова_модуля
