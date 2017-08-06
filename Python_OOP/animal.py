class animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print self.health


animal1 = animal('bob')
animal1.walk().walk().walk().run().run().display_health()

class dog(animal):
    def __init__(self, name):
        super(dog, self).__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self
animal2 = dog('jack')
animal2.walk().walk().walk().run().run().pet().display_health()

class dragon(animal):
    def __init__(self, name):
        super(dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        print 'I am a Dragon'
        super(dragon,self).display_health()

animal3 = dragon('joseph')
animal3.fly().run().display_health()
animal5 = animal('steven')
animal5.pet().fly()
