import random

class Car:
    def __init__(self):
        self.car_details = {}  # dictionary (ordbok)

    def add_car(self, make, model):
        self.car_details[make] = model
    
    def list_cars(self):
        for i, (make, model) in enumerate(self.car_details.items(), 1):
            print(f"{i}) - {make} - {model}")

    def race(self):
        speeds = {}
        for make, model in self.car_details.items():
            # Slumpar fram en hastighet mellan 200 och 350 km/h
            speed = random.randint(200, 350)
            speeds[(make, model)] = speed
            print(f"{make} {model} kom upp i {speed} km/h")
        
        # Hitta bilen med högst hastighet
        winner = max(speeds, key=speeds.get)
        print(f"\nVinnaren är: {winner[0]} {winner[1]} med en hastighet av {speeds[winner]} km/h!")

car = Car()  # car är ett objekt och vi initierar klassen och den får ett bilmärke

car.add_car("Ferrari", "F40")
car.add_car("BMW", "M5")
car.add_car("Lamborghini", "Aventador")
car.add_car("Honda", "Civic")
car.add_car("Audi", "RS6")
car.add_car("McLaren", "GT")

car.list_cars()
car.race()
