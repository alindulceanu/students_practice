class Calculations:
    def sum(self, x,y):
        return x + y

    def sub(self, x,y):
        return x - y

    def divide(self, x, y):
        return float("{:.2f}".format(x / y))

    def product(self, x, y):
        return float("{:.2f}".format(x * y))

    def power(self, x, y):
        po = x
        for i in range(y - 1):
            po *= x

        return po

    def xRoot(self, x, y):
        try:
            return float("{:.2f}".format(x ** (1 / y)))

        except(ValueError):
            print("can't calculate the root of a negative number")
            return -1