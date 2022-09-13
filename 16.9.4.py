class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def client_wallet(self):
        return f"{self.name} {self.surname}.{self.city}.Баланс: {self.balance} руб."

    def client_list(self):
        return f"{self.name} {self.surname}.{self.city}."


person_1 = Client("Иван", "Петров", "Москва", 50)
person_2 = Client("Петр", "Иванов", "Санкт-Петербург", 100)
person_3 = Client("Дуся", "Курочкина", "Иваново", 10)
person_4 = Client("Анна", "Каренина", "Петрозаводск", 250)

clients = [person_1, person_2, person_3, person_4]
for person in clients:
    print(person.client_list())
