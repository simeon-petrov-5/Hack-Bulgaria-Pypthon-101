def mutual(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while (True):
        if (greater % x == 0) and (greater % y == 0):
            mutual = greater
            break
        greater += 1
    return mutual

def simple(x, y):
    while x % 2 == 0 and y % 2 == 0:
        x, y = x / 2, y / 2
    while x % 3 == 0 and y % 3 == 0:
        x, y = x / 3, y / 3
    while x % 5 == 0 and y % 5 == 0:
        x, y = x / 5, y / 5
    return x, y

def mut(a, b, c, d):
    mut = mutual(b, d)
    x, y = a * (mut / b), c * (mut / d)
    return x, y, mut

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator


    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)


    def __repr__(self):
        return self.__str__()


    def __add__(self, other):
        a , b, mutl = mut(self.numerator, self.denominator, other.numerator, other.denominator)
        if a + b == 0:
            return (0)
        if a + b >= mutl:
            return ((a + b)/mutl)
        else:
            return "{} / {}".format((a + b), mut)
    

    def __sub__(self, other):
        a , b, mutl = mut(self.numerator, self.denominator, other.numerator, other.denominator)
        # Why not working?
        if a - b == 0.0:
            return 0
        if a - b >= mutl:
            if a == 0.0 or b == 0.0:
                return 0
            else:
                return ((a - b)/mutl)
        else:
            return "{} / {}".format((a - b), mutl)
    

    def __mul__(self, other):
        num = self.numerator * other.numerator
        denum = self.denominator * other.denominator
        # if a == 0 or b == 0:
        #     return (0)
        if num >= denum:
            return (num/denum)
        else:
            num, denum = simple(num, denum)
            return "{} / {}".format(num, denum)
    

    def __eq__(self, other):
        return self.numerator / self.denominator == other.numerator / other.denominator


a = Fraction(1, 2)
b = Fraction(2, 4)
print(a == b) # True
print(a + b) # 1
print(a - b) # 0
print(a * b) # 1 / 4