# coding: utf8
"""
Модуль служит для вывода сообщений в консоль.
Подсвечивает разными цветами разные типы.
"""
if True:
	import colorama as мКонс #type:ignore
	from colorama import Fore, Back, Style
	import sys, os
	import time

class тКонсоль:
	def __init__(сам, пКорень)->None:
		сам.__корень = пКорень
		сам.рес = пКорень.рес
		мКонс.init(autoreset=True)
		мКонс.ansi.set_title("Oberon-07 compiler")
		сам.Шапка()
		#сам.Печать("Консоль активирована")


	def Ошибка(сам, пСообщ:str)->None:
		print(Style.NORMAL+Fore.LIGHTYELLOW_EX+Back.RED+пСообщ)

	def Печать(сам, пСообщ:str)->None:
		if type(пСообщ) == str:
			print(Style.NORMAL+Fore.WHITE+пСообщ)
		else:
			сам.Ошибка("тКонсоль.Печать(): пСообщ должен быть str, type="+str(type(пСообщ)))

	def Исх_Печать(сам, пСообщ:str)->None:
		print(Style.NORMAL+Fore.GREEN+пСообщ)
