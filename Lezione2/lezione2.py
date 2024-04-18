#Alberto Baccaro
#18/04/2024
print("Hello World")

# Esercizio 2-3
x: str="Eric"

print(f"Hello {x} would you like to learn some Python today?")

#Esercizio 2-4
name_lower=x.lower()
name_upper=x.upper()
name_title=x.title()
print(name_lower, name_upper, name_title)

#Esercizio 2-5
print('Batman una volta ha detto: "Sono Batman"')

#Esercizio 2-6
famous_person: str="Batman"
message: str='una volta ha detto:"Sono Batman"'

print(famous_person + message)

#Esercizio 2-8
filename: str="python_notes.txt"
e=filename.removesuffix(".txt")
print(e)

#Esercizio 3-1
name_friends: str="Andrea", "Nicholas", "Rebecca",
print(name_friends[0],name_friends[1],name_friends[2])

#Esercizio 3-2
message_friends: str="do you want to play D&D?"
for b in name_friends:
    print(f"{b}, {message_friends}")

#Esercizio 3-3
cars: str="Ferrari","BMW","Fiat"
print(f"I would like to ride a {cars[0]}")
print(f"Have you seen that {cars[1]} near that house?")
print(f"Sorry, I have destroyed your {cars[2]}.")

#Esercizio 3-4
guests: str="John","Hagrid","Tizio"
for a in guests:
    print(f"Hello {a}, you are invited to the party!")