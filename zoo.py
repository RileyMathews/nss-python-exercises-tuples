zoo = ("dog", "monkey", "lion", "wolf")

print(zoo.index("dog"))

def animal_search(animal):
    for value in zoo:
        if value == animal:
            print(f"found {value}")

animal_search("dog")
(dog, monkey, lion, wolf) = zoo
print(wolf)

zoo_list = list(zoo)
zoo_list.extend(['lizzard', 'tiger', 'bear'])
print(zoo_list)
zoo = tuple(zoo_list)
print(zoo)