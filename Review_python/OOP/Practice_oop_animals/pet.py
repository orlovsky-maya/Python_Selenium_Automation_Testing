class Pet():
    """Create pet"""

    def __init__(self, name, sex, kind, breed, age):
        """initialize attributes"""
        self.name = name
        self.sex = sex
        self.kind = kind
        self.breed = breed
        self.age = age
        self.weight = 20

    def description_pet(self):
        """get description"""
        description = f"The pet's name is {self.name}, it is {self.sex} {self.kind}, his breed is {self.breed}," \
                      f" his age is {self.age} and weight {self.weight} kg."
        print(description)

    def get_kind(self):
        """get kind"""
        print(f'The kind the pet is {self.kind}')

    def get_age(self):
        """get pet's age"""
        print(f'The age of the pet is {self.age}')

    def update_age(self, year):
        """update age of pet"""
        self.age = year

    def update_weight(self, kg):
        """update age of pet"""
        self.weight = kg


class SuperPet(Pet):
    """create super pet"""

    def __init__(self, name, sex, kind, breed, age):
        """initilization atributs of class parents"""
        super().__init__(name, sex, kind, breed, age)
        self.talent = 'fast run'

    def get_talent(self):
        """get talent"""
        print(f'Super abilities: {self.talent}')

    def description_pet(self):
        """get description"""
        description = f"The pet's name is {self.name}, he has a super power: {self.talent}."
        print(description)


SuperPet = SuperPet('Seba', 'female', 'dog', 'bulterier', 10.5)
SuperPet.update_weight(24)
SuperPet.description_pet()
SuperPet.get_talent()
SuperPet.description_pet()

# cat1 = Pet('Murka', 'fimale', 'cat', 'sfinx', '5')
# cat1.description_pet()
# dog1 = Pet('Bobik', 'male', 'dog', 'bulterier', 10, 25)
# dog1.description_pet()
# cat1.get_kind()
# cat1.update_age(8)
# cat1.get_age()
