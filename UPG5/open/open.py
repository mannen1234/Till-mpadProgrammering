import csv
import os
import locale
from time import sleep


def load_data(filename): 
    products = [] 
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            id = int(row['id'])
            name = row['name']
            desc = row['desc']
            price = float(row['price'])
            quantity = int(row['quantity'])
            
            products.append(        # list
                {                    # dictionary
                    "id": id,       
                    "name": name,
                    "desc": desc,
                    "price": price,
                    "quantity": quantity
                }
            )
    return products


def get_product_by_id(products, id):
    for product in products:
        if product["id"] == id:
            return product
    return None


def remove_product(products, id):
    product = get_product_by_id(products, id)
    
    if product:
        products.remove(product)
        return f"Product: {id} {product['name']} was removed"
    else:
        return f"Product with id {id} not found"


def view_product(products, id):
    product = get_product_by_id(products, id)
    if product:
        return f"Visar produkt: {product['name']} {product['desc']}"
    else:
        return "Produkten hittas inte"


def view_products(products):
    header = f"{'Index':<5}{'ID':<5}{'Name':<30}{'Description':<50}{'Price':>10}"
    product_list = [header, '-'*105]  #Lägger till header och separerar

    for index, product in enumerate(products, 1):
        product_info = (f"{index:<5}{product['id']:<5}{product['name']:<30}"
                        f"{product['desc']:<50}{locale.currency(product['price'], grouping=True):>10}")
        product_list.append(product_info)
    
    return "\n".join(product_list)


locale.setlocale(locale.LC_ALL, 'sv_SE.UTF-8')  

os.system('cls' if os.name == 'nt' else 'clear')
products = load_data('db_products.csv')

while True:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')

        print(view_products(products))  #Visa sorterad lista med produkter

        choice = input("\nVill du (V)isa eller (T)a bort en produkt? ").strip().upper()

        if choice in ["V", "T"]:
            index = int(input("Ange produktens indexnummer: "))

            if choice == "V":   # visa
                if 1 <= index <= len(products):  #Se till att indexet ligger inom rätt
                    selected_product = products[index - 1]  #Skaffa produkten med hjälp av index
                    id = selected_product['id']  #Extrahera produktens ID
                    print("\n" + view_product(products, id))  #Ta bort produkten med ID
                    done = input("\nTryck Enter för att fortsätta...")

                else:
                    print("Ogiltig produkt")
                    sleep(0.3)

            elif choice == "T":  # ta bort
                if 1 <= index <= len(products):  #Se till att indexet ligger inom rätt/ Samma sak
                    selected_product = products[index - 1]  #Skaffa produkten med hjälp av index/ Samma sak
                    id = selected_product['id']  #Extrahera produktens ID/ Samma sak

                    print(remove_product(products, id))  #Ta bort produkten med ID/ Samma sak
                    sleep(0.5)            

                else:
                    print("Ogiltig produkt")
                    sleep(0.3)
        
    except ValueError:
        print("Välj en produkt med siffror")
        sleep(0.5)
