"""
Модуль предоставляет тип для хранения имени модуля и его алиаса.
"""

class тМодульИмя:
	def __init__(self, пМодулАлиас, пМодуль, пцНомер):
		assert type(пМодулАлиас) == str, "тМодульИмя.__init__(): Алиас должен быть строкой, type="+type(пМодулАлиас)
		self.__стрАлиас = пМодулАлиас

		assert type(пМодуль) == str, "тМодульИмя.__init__(): Имя модуля должно быть строкой, type="+type(пМодуль)
		assert пМодуль != "", "Имя не может быть пустым"
		self.__стрИмя = пМодуль

		assert type(пцНомер) == int, "тМодульИмя.__init__(): Номер модуля должен быть целым, type="+type(пцНомер)
		self.__цНомер = пцНомер

	@property
	def алиас(self):
		return self.__стрАлиас

	@property
	def имя(self):
		return self.__стрИмя

	@property
	def бАлиас(self):
		if self.__стрАлиас == "":
			бАлиас = False
		else:
			бАлиас = True
		return бАлиас

	@property
	def номер(self):
		return self.__цНомер
