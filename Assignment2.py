# Polymorphism consists of two concepts - Method overloading(Compile time polymorphism) and Method overriding(Runtime polymorphism)
# Method overloading
class Area:
    def area(*a):
        print("Hello world")
        if(len(a) == 1)
            print("Area of a circle is",3.14*a[0]*a[0])
        else if(len(a) == 2)
            print("Area of a rectangle is",a[0]*a[1])
        else
            print("Invalid input")

a = Area()
a.area(10)
a.area(20,5)

# Method overriding
class SportsCar:
    def speed(self):
        print("100 km/hr")
    
class Lamberghini(self):
    def speed(self):
        print("150 km/hr")
        
        
s = SportsCar()
s.speed()
l = Lamberghini()
l.speed()