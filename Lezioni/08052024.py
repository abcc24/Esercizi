"""Exercise 4 (Folder 9 ex_4.py)
1. Write a new class called Food, it should have name, price and
description as attributes.
2. Instantiate at least three different foods you know and like.
3. Create a new class called Menu, it should have a list (of Foods) as attribute.
__init__ should take a list of Foods as optional parameters (default=[])
4. Create a addFood() and removeFood() for the Menu
5. Create a few new Food instances. Add each to the Menu using the respective
Method.
6. Add a method printPrices() that list all items on the Menu with their
prices.
7. Add a Menu method getAveragePrice() that returns the average Food
price of the Menu"""

class Food:
    def __init__(self, name: str, price: float, description: str = None):
        self.name = name
        self.price = price
        self.description = description
    
    def __str__(self):
        return f"{self.name} (price: {self.price}, description: {self.description})"

kiwi = Food(name="kiwi", price=2.50, description="green fruit")
pasta = Food(name="pasta", price=1.50, description="good food")
meat = Food(name="meat", price=8.20, description="grllled is fantastic")

salmon = Food(name="salmon", price=6.10, description="swimm in the water")
apple = Food(name="apple", price=2.00, description="red fruit")



class Menu:
    def __init__(self, foods: list [Food] = []):
        self.foods: list [Food] = foods
    
    def addFood(self, new_food):
        self.foods.append(new_food)
    
    def removeFood(self, rem_food):
        self.foods.remove(rem_food)
    
    def getAvgPrice (self):
        total_sum: float = 0
        for y in self.foods:
            total_sum += y.price
        avg_price = total_sum / len(self.foods)
        return avg_price

    def __str__(self) -> str:
        repr: str =""
        for x in self.foods:
            repr += x.__str__() + "\n"
            avg_price: float = self.getAvgPrice()
            repr += "_" * 30 + "\n"
            repr += f"Prezzo medio = {avg_price}"
        return repr



menu = Menu()
menu.addFood(salmon)
menu.addFood(apple)
print(menu)
menu.removeFood(apple)
print(menu)