class Bird:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Bird({self.name}, {self.age})'

    def fly(self):
        print("새는 날 수 있다.")

class Parrot(Bird):
    def __init__(self,name,age,words):
        super().__init__(name,age)
        self.words = words

    def __repr__(self):
        return f'Parrot({self.name}, {self.age}, {self.words})'

    def fly(self):
        print("앵무새는 말을 할 수 있으며, 날 수 있다.")

class Penguin(Bird):
    def __init__(self, name, age, divingTime):
        super().__init__(name,age)
        self.divingTime = divingTime

    def __repr__(self):
        return f'Penguin({self.name}, {self.age}, {self.divingTime})'

    def fly(self):
        print("펭귄은 수영을 잘하지만, 날 수 없다.")