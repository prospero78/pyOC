# coding: utf8
"""
Модуль "Импорт" содержит процедуры анализа возможного импорта модулей.
"""
if True:
	from пакКомпилер.пакСлово import тСлово
	from .модМодульТип import тМодуль
	from пакКомпилер.пакМодуль.пакСекция import тСекция

class тИмпорт(тСекция):
	def __init__(сам, пДанные):
		тСекция.__init__(сам, пДанные)
		сам.ошибка = пДанные['ошибка']
		сам.__модули = {} # Содержит словарь для импорта модулей
		сам.__Обработать()

	def ЕслиИмпорт(сам):
		"""
		Первое слово в списке слов должно быть IMPORT.
		Если нет -- значит в исходнике нет импорта.
		IMPORT не может быть пустым.
		"""
		слово = сам.слова_модуля[0]
		if слово.строка == 'IMPORT':
			сам.бСекцияЕсть = True
			# укоротить слова
			слова_модуля = {}
			for счёт in range(1, len(сам.слова_модуля)):
				слово = сам.слова_модуля[счёт]
				слово._Номер_Уст(счёт-1)
				слова_модуля[счёт-1] = слово
			сам.слова_модуля = {}
			сам.слова_модуля = слова_модуля
		return сам.бСекцияЕсть

	@property
	def модули(сам):
		return сам.__модули

	@property
	def цМодулиВсего(сам):
		return len(сам.__модули)

	def ЕслиИмпортОдин(сам):
		"""
		Проверяет, что ключевое слово IMPORT в модуле встречается один раз
		"""
		цСчётИмпорт = 0
		цСловоНом = 0
		цСловаВсего = len(сам.слова_модуля)
		while цСловоНом < цСловаВсего:
			слово = сам.слова_модуля[цСловоНом]
			цСловоНом += 1
			if слово.строка == 'IMPORT':
				цСчётИмпорт += 1
			if цСчётИмпорт > 1:
				сам.ошибка.Коорд("тИмпорт: IMPORT два раза в одном модуле запрещён", слово.стрИсх)

	def ЕслиИмпортОграничен(сам):
		"""
		Ищет разделитель окончания импорта.
		Должно заканчиваться на ";"
		"""
		слово_врем = None
		бМаркер = False
		цСловоНом = 0 # первое слово_врем после ИМПОРТ, а сам ИМПОРТ уже распознан

		if (not бМаркер):
			цСловоНом += 1
		слово_врем = сам.слова_модуля[цСловоНом]
		assert type(слово_врем) == тСлово, "тИмпорт: Слово должно быть тСлово, type="+type(слово_врем)
		бМаркер = (слово_врем.строка == ";")

		while (not бМаркер) and (цСловоНом < сам.цСловаМодуляВсего):

			if (not бМаркер):
				цСловоНом += 1
			слово_врем = сам.слова_модуля[цСловоНом]
			assert type(слово_врем) == тСлово, "тИмпорт: Слово должно быть тСлово, type="+type(слово_врем)

			бМаркер = (слово_врем.строка == ";")
		if not бМаркер:
			сам.ошибка.Печать( "тИмпорт: секция нигде не заканчивается ")
		сам.слово_конец = слово_врем

	def Импорт_Разобрать(сам):
		"""
		Делает разбор импорта, вычисляет алиасы.
		"""
		while len(сам.слова_секции) > 0:
			модуль = тМодуль(сам)
			сам.__модули[сам.цМодулиВсего] = модуль
			модуль = None

	def __Обработать(сам):
		"""
		Обеспечивает обработку импорта модуля.
		"""
		if сам.ЕслиИмпорт():
			print("Есть импорт!")
			сам.ЕслиИмпортОдин()
			сам.ЕслиИмпортОграничен()
			сам.СловаСекции_Получить()
			сам.Импорт_Разобрать()
