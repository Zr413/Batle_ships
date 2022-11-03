import color
from color import Cell
from color import Color
from exept import BoardWrongShipException
from exept import BoardOutException
from exept import BoardUsedException



# Координаты поля
class Dec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


# Доска
class Board:
    def __init__(self, hid=False, size=6):
        self.size = size
        self.hid = hid

        self.count = 0

        self.field = [[" "] * size for _ in range(size)]

        self.busy = []
        self.ships = []

    # Добавление корабля
    def add_ship(self, ship):

        for d in ship.decs:
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException()
        for d in ship.decs:
            self.field[d.x][d.y] = Cell.ship_cell
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)

    # Смещение точки
    def contour(self, ship, verb=False):
        SDVIG = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
        for sd in ship.decs:
            for sd_x, sd_y in SDVIG:
                cur = Dec(sd.x + sd_x, sd.y + sd_y)
                # self.field[cur.x][cur.y] = '•'
                if not (self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = "•"
                    self.busy.append(cur)



    # Отрисовка поля
    def __str__(self):
        letters = ("A", "B", "C", "D", "E", "F")
        res = ""
        res += "  | 1---2---3---4---5---6 |"
        for i, row in enumerate(self.field):
            res += f"\n{letters[i]} | " + "   ".join(row) + " | " + f"{letters[i]}"
            color.set_color(res, Color.blue)
        res += "\n  | 1---2---3---4---5---6 |"

        if self.hid:
            res = res.replace("■", " ")
        return res

    # Проверка выхода зя границы
    def out(self, d):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    def shot(self, d):
        if self.out(d):
            raise BoardOutException()

        if d in self.busy:
            raise BoardUsedException()

        self.busy.append(d)

        for ship in self.ships:
            if d in ship.decs:
                ship.lives -= 1
                self.field[d.x][d.y] = Cell.destroyed_ship
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True

        self.field[d.x][d.y] = Cell.damaged_ship
        print("Мимо!")
        return False

    def begin(self):
        self.busy = []