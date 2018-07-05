zoo = ("dog", "monkey", "lion", "wolf")

print(zoo.index("dog"))

def animal_search(animal):
    for value in zoo:
        if value == animal:
            print(f"found {value}")