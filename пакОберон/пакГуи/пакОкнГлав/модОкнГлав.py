"""
Предоставляет класс главного окна
"""

from tkinter.tix import Tk as тОкно, Frame as тРамка
from .модРамкаНиж import тРамкаНиж
from .модРамкаВерх import тРамкаВерх
from .модРамкаСред import тРамкаСред

class тОкнГлав(тОкно):
   def __init__(self, root):
      рес = root.рес
      self.__root = root
      тОкно.__init__(self)
      self.title(рес.app['name1']+ " "+рес.app['date']+ " "+рес.app['time']+ " "+рес.app['build']+" "+рес.app['build_num'])
      self.minsize(550, 400)
      self.рамкаВерх = тРамкаВерх(root, self)
      self.рамкаСред = тРамкаСред(root, self)
      self.рамкаНиж = тРамкаНиж(root, self)
      
   def Пуск(self):
      self.mainloop()
