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
    def __init__(self, model, cost):
        self.model = model
        self.cost = cost
        self.department = ''


class Printer(OfficeEquipment):
    def __init__(self, model, cost, options):
        super().__init__(model, cost)
        self.__options = options

    def label(self):
        print(f'{self.model}, {self.cost}, {self.__options}')


class Scanner(OfficeEquipment):
    def __init__(self, model, cost, portability):
        super().__init__(model, cost)
        self.__portability = portability

    def label(self):
        print(f'{self.model}, {self.cost}, {self.__portability}')


class Xerox(OfficeEquipment):
    def __init__(self, model, cost, feature):
        super().__init__(model, cost)
        self.__feature = feature

    def label(self):
        print(f'{self.model}, {self.cost}, {self.__feature}')


a = Printer('HP LaserJet', 300, 'laser')
a.label()
b = Scanner('Canon lide 400', 100, False)
b.label()
c = Xerox('Kyocera 3551', 500, 'double-side')
c.label()
