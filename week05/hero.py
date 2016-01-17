from weapon import Weapon
from spell import Spell


class Hero:
    def __init__(self, name, title, health, mana, mana_regeneration_rate, damage = 0):
        self.name = name
        self.title = title
        self.test_health = health
        self.health = health
        self.test_mana = mana
        self.mana = mana
        self.mana_regeneration_rate = mana_regeneration_rate
        self.damage = damage
        self.wdamage = damage
        self.sdamage = damage

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def get_health(self):
        return "Current health: {}".format(self.health)

    def get_mana(self):
        return "Current mana: {}".format(self.mana)

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def can_cast(self):
        if self.mana >= Spell.self.mana_cost:
            return True
        else:
            return False

    def take_damage(self, damage_points):
        if damage_points >= self.health:
            self.health = 0  # тука незнам защо е инвалид синтаксис
        else:
            self.health = self.health - damage_points

    def take_healing(self, healing_points):
        if self.health > 0:
            self.health += healing_points
            if self.health > self.test_health:
                self.health = self.test_health
            return True
        else:
            return False

    # def take_mana(self):
    #     return self.mana += self.mana_regeneration_rate

    def take_mana_potion(self, mana_potion):
        self.mana += mana_potion
        if self.mana > self.test_mana:
            self.mana = self.test_mana
        return self.mana

    def equip(self, weapon):
        self.wdamage = self.damage + weapon.damage

    def learn(self, spell):
        self.sdamage = self.damage + spell.damage

    def attack(self, by):
        if by == "weapon":
            return self.wdamage
        elif by == "spell":
            return self.sdamage
        else:
            return self.damage
