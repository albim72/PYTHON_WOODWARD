from typing import List,Protocol

class Item(Protocol):
    quantity:float
    price:float

class Product:
    def __init__(self,name:str,quantity:float,price:float):
        self.name = name
        self.quantity = quantity
        self.price = price

def calculate_total(items:List[Item])->float:
    return sum([item.quantity*item.price for item in items])


total = calculate_total([
    Product('A',10,155.5),
    Product('B',2,45.3),
    Product('C',1,22),
    Product('D',6,12.99)
])

print(total)
