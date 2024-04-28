from abc import ABC, abstractmethod


class Weapon(ABC):
    def __init__(self, damage):
        self.damage = damage

    @abstractmethod
    def attack(self):
        pass


class Monster:

    def __init__(self, name, stamina):
        self.name = name
        self.stamina = stamina

    def take_damage(self, damage):
        self.stamina -= damage
        if self.stamina <= 0:
            print(f"Монстр {self.name} побежден!")
        else:
            print(f"У Монстра {self.name}  осталось {self.stamina} жизни")


class Bow(Weapon):
    def __init__(self, damage=0):
        super().__init__(damage)

    def attack(self):
        print(f"Наносит удар из лука")


class Sword(Weapon):
    def __init__(self, damage=20):
        super().__init__(damage)

    def attack(self):
        print(f"Наносит удар мечом")


class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon

    def fighter_attack(self, monster: Monster):
        print(f"{self.name} {self.weapon.attack}")
        monster.take_damage(self.weapon.damage)
