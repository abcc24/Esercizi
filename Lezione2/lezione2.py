#Alberto Baccaro
#18/04/2024
print("Hello World")

# Esercizio 2-3
x: str="Eric"
print(f"Hello {x} would you like to learn some Python today?")
#I inserted the variable 'x' inside the function of the print

#Esercizio 2-4
name_lower=x.lower()
name_upper=x.upper()
name_title=x.title()
print(name_lower, name_upper, name_title)
#I lowered the letters in 'x', then I enlarge them and finally I change them as title

#Esercizio 2-5
print('Batman once said: "I am Batman!"')
#I used the "" inside the print('') to make them visible in output

#Esercizio 2-6
famous_person: str="Batman"
message: str='once said:"I am Batman"'
print(famous_person + message)
#I printed the two variables to make a sentence

#Esercizio 2-8
filename: str="python_notes.txt"
e=filename.removesuffix(".txt")
print(e)
#I removed the prefix from the element "python_notes.txt"

#Esercizio 3-1
name_friends: list=["Andrea", "Nicholas", "Rebecca"]
print(name_friends[0])
print(name_friends[1])
print(name_friends[2])
#I printed each name one at a time

#Esercizio 3-2
message_friends: str="do you want to play D&D?"
for b in name_friends:
    print(f"{b}, {message_friends}")
#I used the list from the exercise 3-1 and printed a sentence usinf a function

#Esercizio 3-3
cars: list=["Ferrari","BMW","Fiat"]
print(f"I would like to ride a {cars[0]}.")
print(f"Have you seen that {cars[1]} near that house?")
print(f"Sorry, I have destroyed your {cars[2]}.")
#I created a list of cars and used 3 different functions for all the cars

#Esercizio 3-4
guests: list=["John","Hagrid","Tizio"]
for a in guests:
    print(f"Hello {a}, you are invited to the party!")
#I create a list of guests to a party and used a cicle 'for' to send invitations

#Esercizio 3-5
print(f"{guests[0]} will not make it to the party.")
guests[0]="Sam"
for a in guests:
    print(f"Hello {a}, you are invited to the party!")
#I used the old list and selected the first guests that will not attend to the party
#from the last exercise and I replaced the first guest of the old list with a new one.
#Then I did a new cicle 'for' with the new name in the list.

#Esercizio 3-6
print(f"{guests[0]}, {guests[1]}, {guests[2]}, I found a bigger table!")
guests.insert(0, "Connor")
guests.insert(2,"Sara")
guests.append("Lara")
for a in guests:
    print(f"Hello {a}, you are invited to the party!")
#I used the 'guests' list of the last exercise and i insert 3 new person
#then I created a new cicle 'for' to invite at the table both the new and the old persons

#Esercizio 3-7 (da vedere meglio)
"""guests: list=["Connor","Sam","Sara","Hagrid","Tizio","Lara"]
print("I'm very sorry guys, but I can invite only two of you...")
for a in guests:
    new_guests=guests.pop()
print(guests)"""

#Esercizio 3-8
locations: list=["Japan", "Canada", "Norway", "Ireland", "New Zeland"]
print(locations)
alph_locations=sorted(locations)
print(alph_locations)# list now is alphabetical
r_alph_locations=sorted(locations, reverse=True)
print(r_alph_locations)# now the list is alphabetical reversed
locations.reverse()
print(locations)# the list is reversed from the original (not alphabetical)
locations.reverse()
print(locations)# now the list returned to the original order
locations.sort()
print(locations)# the list is in an alphabetical order again
locations.sort(reverse=True)
print(locations)# now it is again in an reversed alphabetical order

#Esercizio 3-9
print(f"The number of guests at the party is {len(guests)}")
#I asked how many guests are at the party using the list of exercise 3-6

#Esercizio 3-10
cities: list=["Rome", "Dublin", "Munich", "Toronto"]
cities.pop()
print(cities)# removed the last element of the list
cities.append("New York")
print(cities)# added the new city at the end of the list
cities.remove("Rome")
print(cities)# removed Rome from the list
cities.sort(reverse=True)
print(cities)# give a reversed alphabetical order to the list
cities.sort()
print(cities)# give an alphabetical order
cities.insert(0,"Toronto")
print(cities)# inserted Toronto at the beginning of the list

#Esercizio 6-1
person: dict={"first_name":"Marco","last_name":"Latorre","age":30,"city":"Torino"}
print(person["first_name"],person["last_name"],person["age"],person["city"])
#I created a dictionary and printed each information in it

#Esercizio 6-2
fav_numbers: dict={"Riccardo":3,"Laura":21,"Irene":7,"Davide":100}
print(fav_numbers["Riccardo"])
print(fav_numbers["Laura"])
print(fav_numbers["Irene"])
print(fav_numbers["Davide")
#I created a dictionary and printed all the informations

#Esercizio 6-3
glossary: dict={"sort":"give an alphabetical order","append":"add an element at the end of the list"}
for k, v in glossary.items():
    print(f"{k}: {v}")
#Like in the last exercise i printed the information of the dictionary in a separate way

#Esercizio 6-7
person: dict={"first_name":"Marco","last_name":"Latorre","age":30,"city":"Torino"}
person1: dict={"first_name":"Andrea","last_name":"Bianchi","age":25,"city":"Roma"}
person2: dict={"first_name":"Anna","last_name":"Rossi","age":35,"city":"Napoli"}
people: list=[person, person1, person2]
for x in people:
    print(x)
#I created 3 dictionaries and made a list with all of them. Then I printed all the informations
#in the dictionaries using the list

#Esercizio 6-8
fido: dict={"Pet":"dog","Owner":"Federico"}
mariella: dict={"Pet":"cow","Owner":"Bob"}
fria: dict={"Pet":"cat","Owner":"Roberta"}
pets: list=[fido,mariella,fria]
for x in pets:
    print(x)
#Like in the last exercise i created 3 dictionaries and a list with them in it

#Esercizio 6-9
favorite_places: dict={"Laura":"Japan","Marco":"Germany","Fabio":"Ireland"}
for k, v in favorite_places.items():
    print(f"{k}: {v}")
#I used a cicle 'for' to loop each person in the dictionary

#Esercizio 6-10
fav_numbers: dict={"Riccardo":3,"Laura":21,"Irene":7,"Davide":100}
for k, v in fav_numbers.items():
    print(f"{k}: {v}")
#I used a cicle 'for' on a dictionary to print the informations separately

#Esercizio 6-11
cities: dict={
    "Rome":{"Contry":"Italy","Population":"2,873 million","Fact":"A city with a long history"},
    "London":{"Country":"England","Population":"8,982 million","Fact":"There is a king in the city"},
    "Washington":{"Country":"U.S","Population":"671.803","Fact":"Capital U.S."}
    }
print(cities["Rome"])
print(cities["London"])
print(cities["Washington"])
#I have created 3 dictionaries inside a larger dictionary, then I printed the info of each city

#Esercizio 6-12
fav_numbers: dict={"Riccardo":3,"Laura":21,"Irene":7,"Davide":100}
fav_numbers["Antonio"]=50
fav_numbers.pop("Riccardo")
fav_numbers["Laura"]=30
print(fav_numbers)
#I used the dictionary of exercise 6-2
#First I added Antonio to the dictionary, then I removed Riccardo and I changed the values of Laura
