#!/usr/bin/env python3
'''
Пробуем сделать генератор AST для Оберона-07
'''


if __name__ == '__main__':
   from пакКомпилер import тКомпилер

   def main():
      """
      Запускает весь процесс построения AST.
      """
      комп = тКомпилер()
      комп.Пуск()

   main()
