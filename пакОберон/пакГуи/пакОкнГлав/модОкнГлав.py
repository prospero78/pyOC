# coding: utf8
"""
Предоставляет класс главного окна
"""

from tkinter.tix import Tk as тОкно, Frame as тРамка #type:ignore
#from .модРамкаНиж import тРамкаНиж
from пакОберон.пакГуи.пакКонсоль import тКонсоль
from .модРамкаВерх import тРамкаВерх
from .модРамкаСред import тРамкаСред
from .модРамкаКоманды import тРамкаКоманды

class тОкнГлав(тОкно):
	def __init__(сам, пОберон)->None:
		рес = пОберон.рес
		сам.__оберон = пОберон
		тОкно.__init__(сам)
		сам.protocol("WM_DELETE_WINDOW", пОберон.дисп.Приложение_Закрыть)
		сам.title(рес.app['name1']+ " "+рес.app['date']+ " "+рес.app['time']+ " "+рес.app['build']+" "+рес.app['build_num'])
		сам.minsize(550, 400)
		сам.рамкаВерх :тРамкаВерх= тРамкаВерх(пОберон, сам)
		сам.рамкаКоманды :тРамкаКоманды= тРамкаКоманды(пОберон, сам)
		сам.рамкаСред :тРамкаСред= тРамкаСред(пОберон, сам)
		#сам.рамкаНиж :тРамкаНиж= тРамкаНиж(пОберон, сам)
		сам.консоль :тКонсоль= тКонсоль(пОберон, сам)

	def Пуск(сам)->None:
		сам.mainloop()
