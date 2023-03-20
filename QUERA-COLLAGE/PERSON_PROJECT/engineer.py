# YOUR IMPORTS GOES HERE
from person import Person , Consts

import math


class Engineer(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.job = 'engineer'

    def get_price(self) -> int:
        return math.floor(Consts.BASE_PRICE.get('engineer') * math.sqrt(Consts.MIN_AGE / self.age))

    def calc_life_cost(self): # oevrride this method in main class
        return math.floor(Consts.BASE_COST[self.job] * math.sqrt(self.age / Consts.MIN_AGE))

    def calc_income(self): # oevrride this method in main class
        return math.floor(Consts.BASE_INCOME[self.job][self.work_place.get_expertise()] * math.sqrt(Consts.MIN_AGE / self.age))


