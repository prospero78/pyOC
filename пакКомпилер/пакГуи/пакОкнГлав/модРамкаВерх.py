"""
Верхняя рамка с кноками меню.
"""

from tkinter import Frame as тРамка, Menubutton as тКнпМну, Menu as тМеню                         

class тРамкаВерх(тРамка):
   def __init__(self, root, master):
      self.__root = root
      тРамка.__init__(self, master, relief='sunken', border=1)
      self.pack(side="top", expand=True, fill='x')
      
      
      self.кнпФайл = тКнпМну(self, text=root.рес.winMain['mnuFile'], relief='raised')
      self.кнпФайл.pack(side='left')
      
      self.мнуФайл = тМеню(self.кнпФайл, tearoff = 0)
      self.мнуФайл.add_command(label=root.рес.winMain['mnuOpen'])
      self.мнуФайл.add_separator()
      self.мнуФайл.add_command(label=root.рес.winMain['mnuExit'])
      
      
      self.кнпФайл['menu'] = self.мнуФайл
