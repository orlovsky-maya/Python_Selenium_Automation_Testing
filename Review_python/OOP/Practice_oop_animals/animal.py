class Animal():
    """Create animal"""

    def __init__(self, name, kind):
        """initialize attributes"""
        self.name = name
        self.kind = kind

    def eat_meat(self):
        print(self.name + ' - ' + self.kind + ' and he eats meat')

    def eat_grass(self):
        print(self.name + ' - ' + self.kind + ' and he eats grass')


animal1 = Animal('cat', 'predator')
animal2 = Animal('dog', 'predator')
animal3 = Animal('cow', 'herbivorous')

print(animal1.name)
animal1.eat_meat()
animal2.eat_meat()
animal3.eat_grass()