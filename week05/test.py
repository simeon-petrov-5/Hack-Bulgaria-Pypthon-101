from weapon import Weapon


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

    def equip(self, weapon):
        return self.damage + weapon

def main():
    pass

if __name__ == '__main__':
    main()
