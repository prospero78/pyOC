"""
Предоставляет класс главного окна
"""

from tkinter import Tk as тОкно, Frame as тРамка

class тОкнГлав(тОкно):
   def __init__(self, root):
      рес = root.рес
      self.__root = root
      тОкно.__init__(self)
      self.title(рес.app['name'])
      self.minsize(400, 300)
   
   def Пуск(self):
      self.mainloop()
