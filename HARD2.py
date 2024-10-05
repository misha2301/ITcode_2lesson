class Toy:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"Игрушка: {self.name}, Цвет: {self.color}"


class AnimalToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.toy_type = "Животное"


class CartoonToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.toy_type = "Персонаж мультфильма"


class ToyFactory:
    def create_toy(self, name, color, toy_type):
        print(f"Закупка сырья для игрушки {name} ...")
        self.purchase_materials()

        print(f"Пошив игрушки {name} ...")
        self.sew_toy()

        print(f"Покраска игрушки {name} в {color.lower()} цвет ...")
        self.paint_toy()

        if toy_type == "Животное":
            return AnimalToy(name, color)
        elif toy_type == "Персонаж мультфильма":
            return CartoonToy(name, color)
        else:
            raise ValueError("Неизвестный тип игрушки!")

    def purchase_materials(self):
        print("Сырьё успешно закуплено.")

    def sew_toy(self):
        print("Игрушка сшита.")

    def paint_toy(self):
        print("Игрушка покрашена.")

factory = ToyFactory()
animal_toy = factory.create_toy("Лиса", "Оранжевый", "Животное")
cartoon_toy = factory.create_toy("Копатыч", "Коричневый", "Персонаж мультфильма")

print(animal_toy)
print(cartoon_toy)
