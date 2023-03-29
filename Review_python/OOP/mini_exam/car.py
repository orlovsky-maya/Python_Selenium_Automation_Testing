class Car():
    """create class car"""

    def __init__(self, model, year, engine_size, price, run):
        """initialize attributes"""
        self.model = model
        self.year = year
        self.engine_size = engine_size
        self.price = price
        self.run = run
        self.wheels = 4

    def description_car(self):
        """get description car"""
        print(f'The model of the car is {self.model}, year of manufacture is {self.year}, it has engine size '
              f'{self.engine_size} liters, the price is {self.price} rub, the run is {self.run} km, number of wheels'
              f' {self.wheels}')


car1 = Car('Reno Daster', '2020', '2', '2 000 000', '9 000')
car1.description_car()


class Truck(Car):
    """crate subclass Truck"""

    def __init__(self, model, year, engine_size, price, run):
        """initilization atributs of class parents"""
        super().__init__(model, year, engine_size, price, run)
        self.wheels = 8

    def description_track(self):
        """get description track"""
        description = f'{self.model}, year of manufacture is {self.year}, it has engine size ' \
                      f'{self.engine_size} liters, the price is {self.price} rub, the run is {self.run} km, ' \
                      f'number of wheels {self.wheels}'
        return description


track1 = Truck('i - 300', '2019', '5', '5 000 000', '20 000')

print(f'The model of the track is {track1.description_track()}')