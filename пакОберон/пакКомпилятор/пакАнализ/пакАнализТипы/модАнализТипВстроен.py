# coding:utf8
"""
Модуль описывает тип-алиас встроенного типа.
"""

if True:
	from пакОберон.пакКомпилятор.пакСущность.пакРод import тРод
	from пакОберон.пакКомпилятор.пакСущность.пакСлово import тСлово
	from . модАнализТипБазовый import тАнализТипБазовый

class тАнализТипВстроен(тАнализТипБазовый):
	def __init__(сам, пОберон, пДанные):
		сам.__оберон = пОберон
		сам.__конс = пОберон.конс

		сам.__бОшВнутр = False
		сам.__бОшИсх = False

		тАнализТипБазовый.__init__(сам, пОберон, пДанные)

		if сам.бОшВнутр_АнализТипБазовый:
			сам.__конс.ОшВнутр("тАнализТипВстроенный.__init__(): ошибка компилятора. При вызове тАнализТипБазовый")
			return

		сам.Имя_Проверить()
		сам.бЭкспорт_Проверить()
		сам.Определитель_Проверить()
		сам.бУказатель_Проверить()
		сам.__Тип_Проверить()
		# Здесь нет END, сразу ";"
		сам.Разделитель_Обрезать()

	def __Тип_Проверить(сам):
		"""
		Проверяет не является ли тип алиасом встроенного типа.
		Сейчас у сам.тип выставлено слово, описывающее его тип-алиас
		"""
		слово_тип = сам.слова_секции[0]
		строка_тип = слово_тип.Проверить()
		if строка_тип == "BOOLEAN":
			сам.Предок_Уст("BOOLEAN")
		elif строка_тип == "CHAR":
			сам.Предок_Уст("CHAR")
		elif строка_тип == "INTEGER":
			сам.Предок_Уст("INTEGER")
		elif строка_тип == "REAL":
			сам.Предок_Уст("REAL")
		elif строка_тип == "BYTE":
			сам.Предок_Уст("BYTE")
		elif строка_тип == "SET":
			сам.Предок_Уст("SET")
		else:
			сам.__бОшИсх = True
			стрОш =  "тАнализТипВстроен: неизвестный встроенный предок" + слово_тип.стрИсх
			сам.__конс.Ошибка(стрОш)
			return
		# обрежем род типа
		сам.СловаСекции_Обрезать()

	@property
	def бОшВнутр(сам):
		return сам.__бОшВнутр

	@property
	def бОшИсх(сам):
		return сам.__бОшИсх
