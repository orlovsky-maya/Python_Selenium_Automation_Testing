class Pet():
    """create pet"""

    def __init__(self, name, sex, kind, breed, age, weight):
        """initialize attributes"""
        self.name = name
        self.sex = sex
        self.kind = kind
        self.breed = breed
        self.age = age
        self.weight = weight

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


class SuperCat(Pet):
    """create super cat"""

    def __init__(self, name, sex, kind, breed, age, weight):
        """initilization atributs of class parents"""
        super().__init__(name, sex, kind, breed, age, weight)
        self.talent = 'jump high'
        self.kind = 'cat'

    def get_talent(self):
        """get talent"""
        print(f'Super abilities: {self.talent}')

    def description_cat(self):
        """get description"""
        description = f"The pet's name is {self.name}, he has a super power: {self.talent}."
        print(description)

    def get_kind(self):
        """get kind"""
        print(f'The kind is: {self.kind}')


class SuperDog(Pet):
    """create super dog"""

    def __init__(self, name, sex, kind, breed, age, weight):
        """initilization atributs of class parents"""
        super().__init__(name, sex, kind, breed, age, weight)
        self.talent = 'fast run'
        self.kind = 'dog'

    def get_talent(self):
        """get talent"""
        print(f'Super abilities: {self.talent}')

    def description_dog(self):
        """get description"""
        description = f"The pet's name is {self.name}, his breed is {self.breed}, he has a super power: {self.talent}."
        print(description)

    def get_kind(self):
        """get kind"""
        print(f'The kind is: {self.kind}')