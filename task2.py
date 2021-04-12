"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class CustomErr(Exception):
    def __init__(self, txt):
        self.txt = txt


def num(expr):
    expr.replace(' ', '')
    return expr.split('/')


entr = input('Введите выражение деления: ')
try:
    n = num(entr)
    try:
        res = float(n[0]) / float(n[1])
    except ZeroDivisionError:
        raise CustomErr('Деление на ноль недопустимо')
except ValueError:
        print("Вы ввели не число")
except CustomErr as err:
        print(err)
else:
        print(f'{entr} = {res}')
