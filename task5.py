"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.
"""


class Warehouse:
    def __init__(self):
        self.__maxnumber = 6
        self.__items = {Printer: [], Scanner: [], Xerox: []}
        self.__vocub = {'Printer': Printer, 'Scanner': Scanner, 'Xerox': Xerox}
        self.__distribute = {Printer: [], Scanner: [], Xerox: []}

    def add(self, item):
        if sum([len(self.__items[x]) for x in self.__items.keys()]) <= self.__maxnumber:
            for __clss in self.__items.keys():
                if isinstance(item, __clss):
                    self.__items[__clss].append(item)
                    print(f'Поступил на склад: {item}')
        else:
            print('на складе нет места')

    def distribute(self, item, department, value):
        __clss = self.__vocub[item]
        for el in self.__items[__clss]:
            if el.get_param() == value:
                self.__items[__clss].remove(el)
                self.__distribute[__clss].append(el)
                el.department = department
                print(f'Выдан: {el} в {el.department}')
                return
        print(f'Данная позиция на складе отсутствует: {(item, value)}')


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
print('Заказан: Принтер для бухгалтерии. ', end='')
w.distribute('Printer', 'accounts', 'B&W')
print('Заказан: Сканер для директора. ', end='')
w.distribute('Scanner', 'CEO', False)
print('Заказан: Сканер для бухгалтерии. ', end='')
w.distribute('Scanner', 'accounts', False)
