"""
Модуль определяет разбор секции типов.
"""

if True:
   from пакКомпилер.пакТег import тТег
   from .модТип import тТип

class тТипы:
   def __init__(self, root, теги):
      self.__root = root
      
      усл = type(теги) == dict
      _текст = "В секцию типов должен передаваться словарь тегов, type="+str(type(теги))
      root.конс.Контроль(усл, _текст)
      self.__теги = теги # все теги исходника
      
      self.__теги_типы = {} #  Все теги секции TYPE
      self.__типы = {} # хитрый словарь по каждому типу
      self.__бТипы = False # Признак наличия типов
      self.ошибка = root.ошибка
      
   def __ЕслиТипы(self):
      """
      Первый тег в списке тегов должен быть TYPE.
      Если нет -- значит в исходнике нет описания типов.
      """
      тег = self.__теги[0]
      if тег.имя =='TYPE':
         # укоротить типы
         теги = {}
         for счёт in range(1, len(self.__теги)):
            тег = self.__теги[счёт]
            тег._Номер_Уст(счёт-1)
            теги[счёт-1] = тег
         self.__теги = {}
         self.__теги = теги
         бВыход = True
      else:
         бВыход = False
      self.__бТипы = бВыход
      return бВыход

   def __ЕслиТипыПусто(self):
      """
      Может быть следующий тег:   ; VAR PROCEDURE BEGIN (* END модуля уже отброшено *)
      Секция TYPE может быть пустой, но если есть типы, они должны заканчиваться на ;
      """     
      root = self.__root
      
      тег = self.__теги[0] # первый тег после TYPE, а сам TYPE уже распознан и отброшен
      
      усл = type(тег) == тТег
      _текст = "Тег должен быть тТег, type="+str(type(тег))
      root.конс.Контроль(усл, _текст)
      # проверим на внезапный конец секции
      маркер = (тег.имя == "VAR") or (тег.имя == "PROCEDURE") or (тег.имя == "BEGIN")
      бПусто = True
      if маркер: # секция типизации пустая
         self.__бТипы = False
      else:
         бПусто = False
      return бПусто

   def __ЕслиТипыОграничено(self):
      """
      Ищет разделитель окончания типов.
      Сканируем теги все подряд.
      Может быть следующий тег-маркер окончания: VAR PROCEDURE BEGIN
      Первый тег всегда должен быть именем типа и не может быть маркером
      Произвольный тег может быть ";" и не может быть маркером
      """
      def Маркер():
         return (тег.имя == "VAR") or \
               (тег.имя == "PROCEDURE") or \
               (тег.имя == "BEGIN")
               
      root = self.__root
      тег_всего = len(self.__теги)
      тег_счёт = 0 # первый тег после TYPE, а сам TYPE уже распознали и отбросили
      тег = self.__теги[тег_счёт]
      маркер = Маркер()
      while (not маркер) and (тег_счёт < тег_всего):
         тег_счёт += 1
         тег = self.__теги[тег_счёт]
         
         усл = type(тег) == тТег
         _текст = "Тег должен быть тТег, type="+str(type(тег))
         root.конс.Контроль(усл, _текст)
         маркер = Маркер()
      тег_счёт -= 1
      тег = self.__теги[тег_счёт]
      self.__тег_конец = тег
      # Проверка на окончание секции типов
      if тег.имя !=";":
         self.ошибка.Печать("Тег должен быть ';', тег="+тег.имя)

   def __Теги_Получить(self):
      """
      Выбирает теги по секции типов.
      Дальше работает только с ними.
      """
      теги = {}  # будущий словарь тегов
      for счёт_типы in range(0, self.__тег_конец.номер+1): # TYPE уже отброшено
         тег = self.__теги[счёт_типы]
         тег._Номер_Уст(счёт_типы)
         #print("т+", счёт_типы, "num",тег.номер, тег.имя)
         теги[счёт_типы] = тег
      self.__теги_типы = теги

      теги = {}  # будущий словарь тегов
      счёт = 0
      for счёт_типы in range(self.__тег_конец.номер+1, len(self.__теги)):
         тег = self.__теги[счёт_типы]
         тег._Номер_Уст(счёт)
         #print("т-", счёт_типы, тег.номер, тег.имя)
         теги[счёт] = тег
         счёт += 1
      self.__теги = {}
      self.__теги = теги

   def __Тип_База(self, счёт, тег_база):
      """
      Вычисляет базу для типа
      """
      база_имя = ""
      if тег_база.имя == ";": # У типа нет базы
         счёт += 1
      elif тег_база.имя == "(": # У типа есть база
         счёт += 1
         тег_база = self.__теги_типы[счёт]
         база_имя = тег_база.имя
         счёт += 1
         тег_база = self.__теги_типы[счёт]
         if тег_база.имя != ")":
            self.ошибка.Коорд("Ошибка в определении базы типа", тег_база.коорд, тег_база.стр)
         счёт +=1
      else:
         self.ошибка.Коорд("Ошибка в определении типа", тег_база.коорд, тег_база.стр)
      
      return счёт, база_имя
      
   def __Типы_Разделить(self):
      """
      У нас уже есть словарь типов. Теперь их надо разбить на части.
      Тег 1 -- имя
      Тег 2 -- =
      Тег 3 -- варианты: POINTER, RECORD, ARRAY
      Дальше варианты по порядку следования тегов.
      Необходимо контролировать "=" -- это означает начало нового типа.
      Необходимо контролировать "END;" -- окончание типа.
      """
      def ЕслиИмяТипа():
         счёт = 0
         тег_имя = self.__теги_типы[счёт]
         print("Имя типа =", тег_имя.имя)
         if not тег_имя.ЕслиИмя():
            self.ошибка.Коорд("Неправильное имя типа в определении", тег_имя.коорд, тег_имя.стр)
         self.__счёт = счёт
      
      def ЕслиЭкспорт():
         счёт = self.__счёт
         счёт += 1
         тег_эксп = self.__теги_типы[счёт]
         if тег_эксп.имя == "*":
            бЭкспорт = True
            счёт += 1
            тег_эксп = self.__теги_типы[счёт]
            print("   бЭкспорт = True")
         else:
            бЭкспорт = False
         self.__тег_эксп = тег_эксп
         self.__счёт = счёт
      
      def ЕслиОпределить():
         тег_опр = self.__тег_эксп
         счёт = self.__счёт
         if тег_опр.имя == "=":
            счёт += 1
         else:
            строка = self.__root.исх.строки(тег_опр.коорд.стр) 
            print(self.__root.исх.строки(тег_опр.коорд.стр), строка)
            self.ошибка.Коорд("Отсутствует определитель (=) в объявлении типа", тег_опр.коорд, строка)
         self.__счёт = счёт
         
      def РодТипа():
         def Запись_База():
               счёт += 1
               тег_база = self.__теги_типы[счёт]
               print(5, тег_база.имя)
               тег_база, счёт = self.__Тип_База(счёт, тег_база)
               print(6, тег_эксп.имя)
         def Указатель_База():
            def ЕслиТО():
               счёт = self.__счёт
               счёт += 1
               тег_указ = self.__теги_типы[счёт]
               #print("Тег <ТО>", тег_указ.имя)
                  
               # Кючевое слово TO
               if тег_указ.имя != "TO":
                  строка = self.__root.исх.строки(тег_указ.коорд.стр) 
                  print(self.__root.исх.строки(тег_указ.коорд.стр), строка)
                  self.ошибка.Коорд("Неполный квалификатор указателя типа", тег_указ.коорд, строка)
               self.__счёт = счёт
            def ВилкаМодульТочкаТип():
               счёт = self.__счёт
               счёт += 1
               тег_указ = self.__теги_типы[счёт]
               #print("Раздел: ", тег_указ.имя)
                  
               # Теперь вилка -- может быть имя модуля, а может и имя собственное.
               if not тег_указ.ЕслиИмя():
                  строка = self.__root.исх.строки(тег_указ.коорд.стр) 
                  print(self.__root.исх.строки(тег_указ.коорд.стр), строка)
                  self.ошибка.Коорд("Неверное имя базового типа или его модуля для указатели", тег_указ.коорд, строка)
               
               
               # Теперь может быть точка
               счёт +=1
               тег_разд_база = self.__теги_типы[счёт]
               #print(9, " =тег_разд_база= '"+тег_разд_база.имя+"'")
               if тег_разд_база.имя == ".":
                  тег_база_модуль = тег_разд_база
                  счёт += 1
                  # имя базового типа в модуле
                  тег_база_тип = self.__теги_типы[счёт]
                  print("   Модуль     : "+тег_указ.имя+"'")
                  print("   Базовый тип: "+тег_база_тип.имя+"'")
               # Может быть уже разделитель типов
               elif тег_разд_база.имя == ";":
                  счёт += 1
                  тег_база_тип = self.__теги_типы[счёт]
               # Может быть имя члена
               elif тег_разд_база.ЕслиИмя():
                  счёт += 1
                  тег_база_тип = self.__теги_типы[счёт]
               # Все варианты испробованы -- запрещённая сущноть
               else:
                  строка = self.__root.исх.строки(тег_разд_база.коорд.стр) 
                  print(self.__root.исх.строки(тег_разд_база.коорд.стр), строка)
                  self.ошибка.Коорд("Неверный разделитель в определении базы типа", тег_разд_база.коорд, строка)
               # Имя типа в другом модуле должно быть именем
               if not тег_база_тип.ЕслиИмя():
                  строка = self.__root.исх.строки(тег_база_тип.коорд.стр) 
                  print(self.__root.исх.строки(тег_база_тип.коорд.стр), строка)
                  self.ошибка.Коорд("Неверное имя базового типа в другом модуле", тег_база_тип.коорд, строка)
               self.__счёт = счёт
             
            ЕслиТО()
            # Квалификатор указтеля верный. Должно быть имя типа или модуля
            ВилкаМодульТочкаТип()
            
         def ЕслиМассив():
            счёт += 1
            тег_массив = self.__теги_типы[счёт]
            # должно быть число
         счёт = self.__счёт
         тег_род = self.__теги_типы[счёт]
         print("   Род типа:", тег_род.имя)
         if тег_род.имя in ["RECORD", "POINTER", "ARRAY"] or тег_род.ЕслиИмя():
            if тег_род.имя == "RECORD":
               Запись_База()
            elif тег_род.имя == "POINTER":
               Указатель_База()
            elif тег_род.имя == "ARRAY":
               ЕслиМассив()
            else: # здесь может быть базовый или пользовательский тип
               тег_род = тег_класс
         else:
            строка = self.__root.исх.строки(тег_род.коорд.стр)
            self.ошибка.Коорд("Неверный квалификатор рода типа", тег_род.коорд, строка)
      # 1. Посмотрим что у нас вообще есть.
      # self.__ТегиТипы_Печать()
      # 2. Первый тег должен быть имя
      ЕслиИмяТипа()
      
      # 3. Второй тег должен быть "*" или "="
      ЕслиЭкспорт()
      
      # 4. теперь тег точно "="
      ЕслиОпределить()
      
      # 5. Вычисляем какого класса тип
      РодТипа()

   def __Теги_Печать(self):
      print("\nтТипы.Теги_Печать()")
      for keys in self.__теги:
         тег = self.__теги[keys]
         print(тег)

   def __ТегиТипы_Печать(self):
      self.__root.конс.Печать("\nтТипы.ТегиТипы_Печать()")
      for keys in self.__теги_типы:
         тег = self.__теги_типы[keys]
         print(keys, тег)

   def Обработать(self):
      """
      Проводит разбор секции TYPE.
      """
      if self.__ЕслиТипы():
         print("Есть типы!")
         if not self.__ЕслиТипыПусто():
            print("Типы не пустые!")
            #self.Теги_Печать()
            self.__ЕслиТипыОграничено()
            #self.Теги_Печать()
            self.__Теги_Получить()
            #self.Теги_Печать()
            #self.Конст_Печать()
            self.__Типы_Разделить()
      else:
         print("Нет типов!")
