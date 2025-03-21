# Count number of instance 
class Car:
    instance=0
    def __init__(self):
        Car.instance+=1
maruti=Car()
bmw=Car()
honda=Car()

print("Number of instances created: ",Car.instance)
    