class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow!")

    def sayColor(self):
        print(self.color)


class Dog(Pet):
    def speak(self):
        print("Woof!")


class Fish(Pet):
    pass


c = Cat("Tim", 34, "Blue")
c.speak()
c.show()
c.sayColor()

d = Dog("Bill", 25)
d.speak()
d.show()

p = Pet("Jill", 50)
p.speak()

f = Fish("Bubbles", 10)
f.speak()
