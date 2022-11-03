from random import randint
from exept import BoardException
from board import Dec

def let(a):
    letters = ["A", "B", "C", "D", "E", "F"]
    x = letters.index(a)
    return x + 1

class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)

class AI(Player):
    def ask(self):
        d = Dec(randint(0, 5), randint(0, 5))
        print(f"Ход компьютера: {d.x + 1} {d.y + 1}")
        return d


class User(Player):
    def ask(self):
        while True:
            cords = input("Ваш ход: ").split()

            if len(cords) != 2:
                print(" Введите 2 координаты! ")
                continue

            x = let(cords[0])
            y = cords[1]

            # if not (x.isdigit()) or not (y.isdigit()):
            #     print(" Введите числа! ")
            #     continue

            x, y = int(x), int(y)

            return Dec(x - 1, y - 1)