# def Testing(aa):
#
#     aa()
#     print("Inside testing Function")
#     aa()
#
# def  action():
#     print("Action Function")
#
# Testing(action)
#

# from datetime import datetime
#
#
# def log_datetime(func):
#     '''Log the date and time of a function'''
#
#     def wrapper():
#         print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
#         print(f'{"-"*30}')
#         func()
#     return wrapper
#
# @log_datetime
# def daily_backup():
#     print('Daily backup job has finished')
#
# daily_backup()

#### --------------------------------------------------------------------------------

#
# def my_decorator_func(func):
#
#     def wrapper_func(*args, **kwargs):
#         print("before the function")
#         func(*args, **kwargs)
#         print("after the function")
#     return wrapper_func
#
# @my_decorator_func
# def my_func(my_arg):
#     '''Example docstring for function'''
#
#     pass
# # --- Decorators hide the function they are decorating
# print(my_func.__name__)
# print(my_func.__doc__)


def decor1(func):
    def inner():

        x = func()
        print("decor1", x)
        return x * x

    return inner


def decor(func):
    def inner():

        x = func()
        print("decor", x)
        return 2 * x

    return inner


@decor1
@decor
def num():
    return 10


print(num())



