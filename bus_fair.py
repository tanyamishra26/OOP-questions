class Vehicle:
    def __init__(self,seating_capacity=50):
        self.seating_capacity=seating_capacity
    def fare(self):
        return self.seating_capacity*100

class Bus(Vehicle):
    def fare(self):
        base_fare=super().fare()
        total_fare=base_fare+(0.1*base_fare)
        return total_fare

bus=Bus(50)
print("The Total fare for the bus is:",bus.fare())
