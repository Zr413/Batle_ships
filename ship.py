from board import Dec

# Расстановка кораблей
class Ship:
    def __init__(self, nos, dlin, orient):
        self.nos = nos
        self.dlin = dlin
        self.orient = orient
        self.lives = dlin

    @property
    def decs(self):
        ship_decs = []
        for i in range(self.dlin):
            cur_x = self.nos.x
            cur_y = self.nos.y

            if self.orient == 0:
                cur_x += i

            elif self.orient == 1:
                cur_y += i

            ship_decs.append(Dec(cur_x, cur_y))

        return ship_decs

    def shooten(self, shot):
        return shot in self.decs