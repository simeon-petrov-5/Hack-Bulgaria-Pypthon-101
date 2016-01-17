from weapon import Weapon
from spell import Spell
from hero import Hero
# from enemies import Enemies
# from Fights import Fight
import json
from random import randint


class Dungeon:

    def __init__(self):
        self.dungeon = []
        self.movements = []
        self.new_weapon = ["fist", 0]
        self.rol, self.col = 0, 0

    def create_from_file(self, name="level1.txt"):
        with open(name, "r") as f:
            contents = f.read().split("\n")
            self.dungeon = [list(line) for line in contents if line.strip() != ""]
        return self.dungeon

    def print_map(self):
        for dungeon in self.dungeon:
            dun = map(str, dungeon)
            dun = "".join(dun)
            print (dun)

    def current_position(self):
        Spell.position(self.dungeon, self.rol, self.col)

    def move_hero(self, direction):
        if not self.analyze_next_step(direction):
            return False
        else:
            if direction == "up":
                self.dungeon[self.rol][self.col], self.dungeon[self.rol+1][self.col] = ".", "H"
                self.col = 1
                self.movements.append(direction)
                return True

            elif direction == "down":
                self.dungeon[self.rol][self.col], self.dungeon[self.rol+1][self.col] = ".", "H"
                self.col += 1
                self.movements.append(direction)
                return True

            elif direction == "left":
                self.dungeon[self.rol][self.col], self.dungeon[self.rol][self.col-1] = ".", "H"
                self.rol -= 1
                self.movements.append(direction)
                return True

            elif direction == "right":
                self.dungeon[self.rol][self.col], self.dungeon[self.rol][self.col+1] = ".", "H"
                self.col += 1
                self.movements.append(direction)
                return True

    def spawn(self, respawn_points = 2):
        if respawn_points > 0:
            for move in self.movements:
                self.move_hero(move)
            return True
        else:
            return False

    def pick_treasure(self):
        self.new_weapon = []
        n = randint(0, 1)
        k = randint(0, 3)
        with open('treasure_lvl1.json', 'r') as f:
            data = json.load(f)
        if n == 0:
            weapon = data["weapons"][k]
            self.new_weapon = [x for x in (weapon["name"], weapon["damage"])]
            print("You have picked weapon {} with {} damage,you ca equip it.".format(weapon["name"], weapon["damage"],))
        elif n == 1:
            spell = data["spells"][k]
            s = Spell(spell["name"], spell["damage"], spell["mana_cost"], spell["cast_range"])
            print(
                "You have picked spell\
                {} with {} damage, {} mana cost, {} cast range,\
                you ca learn it."
                .format(
                    spell["name"],
                    spell["damage"],
                    spell["mana_cost"],
                    spell["cast_range"]))

    def end_of_level(self):
        return "Success!!! Bravo, great worrior, you have passed through this level!"

    def analyze_next_step(self, direction):
        direction = direction.lower()

        if direction == "up" and self.rol != 0:
            if self.dungeon[self.rol-1][self.col] == "#":
                return False
            elif self.dungeon[self.rol-1][self.col] == "T":
                self.pick_treasure()
                return True
            elif self.dungeon[self.rol-1][self.col] == "E":
                self._some_fight_method()
                return True
            elif self.dungeon[self.rol-1][self.col] == "G":
                self.end_of_level()
                return True
            else:
                return True

        elif direction == "down" and self.rol != len(self.dungeon):
            if self.dungeon[self.rol+1][self.col] == "#":
                return False
            elif self.dungeon[self.rol+1][self.col] == "T":
                self.pick_treasure()
                return True
            elif self.dungeon[self.rol+1][self.col] == "E":
                self._some_fight_method()
                return True
            elif self.dungeon[self.rol+1][self.col] == "G":
                self.end_of_level()
                return True
            else:
                return True

        elif direction == "left" and self.col != 0:
            if self.dungeon[self.rol][self.col-1] == "#":# тука self.rol self.col-1
                return False
            elif self.dungeon[self.rol][self.col-1] == "T":
                self.pick_treasure()
                return True
            elif self.dungeon[self.rol][self.col-1] == "E":
                self._some_fight_method()
                return True
            elif self.dungeon[self.rol][self.col-1] == "G":
                self.end_of_level()
                return True
            else:
                return True

        elif direction == "right" and self.col != 9:#  според мен тука трябва да бъде дължината на втория лист
            if self.dungeon[self.rol][self.col+1] == "#":
                return False
            elif self.dungeon[self.rol][self.col+1] == "T":
                return self.pick_treasure()
            elif self.dungeon[self.rol][self.col+1] == "E":
                # Тук трябва да вържем fight

                return self._some_fight_method()
            elif self.dungeon[self.rol][self.col+1] == "G":
                return self.end_of_level()
            else:
                return True

        else:
            print("ERROR. Movement out of the map.")
            return False


def main():
    maps = Dungeon()
    w = Weapon(maps.new_weapon[0], maps.new_weapon[1])
    h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)
    s = Spell("none", 0, 0, 0)
    maps.create_from_file()
    m = "maps.print_map()"
    a = "maps.move_hero('left')"
    d = "maps.move_hero('right')"
    w = "maps.move_hero('up')"
    s = "maps.move_hero('down')"
    options = ["a", "d", "w", "s", "m"]
    while True:
        w = Weapon(maps.new_weapon[0], maps.new_weapon[1])
        value = input('>>>')
        if value == "exit":
            break
        elif value in options:
            eval(eval(value))


if __name__ == '__main__':
    main()