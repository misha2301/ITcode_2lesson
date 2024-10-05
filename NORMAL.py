class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def Attack(self, opponent):
        print(f"{self.name} атакует, нанося {self.damage} единиц урона противнику.")
        opponent.TakeDamage(self.damage)

    def TakeDamage(self, amount):
        damage_taken = self.__calculate_damage(amount)
        self.health -= damage_taken
        self.health = max(0, self.health)
        print(f"{self.name} получает {damage_taken} единиц урона. Осталось {self.health} единиц здоровья.")

    def __calculate_damage(self, amount):
        damage_taken = amount - self.armor
        if damage_taken < 0:
            damage_taken = 0
        return damage_taken


class Player(Person):
    def __init__(self, name, health, damage, armor):
        super().__init__(name, health, damage, armor)


class Enemy(Person):
    def __init__(self, name, health, damage, armor):
        super().__init__(name, health, damage, armor)


class Game:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start(self):
        turn = 'player'
        while self.player.health > 0 and self.enemy.health > 0:
            if turn == 'player':
                self.player.Attack(self.enemy)
                turn = 'enemy'
            else:
                self.enemy.Attack(self.player)
                turn = 'player'

        if self.player.health <= 0:
            print(f"{self.enemy.name} победил!")
        else:
            print(f"{self.player.name} победил!")


# Создаем игрока и врага
player = Player('Илья Муромец', 1000, 60, 35)
enemy = Enemy('Соловей-разбойник', 100, 40, 0)

# Запускаем игру
game = Game(player, enemy)
game.start()
