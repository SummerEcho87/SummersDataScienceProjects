#Create two dictionaries to represent information about two pets. 
#Each dictionary should contain the following information (different for each pet):

#Pet's Name (This should be the name of your dictionary)
#Type of Pet
#Color
#Nickname
#Owner's Name

Saturn = {'type of pet': 'Dragon', 'color': 'Blue', 'nickname': 'Beast','owner name': 'Malificent'}
Caluna= {'type of pet': 'Unicorn', 'color': 'White', 'nickname': 'Luna','owner name': 'Morgan La Fey'}

print(Saturn)
print(Caluna)

#Iterate over each dictionary, printing each key-value pair on one line. 

for key, value in Saturn.items():
    print(key, ":", value)

for key, value in Caluna.items():
    print(key, ":", value)

#Add three new dictionaries to your program.
#Each dictionary should represent a city around the world.

Cardiff= {'Country': 'Wales', 'Language': 'Welsh', 'Population': '3.1 million', 'Interesting Fact': 'The most beautiful people in the world are Welsh'}
Polpello= {'Country': 'Cornwall','Language': 'Cornish', 'Population': '1 million', 'Interesting Fact': 'Although part of England the Cornish consider themselves a seperate Country'}
Oslo= {'Country': 'Norway', 'Language': 'Norwegien', 'Population': '6.8 million', 'Interesting Fact': 'There have been several mermaid sightings off the coast of Oslo'}

print(Cardiff)
print(Polpello)
print(Oslo)

#Add the below dictionaries to your main.py file

england = {'Capital': 'London', 'Language': 'Englandese', 'Population': '44.8 million', 'Interesting Fact': 'English tea was once made with the Kings tears '}
france = {'Capital': 'Paris', 'Language': 'French', 'Population': '7.8 million', 'Interesting Fact': 'The Eifel tower was originally made of gold but over the years it was stripped and sold for cash'}
belgium = {'Capital': 'Brussels', 'Language': 'Belgin', 'Population': '4.8 million', 'Interesting Fact': 'There is actually nothing interesting about belgium'}

print(england)
print(france)
print(belgium)

#Once you have added the necessary information into the dictionaries, loop through each one and print out all key-value pairs.

for key, value in Cardiff.items():
    print(key, ":", value)
for key, value in Polpello.items():
    print(key, ":", value)
for key, value in Oslo.items():
    print(key, ":", value)
for key, value in england.items():
    print(key, ":", value)
for key, value in france.items():
    print(key, ":", value)
for key, value in belgium.items():
    print(key, ":", value)

#Add a dictionary to your program that replicates a user's pizza order. Name this dictionary pizza_order and it should contain the following:
#Customer's Name
#What size pizza they have ordered
#What type of crust
#What toppings they would like.
#Toppings should include at least three separate toppings

pizza_order = {'name': 'Clifton', 'size': 'gargantuan', 'crust': 'pure diamond'}
print(pizza_order)

toppings= {'topping 1':'sausage','topping 2': 'anchovies', 'topping 3': 'tomatoes'}
print(toppings)
for key, value in pizza_order.items():
    print(key, ":", value)

pizza_order['toppings'] = toppings

print(pizza_order)

greetings = []
for customer in pizza_order.values():
    greeting = "Thank you for your order" + customer["name"] 
    greetings.append(greeting)
print(greetings)
