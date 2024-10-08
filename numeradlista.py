def skapa_numererad_lista(cars):

    return "\n".join([f"{i+1}) {car}" for i, car in enumerate(cars)])

cars = ["Porsche 911 Turbo S", "Ferrari LaFerrari", "Lamborghini Revuelto"]

print(skapa_numererad_lista(cars))

