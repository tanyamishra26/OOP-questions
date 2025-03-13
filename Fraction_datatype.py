# Fraction DataType
class Fraction:
    #parameterized constructor
    def __init__(self,x,y):
        self.num=x
        self.den=y
        # returns a string representation of class object
    def __str__(self):
        return f"{self.num}/{self.den}"
    # gets triggered when + operator is used
    def __add__(self,other):
        new_num=self.num*other.den+other.num*self.den
        new_den=self.den*other.den
        return f"{new_num}/{new_den}"
    # gets triggered when - operator is used 
    def __sub__(self,other):
        new_num=self.num*other.den-other.num*self.den
        new_den=self.den*other.den
        return f"{new_num}/{new_den}"
    def __mul__(self,other):
        new_num=self.num*other.num
        new_den=self.den*other.den
        return f"{new_num}/{new_den}"
    def __truediv__(self,other):
        new_num=self.num*other.den
        new_den=self.den*other.num
        return f"{new_num}/{new_den}"
    def convert_to_decimal(self):
        return self.num/self.den
fr1=Fraction(3,4)
fr2=Fraction(1,2)

print(fr1+fr2)
print(fr1-fr2)
print(fr1*fr2)
print(fr1/fr2)
print(fr1.convert_to_decimal)