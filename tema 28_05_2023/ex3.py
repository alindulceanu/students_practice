"""•Define a Circle class allowing to create a circleC (O, r) with center O(a, b) and radius r using the constructor(parameters inside the consctructor would be r,a,b)

•Define a Area() method of the class which calculates the area of the circle.

•Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

•Define a testBelongs() method of the class which allows to test whether a point A(x, y) belongs to the circle C(O, r) or not."""
import math as m


class Circle:
    def __init__(self, r, a, b):
        self.__r = r
        self.__x = a
        self.__y = b

    def Area(self):
        print(3.14 * self.__r**2)

    def Perimeter(self):
        print(2 * 3.14 * self.__r)

    def testBelongs(self, x, y):
        d = m.sqrt(pow(x - self.__x, 2) + pow(y - self.__y, 2))
        print(d)

        if d <= self.__r:
            print("Apartine cercului!")

        else:
            print("Nu apartine cercului!")


cir = Circle(50, 0, 0)

A = (40, 20)

cir.testBelongs(*A)
