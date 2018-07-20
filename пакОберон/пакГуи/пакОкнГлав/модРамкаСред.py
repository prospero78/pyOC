"""
Рамка содержит элементы средней части окна.
"""

from tkinter import Frame as тРамка, Text as тТекст

class тРамкаСред(тРамка):
   def __init__(self, root, master):
      self.__root = root
      self.__master = master
      тРамка.__init__(self, master)
      self.pack(expand=True, fill='both')
      
      self.текстКод = тТекст(self)
      self.текстКод.pack(expand=True, fill='both')
