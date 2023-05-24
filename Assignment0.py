class rectangle:
    def __init__(self, l, b):
        self.l = l;
        self.b = b;
    def area(self):
        print("Area is ",self.l*self.b);
    def perimeter(self):
        print("Perimeter is ", 2*(self.l+self.b))
    def changeDimensions(self, l, b):
        self.l = l;
        self.b = b;
    def reportDimensions(self):
        print("Length is:",self.l,"Breadth is:",self.b)
        
r = rectangle(10,20)
r.area()
r.perimeter()

class Polygon:
    def __init__(self, name, sides):
        self.name = name
        self.sides = sides
        
    def area(self):
        pass
    def perimeter(self):
        pass
    
class rectangle(Polygon):
    def __init__(self, l, b):
        super().__init__("Rectangle", 4)
        self.l = l
        self.b = b
        
    def area(self):
        print("Area is ",self.l*self.b);
    def perimeter(self):
        print("Perimeter is ", 2*(self.l+self.b))
        
        
class square(Polygon):
    def __init__(self, s):
        super().__init__("Square", 4)
        self.s = s
        
    def area(self):
        print("Area is ",self.s*self.s);
    def perimeter(self):
        print("Perimeter is ", 4*(self.s))
class Circle(Polygon):
    def __init__(self, r):
        super().__init__("Circle", 0)
        self.r = r
    
    def area(self):
        print("Area of circle : ", 3.14*self.r*self.r)
        
r = rectangle(10,20)
r.area()
r.perimeter()

s = square(10)
s.area()
s.perimeter()