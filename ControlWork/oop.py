from abc import ABC, abstractmethod
import math

class Person:
    def __init__(self, age: int = 0):
        self.__age = 0
        self.set_age(age)

    def set_age(self, age: int) -> None:
        """
        Установить возраст. Возраст должен быть целым неотрицательным.
        Если значение некорректно — возбуждается ValueError.
        """
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целым числом (int).")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным.")
        self.__age = age

    def get_age(self) -> int:
        """Возвращает возраст."""
        return self.__age


class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        """Возвращает звук животного (по умолчанию пустая строка)."""
        return ""

class Dog(Animal):
    def speak(self) -> str:
        return "Woof"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow"


class Transport:
    def move(self) -> str:
        return "Transport is moving"

class Car(Transport):
    def move(self) -> str:
        return "Car is driving"

class Bicycle(Transport):
    def move(self) -> str:
        return "Bicycle is pedaling"

def move(obj: Transport) -> str:
    """
    Принимает объект (ожидается наследник Transport) и вызывает его метод move().
    Поддерживает полиморфизм.
    """
  
    if not hasattr(obj, "move"):
        raise TypeError("Объект не поддерживает метод move().")
    return obj.move()


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Вычислить площадь — абстрактный метод."""
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        if width < 0 or height < 0:
            raise ValueError("Ширина и высота должны быть неотрицательными.")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius: float):
        if radius < 0:
            raise ValueError("Радиус не может быть отрицательным.")
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)


if name == "__main__":
    p = Person()
    p.set_age(25)
    print("Person age:", p.get_age()) 
    try:
        p.set_age(-5)
    except Exception as e:
        print("Ошибка при установке возраста:", e)

    dog = Dog("Buddy")
    cat = Cat("Kitty")
    print(dog.name, dog.speak()) 
    print(cat.name, cat.speak())  

    car = Car()
    bike = Bicycle()
    print(move(car))   
    print(move(bike))  

    rect = Rectangle(10, 5)
    circle = Circle(7)
    print("Rectangle area:", rect.area()) 
    print("Circle area:", round(circle.area(), 2))  