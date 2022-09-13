class Pets:
    def __init__(self, species, name, gender, age):
        self.species = species
        self.name = name
        self.gender = gender
        self.age = age


    def print_pet(self):
        i = input("Введите вид животного:")
        if self.species == i:
            print(f"Имя питомца: {self.name}\nПол питомца: {self.gender}\nВозраст питомца: {self.age}")
        else:
            print("Другой вид животного")