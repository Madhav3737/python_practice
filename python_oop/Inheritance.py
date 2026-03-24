class Animal:
    def __init__(self):
        print("I am an Animal")
    def eat(self):
        print("I can Eat")
    def sleep(self):
        print("I can Sleep")
class Dog(Animal):
    def __init__(self):
        print("I am a Dog")
    #if derived class did not have any init function(contructor) the the parent class init function will be executed
    def Bark(Self):
        print("I can Bark")
class Cat(Animal):
    def __init__(self):
        print("I am Cat")
    def Meow(self):
        print("I can Meow")
dog = Dog()
dog.Bark()
dog.eat()
dog.sleep()
cat = Cat()
cat.Meow()
cat.eat()
cat.sleep()
