"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __new__(cls, *args):
        cls.date = args[0]
        return super().__new__(cls)

    @classmethod
    def extrator(cls):
        d = [int(i) for i in cls.date.split('-')]
        if not Date.checher(d):
            return False
        else:
            return True

    @staticmethod
    def checher(date):
        __monthlen = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        if date[1] > 12:
            print('неверный месяц в дате')
        elif date[0] > __monthlen[date[1] - 1]:
            print('неверный день в дате')
        elif date[2] >= 10000:
            print('неверный год в дате')
        else:
            return True
        return False


d = input('Введите дату в формате DD-MM-YYYY: ')
Date(d)
print(Date.extrator())