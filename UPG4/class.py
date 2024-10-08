import os

class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model 
        self.color = color

    def view_car(self):
        return f"{self.make} - {self.model} - ({self.color})"

def list cars():
    for index, car in enumerate(cars, 1)
        print(f"{index} {car.view_car()}")

    def display_cars():
        os.system("cls")
        print("")

cars = []

while True:
    make = input("make: ")
    model = input("model: ")
    color = input("color: ")


    cars.append(Car("Lada", "Kalina", "Yellow"))

    for car in cars:
        print(car.view_car())

    car.view_car("Ferrari", "F40")

    car.list_cars()