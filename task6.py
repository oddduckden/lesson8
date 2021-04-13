"""
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
уроках по ООП.
"""


class Warehouse:
    def __init__(self):
        self.__maxnumber = 6
        self.__items = {Printer: [], Scanner: [], Xerox: []}
        self.__vocub = {'Printer': Printer, 'Scanner': Scanner, 'Xerox': Xerox}

    def add(self, item):
        if sum([len(self.__items[x]) for x in self.__items.keys()]) <= self.__maxnumber:
            for __clss in self.__items.keys():
                if isinstance(item, __clss):
                    self.__items[__clss].append(item)
                    print(f'Поступил на склад: {item.model}')
        else:
            print('на складе нет места')

    def distribute(self, item, department):
        for el in self.__items[self.__vocub[item]]:
            if getattr(el, 'department') == '':
                setattr(el, 'department', department)
                print(f'Выдан: {el.model}')
                return
        print('Данная позиция на складе отсутствует')


class OfficeEquipment:
    def __init__(self, model, cost):
        self.model = model
        self.cost = cost
        self.department = ''


class Printer(OfficeEquipment):
    def __init__(self, model, cost, options):
        super().__init__(model, cost)
        self.__options = options


class Scanner(OfficeEquipment):
    def __init__(self, model, cost, portability):
        super().__init__(model, cost)
        self.__portability = portability


class Xerox(OfficeEquipment):
    def __init__(self, model, cost, feature):
        super().__init__(model, cost)
        self.__feature = feature


w = Warehouse()
add_list = [Printer('HP LaserJet', 300, 'B&W'), Scanner('Canon lide 400', 100, False),
            Xerox('Kyocera 3551', 500, 'double-side'), Printer('HP Inkjet', 100, 'Color'),
            Printer('HP laserJet', 300, 'Color'), Printer('Canon ip6500', 400, 'Color')]
for i in add_list:
    w.add(i)
print('Заказан: Принтер для бухгалтерии. ', end='')
w.distribute('Printer', 'accounts', )
print('Заказан: Сканер для директора. ', end='')
w.distribute('Scanner', 'CIO')
print('Заказан: Сканер для бухгалтерии. ', end='')
w.distribute('Scanner', 'accounts')
