"""
Модуль служит для вывода сообщений в консоль.
Подсвечивает разными цветами разные типы.
"""
if True:
	import colorama as мКонс
	from colorama import Fore, Back, Style
	import sys

class тКонсоль:
	def __init__(self, root):
		self.__root = root
		self.рес = root.рес
		мКонс.init(autoreset=True)
		мКонс.ansi.set_title("Oberon-07 compiler")
		self.Шапка()
		#self.Печать("Консоль активирована")

	def Проверить(self, усл, текст):
		if not усл:
			self.Ошибка(текст)

	def Ошибка(self, текст):
		print(Style.NORMAL+Fore.LIGHTYELLOW_EX+Back.RED+текст)
		sys.exit()

	def Печать(self, текст):
		if type(текст) == str:
			print(Style.NORMAL+Fore.WHITE+текст)
		else:
			self.Ошибка("тКонсоль.Печать(): текст должен быть str, type="+str(type(str)))
	
	def Исх_Печать(self, текст):
		print(Style.NORMAL+Fore.GREEN+текст)

	def Шапка(self):
		текст = "\n               " + self.рес.app['name'] + "       \n"
		текст+= "         KBK Techniks ltd. 2018 BSD-2   \n"
		текст+= "         "+self.рес.app['date']+" "+self.рес.app['time']+" "+self.рес.app['build']+" " +self.рес.app['build_num']+"     "
		# это вроде не работает?
		мКонс.ansi.clear_screen()
		# это надо потестить
		#for i in range(300):
		#   мКонс.ansi.clear_line()
		print(Style.BRIGHT+Fore.LIGHTWHITE_EX+Back.LIGHTBLUE_EX+текст)
		print(Style.RESET_ALL)
		print()
