from weapon import Weapon
from spell import Spell

class Enemies:

    def __init__(self, health, mana, damage):
        self.health = health
        self.mana = mana
        self.damage = damage

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def can_cast(self):
        pass

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def equip(self, weapon):
        pass

    def learn(self, spell):
        pass
    def attack(self, by):
        #тук ще има рандом генератор
        if by == "weapon":
            return self.equip()
        elif by == "spell":
            return self.learn()
        else:
            return self.damage

    def take_damage(self, damage):
        if damege >= self.health:
            return self.healt = 0
        else:
            return self.health = self.health - damage
