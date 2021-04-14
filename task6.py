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
        self.__distribute = {Printer: [], Scanner: [], Xerox: []}
        self.__overload = []

    def add(self, item):
        if sum([len(self.__items[x]) for x in self.__items.keys()]) <= self.__maxnumber:
            for __clss in self.__items.keys():
                if isinstance(item, __clss):
                    self.__items[__clss].append(item)
                    print(f'Поступил на склад: {item}')
        else:
            print('на складе нет места')
            self.__overload.append(item)

    def distribute(self, item, department, value):
        __clss = self.__vocub[item]
        for el in self.__items[__clss]:
            if el.get_param() == value:
                self.__items[__clss].remove(el)
                self.__distribute[__clss].append(el)
                el.department = department
                print(f'Выдан: {el} в {el.department}')
                w.check_overload()
                return
        print('Данная позиция на складе отсутствует')

    def check_overload(self):
        if self.__overload:
            w.add(self.__overload.pop(0))


class OfficeEquipment:
    def __init__(self, model, cost):
        self.model = model
        self.cost = cost
        self.department = ''


class Printer(OfficeEquipment):
    def __init__(self, model, cost, options):
        super().__init__(model, cost)
        self.__options = options

    def __str__(self):
        return f'{self.model}, {self.cost}, {self.__options}'

    def get_param(self):
        return self.__options


class Scanner(OfficeEquipment):
    def __init__(self, model, cost, portability):
        super().__init__(model, cost)
        self.__portability = portability

    def __str__(self):
        return f'{self.model}, {self.cost}, {self.__portability}'

    def get_param(self):
        return self.__portability


class Xerox(OfficeEquipment):
    def __init__(self, model, cost, feature):
        super().__init__(model, cost)
        self.__feature = feature

    def __str__(self):
        return f'{self.model}, {self.cost}, {self.__feature}'

    def get_param(self):
        return self.__feature


ddct = {'Printer': Printer, 'Scanner': Scanner, 'Xerox': Xerox}
add_list = [('Printer', 'HP LaserJet', 300, 'B&W', 2), ('Scanner', 'Canon lide 400', 100, False, 1),
            ('Xerox', 'Kyocera 3551', 500, 'double-side', 1), ('Printer', 'HP Inkjet', 100, 'Color', 1),
            ('Printer', 'HP laserJet', 300, 'B&W', 2), ('Printer', 'Canon ip6500', 400, 'Color', 1)]
w = Warehouse()
for i in add_list:
    for n in range(i[-1]):
        c = ddct[i[0]](i[1], i[2], i[3])
        w.add(c)
print('Заказан: Принтер в бухгалтерию, черно-белый. ', end='')
w.distribute('Printer', 'accounts', 'B&W')
print('Заказан: Принтер в маркетинг, цветной. ', end='')
w.distribute('Printer', 'marketing', 'Color')
print('Заказан: Принтер в отдел разработки, цветной. ', end='')
w.distribute('Printer', 'R&D', 'Color')
print('Заказан: Сканер для директора. ', end='')
w.distribute('Scanner', 'CEO', False)
# c = Printer('Canon ip6500', 400, 'Color')
# w.add(c)
print('Заказан: Сканер в бухгалтерию. ', end='')
w.distribute('Scanner', 'accounts', False)
print('Заказан: Принтер в отдел разработи, цветной. ', end='')
w.distribute('Printer', 'R&D', 'Color')
