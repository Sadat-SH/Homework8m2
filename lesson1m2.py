# ООП - Обьектно ориентированное программирование, это способ писать программы в котором все строится вокруг объектов - "штук" с данными(свойствами) и действиями(методмами).
# ООП помогает организовать код, делая его более понятным и легким для поддержки.
# до этого мы использовали более простой подход - ПРОЦЕДУРНОЕ ПРОГРАММИРОВАНИЕ, где код делится на процедуры или функции, которые выполняют определенные задачи последовательно. Это более старый подход, где данные и функции разделены.  

# Основные понятия в ООП:
# - Класс
# - Объект

# Класс:
# - Шаблон для создания объектов. Чертеж.
# - Описывает свойства, которые будут иметь объекты и действия, которые будет выполнять.


class Car:
    # конструктор/инициализатор
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive(self, location):
        print(f"Car {self.model} driving in {location}")

    def test(self):
        self.drive("Karakol")
color = "red"
car_honda = Car(color="red", model="Honda")
car_subaru = Car(color="silver", model="Subaru")

car_subaru.drive("Bishkek")
car_honda.test()
print(car_honda)
print(car_subaru)
print(car_honda.color)
print(car_subaru.color)
print(car_honda.model == car_subaru.model )
print(type(123), type("aaaaaaaa"))
print(type(car_subaru))
