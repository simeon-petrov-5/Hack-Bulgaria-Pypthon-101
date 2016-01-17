from hero import Hero
from enemies import Enemies
from spell import Spell
class Fights:
    def __init__(self):
        self.fattack = True  # това е за проверка да ли е първа атака
        self.msg1 = "A fight is started between our Hero(health={},mana={})\
        and Enemey(health={}, mana={}, damage={})".format(Hero.self.health, Hero.self.mana, Enemies.self.health, Enemies.self.mana)
        self.msg2 = "Hero casts a {}, hits enemy for {} dmg. Enemy health is {}".format(Spell.self.name, Spell.self.damage, Enemies.self.health)
        self.msg3 = "Enemy hits hero for {} dmg. Hero health is {}".format()
    def hero_attack(self, by):
        if by == "spell":
            if Spell.in_range():
                if Hero.can_cast() == True and self.fattack == True:
                    self.fattack = False  # след боя трябва да стане пак True
                    print(self.msg1)
                    Enemies(take_damege())
                    # Трябва да се добави боя
                elif Hero.can_cast():
                    # Трябва да се добави боя
                else:
                    return self.hero_attack("weapon")  # Май така беше да се испълни функцията

            else:
                print("Nothing in casting range {}".format(self.cast_range))
        if by == "weapon":
            # Трябва да се добави боя
            pass
    def battle(self):
        pass