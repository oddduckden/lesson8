"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""

class Warehouse:
    def __init__(self):
        pass

class OfficeEquipment:
    def __init__(self, cost=0, weight=0):
        self.cost = cost
        self.weight = weight


class Printer(OfficeEquipment):
    def __init__(self, cost, weight, model):
        super().__init__(cost, weight)
        self.__model = model

    def label(self):
        print(f'{self.cost}, {self.weight}, {self.__model}')


class Scanner(OfficeEquipment):
    def __init__(self, cost, weight, portability):
        super().__init__(cost, weight)
        self.__portability = portability

    def tag(self):
        print(f'{self.cost}, {self.weight}, {self.__portability}')


class Xerox(OfficeEquipment):
    def __init__(self, cost, weight, items):
        super().__init__(cost, weight)
        self.__items = items

    def label(self):
        print(f'{self.cost}, {self.weight}, {self.__items}')


a = Printer(300, 35, 'laser')
a.label()
b = Scanner(100, 5, False)
b.tag()
c = Xerox(500, 100, ('stapler', 'double-side'))
c.label()
