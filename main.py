list_of_names = ['Kurt', 'David', 'Katherine']

for name in list_of_names:
    print("Where is " + name + " today?")

my_favorite_cars= ["Subaru","Lincoln","Horse"]
my_favorite_flowers = ["Iris", "Peony", "Rose","Lily"]
my_favorite_animals = ["Dog","Bird","Ant","Fish","Uncicorn"]

my_favorite_things = my_favorite_cars + my_favorite_flowers + my_favorite_animals
print(my_favorite_things)

for thing in my_favorite_things:
    if len(thing) % 2 == 0:
        print(thing)

number_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for number in number_range:
    if number % 3 == 0 and number % 5 == 0:
        print('ZipZap')
    elif number % 3 == 0:
        print('Zip')
    elif number % 5 == 0:
        print('Zap')
    else:
        print(number)