class Person:
    def __init__(self, name, birth_date, profession):
        self.name = name
        self.birth_date = birth_date
        self.profession = profession

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. Я родился {self.birth_date}, работаю {self.profession}.")


class Classmate(Person):
    def __init__(self, name, birth_date, profession, group_name):
        super().__init__(name, birth_date, profession)
        self.group_name = group_name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я одногруппник из {self.group_name}. "
              f"Родился {self.birth_date}, сейчас работаю {self.profession}.")


class Friend(Person):
    def __init__(self, name, birth_date, profession, hobby):
        super().__init__(name, birth_date, profession)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я люблю {self.hobby}. "
              f"Родился {self.birth_date}, работаю {self.profession}.")



classmate1 = Classmate("Бектур", "05.12.2000", "инженером", "Группа GEEKS-3")
classmate2 = Classmate("Айдана", "10.03.2001", "дизайнером", "Группа GEEKS-3")

friend1 = Friend("Алмаз", "15.05.1999", "программистом", "играть в шахматы")
friend2 = Friend("Байэл", "01.08.2000", "маркетологом", "путешествовать")

classmate1.introduce()
classmate2.introduce()
friend1.introduce()
friend2.introduce()


# Дополнительное задание 1

people = [classmate1, classmate2, friend1, friend2,
           Person("Эрмек", "12.06.1995", "врач")]

print("\n--- Вывод через цикл ---")
for person in people:
    person.introduce()


# Дополнительное задание 2

class BestFriend(Friend):
    def __init__(self, name, birth_date, profession, hobby, shared_memory):
        super().__init__(name, birth_date, profession, hobby)
        self.shared_memory = shared_memory

    def introduce(self):
        super().introduce()
        print(f"Мы с ним(ней) часто вспоминаем, как {self.shared_memory}.")


best_friend = BestFriend("Нурлан", "20.04.1998", "тестировщик", "играть в футбол",
                         "гуляли в парке")

print("\n--- Лучший друг ---")
best_friend.introduce()
