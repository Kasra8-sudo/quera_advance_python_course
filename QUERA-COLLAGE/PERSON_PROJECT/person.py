import math


class Person:
    instances = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.level = 1
        self.job = ''
        self.work_place = None
        Person.instances.append(self)

    def do_level(self, incom):
        return incom * math.sqrt(self.level*self.work_place.level)

    def calc_income(self):
        pass

    def calc_life_cost(self):
        pass

    def calc(self):
        income = self.calc_income()
        cost = self.calc_life_cost()
        return self.do_level(income) - cost

    def get_job(self):
        return self.job

    def upgrade(self):
        self.level += 1

    @staticmethod
    def calc_all():
        result = 0
        for i in Person.instances:
            result += Person.calc(i)
        return result


class WorkPlaceIsFull(Exception):

    def __str__(self):
        return "work place is full!"


class Consts:
    # You can change these numbers to your custom prices
    BASE_PRICE = {'worker': 200, 'teacher': 150, 'engineer': 250}
    BASE_COST = {'worker': 200, 'teacher': 150, 'engineer': 300}
    BASE_INCOME = {'worker': {'mine': 800, 'school': 500, 'company': 600},
                   'teacher': {'mine': 400, 'school': 900, 'company': 700},
                   'engineer': {'mine': 1000, 'school': 800, 'company': 900}}
    MIN_AGE = 5
    AGE_MUL = 5
    BASE_PLACE_COST = 1000
    LEVEL_MUL = 10

class WorkPlace:
    instances = []

    def __init__(self, name: str):
        self.name = name
        self.level = 1
        self.expertise = ""
        self.employees = []
        self.capacity = 1
        WorkPlace.instances.append(self)

    def get_price(self) -> int:
        return Consts.BASE_PRICE[self.expertise]

    def calc_costs(self):
        pass

    def calc_capacity(self):
        pass

    def upgrade(self):
        self.level += 1
        self.calc_capacity()

    def hire(self, person: Person):
        if len(self.employees) >= self.capacity:
            raise WorkPlaceIsFull()
        else:
            self.employees.append(person)
            person.work_place = self

    def get_expertise(self) -> str:
        return self.expertise

    def calc(self) -> int:
        return -1 * (self.calc_costs())

    @staticmethod
    def calc_all() -> int:
        result = 0
        for i in WorkPlace.instances:
            result += WorkPlace.calc(i)
        return result
