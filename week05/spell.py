#from Dungeon import Dungeon
#from Fights import Fights


class Spell:
    def __init__(self, name, damage, mana_cost, cast_range):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range
        self.dungeon, self.row, self.col = [], 0, 0

    def position(self, dungeon, row, col):
        self.dungeon, self.row, self.col = dungeon, row, col

    def in_range(self):
        if self.left():
            return True
        elif self.right():
            return True
        elif self.top():
            return True
        elif self.bottom():
            return True
        else:
            return False

    def top(self):
        if self.row != 0:
            for index in range(0, self.cast_range):
                if self.dungeon[self.row-index][self.col] == "#":
                    return False
                    break
                elif self.dungeon[self.row-index][self.col] == "E":
                    return True
                    break

    def bottom(self):
        if self.row != len(self.dungeon) - 1:
            for index in range(0, self.cast_range):
                if self.dungeon[self.row+index][self.col] == "#":
                    return False
                    break
                elif self.dungeon[self.row+index][self.col] == "E":
                    return True
                    break

    def right(self):
        if self.col != len(self.dungeon[self.row]) - 1:
            for index in range(0, self.cast_range):
                if self.dungeon[self.row][self.col+index] == "#":
                    return False
                    break
                elif self.dungeon[self.row][self.col+index] == "#":
                    return True
                    break

    def left(self):
        if self.col != 0:
            for index in range(0, self.cast_range):
                if self.dungeon[self.row][self.col-index] == "#":
                    return False
                    break
                elif self.dungeon[self.row][self.col-1] == "E":
                    return True
                    break
