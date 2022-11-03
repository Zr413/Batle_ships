from random import randint
from board import Board
from ship import Ship
from board import Dec
from player import AI
from player import User
import color
from color import Color
from exept import BoardWrongShipException

class Game:
    def __init__(self, size=6):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hid = True

        self.ai = AI(co, pl)
        self.us = User(pl, co)


    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board


    def random_place(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dec(randint(0, self.size), randint(0, self.size)), l, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board


    def greet(self):
        print("⠀⠀⢀⣠⠖⠖⠒⠒⠒⠒⠒⠒⠓⠒⠒⠒⠒⠂⠒⠒⠒⠒⠒⠒⠒⠶⣄⡀⠀⠀")
        print("⠀⡤⠏⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⡶⢀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠈⠑⠄⠀                                                         ")
        print("⠀⠇⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠟⣠⡞⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀   ⠀⠘⡆                                                         ")
        print("⠸⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⢠⢉⠽⣅⡀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀   ⠀⠀⡇                                                         ")
        print("⢸⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠂⠭⠤⡐⠂⠪⠷⠶⠔             ⡆⠀---------------------------------------------------------")
        print("⢸⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⢸⠁⣶⡆⡏                ⡇", color.set_color('          Приветсвуем вас в игре морской бой!   ', Color.blue))
        print("⠸⡁⠀⠀⠀⠀⠀⠀⠀⠀⢰⠠⡊⠝⢈⢀⡙⡈⡂              ⡇", color.set_color('          Формат ввода координат', Color.blue), color.set_color('A 1', Color.red))
        print("⢸⠀⠀⠀⠀⠀⠀⠀⢀⣘⣐⣓⡰⡄⢆⡆⡯⠥⣍⠒⡀⠀⠀⠀⠀⠀⠀⠀  ⠀ ⡇                                                         ")
        print("⢸⠀⠀⠀⠀⠀⠀⢠⣬⢵⢞⢇⡢⣌⢴⠳⠎⣜⡁⠠⢸⡀          ⡇⠀---------------------------------------------------------")
        print("⢸⠀⠀⠀⠀⠀⠀⠘⢋⣵⣼⡾⣿⣓⠜⠇⠀⠀⠉⠚⢮⡳⠂         ⡇                                                         ")
        print("⢸⠀⠀⠀⠀⠀⠀⢼⣿⣿⠗⣃⡴⠇⢀⠇⠀⠀⠀⠀⠀⢉⡄          ⡃                                                         ")
        print("⢸⠄⠀⠀⠀⠀⠀⠘⣿⡻⢞⠕⢄⠁⢀⡅⠀⠀⠀⠀⠀⡘           ⡅                                                         ")
        print("⠘⡇⠀⠀⠀⠀⠀⠀⢩⣯⣞⣏⠗⠐⠌⡇⠀⠀⠀⠀⢸           ⢨⠁                                                         ")
        print(color.set_color('⠀⠡⣆⡠⣦⡤⠤⢤⣜⣻⣛⢣⣌⡍⡲⠯⠓⠥⠀⣶⣥⣀⣠⣂⣤⡤⣤⡰⠋', Color.blue))
        print(color.set_color('⠀  ⠈⠙⠶⠗⠆⠬⠭⠮⠯⠬⠾⠤⠮⠯⠼⠵⠶⠷⠾⠾⠷⠤⠖⠒⠉', Color.blue))


    def loop(self):
        num = 0
        while True:
            print("-" * 20)
            print("Доска пользователя:")
            print(self.us.board)
            print("-" * 20)
            print("Доска компьютера:")
            print(self.ai.board)
            if num % 2 == 0:
                print("-" * 20)
                print("Ходит пользователь!")
                repeat = self.us.move()
            else:
                print("-" * 20)
                print("Ходит компьютер!")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.count == 7:
                print("-" * 20)
                print("Пользователь выиграл!")
                break

            if self.us.board.count == 7:
                print("-" * 20)
                print("Компьютер выиграл!")
                break
            num += 1


    def start(self):
        self.greet()
        self.loop()