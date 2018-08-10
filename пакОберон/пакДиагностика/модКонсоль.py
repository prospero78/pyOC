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

	def Проверить(сам, пбУсл:bool, пСообщ:str)->None:
		if not пбУсл:
			сам.Ошибка(пСообщ)

	def Ошибка(сам, пСообщ:str)->None:
		print(Style.NORMAL+Fore.LIGHTYELLOW_EX+Back.RED+пСообщ)
		sys.exit()

	def Печать(сам, пСообщ:str)->None:
		if type(пСообщ) == str:
			print(Style.NORMAL+Fore.WHITE+пСообщ)
		else:
			сам.Ошибка("тКонсоль.Печать(): пСообщ должен быть str, type="+str(type(пСообщ)))

	def Исх_Печать(сам, пСообщ:str)->None:
		print(Style.NORMAL+Fore.GREEN+пСообщ)

	def Шапка(сам)->None:
		if sys.platform == "win32":
			os.system("cls")
		else:
			os.system("clear")
		стрСообщ :str= "\n               " + сам.рес.app['name'] + "       \n"
		стрСообщ+= "         KBK Techniks ltd. 2018 BSD-2     \n"
		стрСообщ+= "         "+сам.рес.app['date']+" "+сам.рес.app['time']+" "+сам.рес.app['build']+" " +сам.рес.app['build_num']+"      "
		# это вроде не работает?
		мКонс.ansi.clear_screen()
		# это надо потестить
		#for i in range(300):
		#   мКонс.ansi.clear_line()
		print(Style.BRIGHT+Fore.LIGHTWHITE_EX+Back.LIGHTBLUE_EX+стрСообщ)
		print(Style.RESET_ALL)
		print()
		#time.sleep(2)
