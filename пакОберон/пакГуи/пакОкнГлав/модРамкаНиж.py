# coding: utf8
"""
Предоставляет нижнюю рамку для главного окна. Выводит лог работы программы.
"""

from tkinter import LabelFrame as тРамкаНадпись, Text as тТекст

class тРамкаНиж(тРамкаНадпись):
   def __init__(self, root, master):
      self.__root = root
      тРамкаНадпись.__init__(self, master, text = root.рес.winMain['log'])
      self.pack(side="bottom", expand=True, fill='x')
      self.лог = тТекст(self, relief='sunken', border=3, bg='white', height=10)
      self.лог.pack(expand = True, fill = 'both')
