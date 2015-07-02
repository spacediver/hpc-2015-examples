def print_args(fn):
  def printing_args(*args):
    print ('args: ', args)
    return fn(*args)
  return printing_args

# Проверка ниже нужна для того, чтобы примеры выполнялись только когда файл
# decorator.py выполняется как отдельная программа (в терминале: python3 decorator.py), 
# но не когда импортируется как модуль (в интерпретаторе: import decorator). 
# Во втором случае встроенная переменная __name__ (наблюдаемая 
# из интерпретатора как decorator.__name__), будет равна не '__main__', 
# а 'decorator'.
if __name__ == '__main__': 

    # Пример использования (декорирования функции)

    def f(x,y):
      return x+y

    print ('f =', f)
    f_decorated = print_args(f)
    print ('f_decorated =', f_decorated)

    print ('------- f(4,5):')
    print (f(4,5))

    print ('------- f_decorated(4,5):')
    print (f_decorated(4,5))
