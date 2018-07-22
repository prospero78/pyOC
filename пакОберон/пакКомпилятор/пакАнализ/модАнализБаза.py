# coding:utf8
"""
Модуль базового типа для анализа секции для всех секций
"""

if True:
	from пакОберон.пакКомпилятор.пакСущность.пакСлово import тСлово

class тАнализБаза:
	def __init__(сам, пДанные):
		def Анализ_Проверить():
			бУсл = пДанные['анализ'] == "анализ"
			стрОш = "В секцию  должен передаваться словарь слов для анализа"
			assert бУсл, стрОш

		Анализ_Проверить()
		сам.слова_секции = пДанные['слова']

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
		assert пСлово != None, "тАнализ: слово_конец уже установлено" + сам.__слово_конец.стрИсх
		assert type(пСлово) == тСлово, "тАнализ: пСлово должно быть тСлово, type="+str(type(пСлово))
		сам.__слово_конец = пСлово

	@property
	def слово_конец(сам):
		return сам.__слово_конец
