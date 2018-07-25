# coding: utf8
"""
Модуль для анализа секции типов -- тип-переменная
"""

if True:
	from пакОберон.пакКомпилятор.пакСущность.пакСлово import тСлово
	from пакОберон.пакКомпилятор.пакСущность.пакРод import тРод

	from .модАнализТипБазовый import тАнализТипБазовый

class тАнализТипПерем(тАнализТипБазовый):
	def __init__(сам, пДанные):
		тАнализТипБазовый.__init__(сам, пДанные)
		сам.Имя_Проверить()
		print("тАнализТипПерем: 2256 имя типа-переменной=", сам.имя)
		сам.бЭкспорт_Проверить()
		сам.Определитель_Проверить()
		сам.Предок_Проверить()
		# Здесь нет END, сразу за типом ";"
		сам.Разделитель_Обрезать()
