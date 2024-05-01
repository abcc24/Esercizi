#Alberto Baccaro

#Esercizio 8-1
def display_message():
    print ("During this lesson I learned to do functions")

#Esercizio 8-2
def favorite_book():
    print ("One of my favorite books is Alice in Wonderland")
favorite_book()

#Esercizio 8-3
def make_shirt(size, text):
    print ("The size of the t-shirt is", size)
    print ("And the sentenze on it is", text)
make_shirt (size="medium", text='"I am Batman"')

#Esercizio 8-4
make_shirt (size="large", text="I love Python")
make_shirt (size="medium", text="I love Python")
make_shirt (size="small", text="I want to go home")

#Esercizio 8-5
def describe_city(name, country):
    print (name, "is in", country)
country: str = "Italy"
describe_city ("Rome", country)
describe_city ("Florence", country)
describe_city ("Bologna", country)

#Esercizio 8-6
def city_country(name_city, country_name):
    print(name_city, country_name)
name_city: str = "Milan"
country_name: str = "Italy"
city_country(name_city, country_name)

#Esercizio 8-7
def make_album(artist, title, songs=None):
    music_album: dict={"name":artist,"song":title}
    print(music_album)
make_album("Springsteen","Born in the USA")
make_album("Freddy Mercury","We will rock you")
make_album("Hans Zimmer","Flight")

#Esercizio 8-8
while True:
    x=input("Nome artista: ")
    y=input("Nome musica: ")
    break
make_album(x,y)

#Esercizio 8-9
short_mess: list = ["I am arrived!", "Do you like coffe?", "You know nothing, Jon Snow"]
def show_message():
    for x in short_mess:
        print(x)
show_message()

#Esercizio 8-10
def send_messages():
    sent_messagges: list = []
    for y in short_mess:
        print(f"The messages are {y}")
        sent_messagges.append(y)
send_messages()

#Esercizio 8-11

#Esercizio 8-12
def sandwich(elem1, elem2, elem3):
    ingredients: list = [elem1, elem2, elem3]
    print(f"The ingredintes are {elem1}, {elem2} and {elem3}")
sandwich("bread","cheese","hamburger")
sandwich("bread","tomato","chicken")
sandwich("bread","carrot","hot-dog")

#Esercizio 8-13
def build_profile(Name ,Age, Eyes, Hair):
    human: dict = {"Name": Name, "Age": Age,"Eyes": Eyes, "Hair": Hair}
    n_list:list = []
    for i in human.values():
        n_list.append(i)
    pas: str = (f"{n_list[0]}, {n_list[1]}, {n_list[2]}, {n_list[3]} ")
    return(pas)

print(build_profile("Alberto" ,32 ,"verdi" ,"castani"))

#Esercizio 8-14
def car(car_name, car_model, car_color, optional):
    car:dict = {"name":car_name ,"model":car_model ,"color":car_color, "optional":optional}
    print(car)

car("BMW" ,"berlina" ,"blu" ,"turbo-jet")

#