# окрашивание текста в заданный цвет.

def set_color(text, color):
    return color + text + Color.reset

class Color:
    yellow2 = '\033[1;35m'
    reset = '\033[0m'
    blue = '\033[0;34m'
    yellow = '\033[1;93m'
    red = '\033[5;31m'
    miss = '\033[0;37m'


class Cell():
    empty_cell = set_color(' ', Color.yellow2)
    ship_cell = set_color('■', Color.blue)
    destroyed_ship = set_color('X', Color.yellow)
    damaged_ship = set_color('◦', Color.red)
    miss_cell = set_color('•', Color.miss)