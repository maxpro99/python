# 4. Написать декоратор с аргументом-функцией (callback),
# позволяющий валидировать входные значения функции и
# выбрасывать исключение ValueError, если что-то не так, например:
# ----------
# def val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
# ---------
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?


from functools import wraps


def val_checker1(a):
    def wrapper(func):
        def called(*args):
            if a(*args):
                return func(*args)
            else:
                raise ValueError(f' wrong val {args[0]}')
        return called
    return wrapper


@val_checker1(lambda x: x > 0)
def calc_cube1(x):
    """Cube"""
    return x ** 3


def val_checker(a):
    def wrapper(func):
        @wraps(func)
        def called(*args):
            if a(*args):
                return func(*args)
            else:
                raise ValueError(f'wrong val {args[0]}')
        return called
    return wrapper


@val_checker(lambda x: x > 0)
def calc_cube(x):
    """Cube"""
    return x ** 3


print(calc_cube(2))
print('Вот имя функции которую мы вызывваем', calc_cube.__name__)
print('Но поскольку декоратор не замаскирован, мы получаем имя функции в декораторе')
print(calc_cube1(2))
print('Вот имя функции которую мы вызывваем', calc_cube1.__name__)
print('Но поскольку декоратор замаскирован, мы получаем имя вызываемой функции')
print(calc_cube(2.54))
print(calc_cube(-5))
print(calc_cube(3, 2.54, []))

# Маскировка произведена с помощью functools
# В задании про это ни слова.
#
# Смысл callback в данном примере не ясен.
# Думаю, что вообще такая конструкция может быть полезной
# Только в каких примерах? Не придумал(((
