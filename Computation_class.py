# Create a Computation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.
# Create a method called Factorial() which allows to calculate the factorial of an integer n. Integer n as parameter for this method
# Create a method called naturalSum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Integer n as parameter for this method.
# Create a method called testPrime() in the Calculation class to test the primality of a given integer n, n is Prime or Not? Integer n as parameter for this method.
# Create a method called testPrims() allowing to test if two numbers are prime between them. Two integers are prime to one another if they have only 1 as their common divisor. Eg. 4 and 9 are prime to each other.
# Create a tableMult() method which creates and displays the multiplication table of a given integer. Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.
# Create a static listDiv() method that gets all the divisors of a given integer on new list called Ldiv. Create another listDivPrim() method that gets all the prime divisors of a given integer.



class Computation:
    def __init__(self):
        pass
    def Factorial(self,n):
        fact=1
        for i in range(1,n+1):
            fact*=i
        return fact
    def naturalSum(self,n):
        sum=0
        for i in range(1,n+1):
            sum+=i
        return sum
    def testPrime(self,n):
        for i in range(2,int((n/2)+1)):
            if n%i==0:
                return n,"is not a prime number"
                break
            else:
                return n,"is a prime number"
    def tableMult(self,n):
        for i in range(1,11):
            print(n,"*",i,"=",n*i) 
    
    def allTablesMult(self):
        for i in range(1,11):
            for j in range(1,11):
                print(i,"*",j,"=",i*j)

com=Computation()
print(com.allTablesMult)

