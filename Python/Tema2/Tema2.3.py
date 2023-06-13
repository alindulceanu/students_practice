import math
pi=3.14

class Circle:
    def __init__(self, r, a, b):
        self.r =r
        self.a = a
        self.b = b
    def Area(self):
        Area=2*pi*self.r**2
        print(Area)
    def Peremiter(self):
        Peremiter=2*pi*self.r
        print(Peremiter)
    def testBelongs(self, x, y):
        distance = math.sqrt((x - self.a) ** 2 + (y - self.b) ** 2)
        if distance <= self.r:
            print("Inside")
        else:
            print("Outside")
                    
r=int(input("Radius: "))
a=int(input("Center coord a: "))
b=int(input("Center coord b: "))
x=int(input("Point coord x: "))
y=int(input("Point coord y: "))

p1 = Circle(r, a, b)
p1.Area()
p1.Peremiter()
p1.testBelongs(x,y)