'''21.04.2026 Декораторы (паттерн проектирования)
1. Расширение поведения без измен. существ. кода
2. Когда необх. расширить функционал  не прибегая к наследованию'''





'1.Ф-ция как объект первого класса'
# def greet(name):
#     return f'Hello, {name}'
#
# my_fanc = greet
# print(my_fanc('Имя1'))





'2.Замыкание - прототип декоратора'
# def outer_function(x):
#     def inner_function(y):
#         return x + y
#     return inner_function
#
# add_five = outer_function(5)
# print(add_five(3))





'Базовый пример декоратора'

# def my_decorator(say_hello):
#     def wrapper():  #Вместо wrapper можно использовать другое имя
#         print('Что-то происходит перед вызовом функции')
#         say_hello()
#         print('Что-то происходит после вызова функции')
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print('Hello!')
#
# say_hello()





'Эквивалент без синтаксиса @'

# def my_decorator(func): #Название func- это фактически, наша ф-ция
#     def wrapper():
#         print('Что-то происходит перед вызовом функции')
#         func()
#         print('Что-то происходит после вызова функции')
#     return wrapper
#
#
# def say_hello():
#     print('Hello!')
#
# say_hello = my_decorator(say_hello)
# say_hello()





'Декоратор для функции с аргументом'

# def smart_divide(func):
#     def wrapper(*args):
#         print(f'Вызывается ф-ция {func.__name__} c аргументами {args}')
#         result = func(*args)
#         print(f'Результат: {result}')
#         return result
#     return wrapper
#
# @smart_divide
# def divide(a, b):
#     return a / b
#
# divide(10, 2)
#
#
# @smart_divide
# def summ(*args):
#     return sum(args)
#
# summ(1,2,3,4,5,6)





'''Декораторы с параметрами'''

# def repeat(num_times):
#     def decorator_repeat(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator_repeat
#
# @repeat(num_times = 2)
# def greet(name):
#     print(f'Hello {name}')
#
# greet('World')





'''Несколько декораторов'''
# def decorator1(func):
#     def wrapper(): #Вместо wrapper можно использовать другое имя
#         print('Декоратор1 - до')
#         func()
#         print('Декоратор1 - после')
#     return wrapper
#
# def decorator2(func):
#     def wrapper():  # Вместо wrap
#         print('Декоратор2 - до')
#         func()
#         print('Декоратор2 - после')
#     return wrapper
#
# @decorator1
# @decorator2
# def my_function():
#     print('Основная ф-ция')
#
# my_function()




'''Сохранение метаданных ф-ции'''
# def my_decorator(func):
#     def wrapper():
#         '''Документация wrapper'''
#         return func()
#     return wrapper
#
# @my_decorator
# def original_func():
#     '''Документация original_func'''
#     pass
#
# print(original_func.__name__) #wrapper
# print(original_func.__doc__) #Документация wrapper



'''Специальный модуль functools'''
# from functools import wraps
#
# def my_decorator(func):
#     @wraps(func)
#     def wrapper():
#         '''Документация wrapper'''
#         return func
#     return wrapper
#
# @my_decorator
# def original_func():
#     '''Документация original_func'''
#     pass
#
# print(original_func.__name__) #документация original_func
# print(original_func.__doc__)




# import time
# from functools import wraps
#
# def timer(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time() # time.time - берет текущее время
#         print(f'Функция {func.__name__} выполнилась {end_time - start_time: .4f} секунд')
#         return result
#     return wrapper()
#
# @timer
# def slow_function():
#     time.sleep(2)
#     return 'Готово!'


'''Задача'''
# import time
# arr = [1, 10, 6, 4, 9, 200, 14, 54, 12]
#
# def timer(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         arr = [1, 10, 6, 4, 9, 200, 14, 54, 12]
#         n = len(arr)
#         for i in range(n):
#             for j in range(0, n - 1):
#                 if arr[j] > arr[j + 1]:
#                     arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             start_time = time.time()
#             end_time = time.time()
#             print(f'Функция {func.__name__} выполнилась {end_time - start_time: .4f} секунд')
#
#         return arr
#
# @timer
# def slow_function():
#     time.sleep(10)


'''Задача 1'''
# def logger(func):
#     def wrapper(*args):
#         print(f' Имя функции: {func.__name__}, аргументы функции: {args}')
#     return wrapper
#
#
# @logger
# def log(value1, value2):
#     result = value1 + value2
#     return result
#
# log(1,2)




def call_counter(func):
    def wrapper():
        count = 0
        say_hello()
        count =+ 1
        print(f'{func.__name__} вызвалась {count} раз')
    return wrapper


@call_counter
def say_hello():
    print('Hello!')


say_hello()


