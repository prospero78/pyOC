"""
Предоставляет класс главного окна
"""

from tkinter.tix import Tk as тОкно, Frame as тРамка #type:ignore
from .модРамкаНиж import тРамкаНиж
from .модРамкаВерх import тРамкаВерх
from .модРамкаСред import тРамкаСред

class тОкнГлав(тОкно):
   def __init__(self, пОберон)->None:
      рес = пОберон.рес
      self.__root = пОберон
      тОкно.__init__(self)
      self.title(рес.app['name1']+ " "+рес.app['date']+ " "+рес.app['time']+ " "+рес.app['build']+" "+рес.app['build_num'])
      self.minsize(550, 400)
      self.рамкаВерх :тРамкаВерх= тРамкаВерх(пОберон, self)
      self.рамкаСред :тРамкаСред= тРамкаСред(пОберон, self)
      self.рамкаНиж :тРамкаНиж= тРамкаНиж(пОберон, self)

   def Пуск(self)->None:
      self.mainloop()
