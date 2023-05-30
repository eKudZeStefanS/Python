class Company:
    levels = {
        1: 'junior',
        2: 'middle',
        3: 'senior',
        4: 'lead'
    }

    def __init__(self, index):
        self._index = index
        self._level = Company.levels[index]

    def _level_up(self):
        if self._index != 4:
            self._index += 1
            self._level = Company.levels[self._index]

    def is_lead(self):
        return self._index == 4


class Programmer:
    def __init__(self, name, age, index):
        self.name = name
        self.age = age
        self._company = Company(index)

    def work(self):
        self._company._level_up()

    def info(self):
        print(f'Name: {self.name}, Age: {self.age}, Level: {self._company._level}')

    @staticmethod
    def knowledge_base():
        print('Programming is fun!')


Programmer.knowledge_base()

p = Programmer('Stefan', 21, 1)

while not p._company.is_lead():
    p.work()
    p.info()