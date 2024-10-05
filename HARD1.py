class Toy:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type

    def __str__(self):
        return f"Игрушка: {self.name}, цвет: {self.color}, тип: {self.toy_type}"

class Factory:
    def create_toy(self, name, color, toy_type):
        print("Закупка сырья...")
        self.purchase_materials(name, color, toy_type)

        print("Пошив игрушки...")
        self.sew_toy(name, color, toy_type)

        print("Покраска игрушки...")
        self.paint_toy(name, color, toy_type)

        print('Игрушка готова.')
        return Toy(name, color, toy_type)

    def purchase_materials(self, name, color, toy_type):
        print(f"Сырье для игрушки {name} закуплено.")

    def sew_toy(self, name, color, toy_type):
        print(f"Игрушка {name} сшита.")

    def paint_toy(self, name, color, toy_type):
        print(f"Игрушка {name} покрашена.")

factory = Factory()
new_toy = factory.create_toy("Кролик", "Белый", "Животное")
print(new_toy)
