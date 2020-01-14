from random import randint
from car import Car


class UnreliableCar(Car):
    """Initialise the UnreliableCar"""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Reliability check using random"""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        driven_distance = super().drive(distance)
        return driven_distance
