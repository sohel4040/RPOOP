# Single inheritance
class Animal:
    def __init__(self, name, legs, eyes):
        self.name = name
        self.legs = legs
        self.eyes = eyes
        
    def walk(self):
        pass
    def eat(self):
        pass
    
class Dog(Animal):
    def __init__(self):
        super().__init__("Dog", 4, 2):
        
    def walk(self):
        print("Dog is walking")
    def eat(self):
        print("Dog eats dog food");
        
#multiple inheritance
class Animal:
    def eat(self):
        print("Animal is eating...")

class Mammal:
    def run(self):
        print("Mammal is running...")

class Bat(Animal, Mammal):
    def fly(self):
        print("Bat is flying...")

b = Bat()
b.eat()  
b.run()  
b.fly()  

#multilevel inheritance
class Shape:
    def __init__(self, color):
        self.color = color

class Square(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

class ColoredSquare(Square):
    def __init__(self, color, side_length):
        super().__init__(color, side_length)

    def display_color(self):
        print(f"This square is {self.color}.")

square = ColoredSquare("blue", 5)
square.display_color()  
print(square.area())

# Heirachical Inheritance
class Animal:
    def __init__(self, name):
            self.name = name
    def eat(self):
        print(f"{self.name} is eating")
        
class Cat(Animal):
    def meow(self):
        print(f"{self.name} says meow")
        
class Dog(Animal):
    def barks(self):
        print(f"{self.name} barks")
        
cat = Cat("Kitty")
dog = Dog("Sheru")

cat.eat()
cat.meow()

dog.eat()
dog.barks()


class Boss:
    def __init__(self):
        print("Boss constructor")
        
class B1(Boss):
    def __init__(self):
        super().__init__()
        print("B1 constructor")
        
class B2(Boss):
    def __init__(self):
        print("B2 constructor")
        
class Child(B1,B2):
    def __init__(self):
        super().__init__()
        print("Child constructor")
        
b = Child()