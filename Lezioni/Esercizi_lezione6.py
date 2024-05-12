#Alberto Baccaro

#Esercizio 9-1
class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print (f"The name is {self.restaurant_name}, and the cuisine is {self.cuisine_type}")

    def open_restaurant(self):
        print (f"The {self.restaurant_name} restaurant is open!")
    
restaurant = Restaurant(restaurant_name = '"Green Dragon"', cuisine_type = "hobbit")

restaurant.describe_restaurant()
restaurant.open_restaurant()

###

#Esercizio 9-2

restaurant1 = Restaurant(restaurant_name = '"Da Giorgione"', cuisine_type = "THE TRUE CUISINE")
restaurant2 = Restaurant(restaurant_name = '"Lo Zozzone"', cuisine_type = "...")

restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

###

#Esercizio 9-3

class User:
    def __init__(self, first_name: str, last_name: str, age: int, gender: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    
    def describe_user(self):
        print (f"User's first name: {self.first_name}, User's last_name: {self.last_name}, User's age: {self.age}, User's gender: {self.gender}")
    
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, how are you?")
    
user1 = User(first_name = "Sara", last_name = "Trollo", age = 28, gender = "female")
user2 = User(first_name = "Sam", last_name = "Gamgee", age = 40, gender = "male")
user3 = User(first_name = "LALOLA", last_name = "MARAMA", age = 1000, gender = "boh")

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()

###

#Esercizio 9-4

class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str, number_served: int = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    
    def set_number_served(self):
        print(f"The clients served are {self.number_served}")

    def increment_number_served(self):
        self.number_served = 9
        print(f"The clients served are {self.number_served} in a day")

restaurant = Restaurant(restaurant_name = '"Green Dragon"', cuisine_type = "hobbit")

restaurant.set_number_served()
restaurant.increment_number_served()

###

#Esercizio 9-5

class User:
    def __init__(self, first_name: str, last_name: str, age: int, gender: str, login_attempts: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attemps = login_attempts
    
    def increment_login_attempts(self):
        while self.login_attemps < 5:
            self.login_attemps += 1
            print(f"The numbers of login attempts are {self.login_attemps}")

    def reset_login_attempts(self):
        self.login_attemps = 0
        print(f"The numbers of login attempts are None")
    
user1 = User(first_name = "Sara", last_name = "Trollo", age = 28, gender = "female", login_attempts = 1)

user1.increment_login_attempts()
user1.reset_login_attempts()

###

#Esercizio 9-6

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name: str, cuisine_type: str, number_served: int, flavors: list[str] = []):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = flavors

    def display_flavors(self):
        for x in self.flavors:
            print(f"The icecream flavors is {x}")

icecreamstand = IceCreamStand(restaurant_name = "Ice Queen", cuisine_type = "icecream", number_served = 3, flavors = ["chocolate", "vanilla", "mint", "Gargamella"])
icecreamstand.display_flavors()

###

#Esercizio 9-7

class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int, gender: str, login_attempts: int, privileges: list[str] = []):
        super().__init__(first_name, last_name, age, gender, login_attempts)
        self.privileges = privileges

    
    def show_privileges(self):
        for x in self.privileges:
            print(f"The privilages are: {x}")

user1 = Admin(first_name = "Sara", last_name = "Trollo", age = 28, gender = "female", login_attempts = 1, privileges = ["can add post", "can delete post", "can ban user"])
user1.show_privileges()

###

#Esercizio 9-8 (provate diverse soluzioni, ma non funziona)

"""class Privileges ():
    def __init__(self, privileges: list = ["can add post", "can delete post", "can ban user"]):
        self.privileges = privileges
    
    def show_privileges(self):
        for x in self.privileges:
            print(f"The privilages are: {x}")


class Admin(User):
    def __init__(self, first_name: str, last_name: str, age: int, gender: str, login_attempts: int):
        super().__init__(first_name, last_name, age, gender, login_attempts)
        self.privileges = Privileges()
    
    def show_privileges(self):
        for x in self.privileges:
            print(f"The privilages are: {x}")

person1 = Admin (first_name = "John", last_name = "Kent", age = 57, gender = "male", login_attempts = 4)

person1.show_privileges()"""

###

#Esercizio 9-9

"""class Battery:
    def __init__(self, size: int, capacity: int):
        self.size = size
        self.capacity = capacity
    
    def upgrade_battery(self):
        if self.size and self.capacity == 65:
            print(f"The ")"""

#Credo che manchi un pezzo a questo esercizio

###

#Esercizio 9-10

"""from restaurants import Restaurant

restaurant = Restaurant(restaurant_name = '"Green Dragon"', cuisine_type = "hobbit")

restaurant.describe_restaurant()
restaurant.open_restaurant()"""

###

#Esercizio 9-13

import random

class Die:
    def __init__(self, sides: int = 6):
        self.sides = sides
    
    def roll_die(self):
        print(f"The number is {random.randint(1, self.sides)}")

dice_roll_six = Die()

for x in range(10):
    dice_roll_six.roll_die()

dice_roll_ten = Die(sides = 10)

for x in range(10):
    dice_roll_ten.roll_die()

dice_roll_twenty = Die(sides = 20)

for x in range(10):
    dice_roll_twenty.roll_die()

###

#Esercizio 9-14

lottery_list: list = [1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e"]

print(f"The winning ticket contains {random.sample(lottery_list, 4)}")

###

#Esercizio 9-15

lottery_list: list = [1,2,3,4,5,6,7,8,9,10,"a","b","c","d","e"]

win_ticket: list = [1,4,"a",6]

counter: int = 0

while True:
    pull_num = random.sample(lottery_list, 4)
    counter += 1

    if pull_num == win_ticket:
        print(f"Numbers of pulling: {counter}")
        break