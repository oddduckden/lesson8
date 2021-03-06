"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""
class MyComplex:
    def __init__(self, re, bi):
        self.re = re
        self.bi = bi

    def __add__(self, other):
        return MyComplex(self.re + other.re, self.bi + other.bi)

    def __mul__(self, other):
        return MyComplex(self.re * other.re - self.bi * other.bi, self.bi * other.re + self.re * other.bi)

    def __str__(self):
        return f'({self.re}+{self.bi}j)'



a = complex(5, 6)
b = complex(7, 8)
print(f'{a} + {b} = {a + b}')
print(f'{a} * {b} = {a * b}')
c = MyComplex(5, 6)
d = MyComplex(7, 8)
print(f'{c} + {d} = {c + d}')
print(f'{c} * {d} = {c * d}')