import random
from minesweeper.game.box import Box
from termcolor import colored

class Board:
    def __init__(self, num_rows: int, num_cols: int, num_bombs: int):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.bombs = self.generate_bombs(num_bombs)
        self.rows = self.generate_rows()

    def generate_bombs(self, num_bombs: int):
        bombs = []
        while len(bombs) < num_bombs:
            bomb = [random.randint(0, self.num_cols - 1), random.randint(0, self.num_rows - 1)]
            while bomb in bombs:
                bomb = [random.randint(0, self.num_cols), random.randint(0, self.num_rows)]     
            bombs.append(bomb)               
        return bombs

    def generate_rows(self):
        rows = []
        for y in range(0, self.num_rows):  
            row = []
            for x in range(0, self.num_cols):
                box = Box([x, y], self.bombs)
                
                if [x, y] in self.bombs:
                    box.isBomb = True
                else:
                    box.bombs = box.count_bombs(self.bombs, self.num_cols, self.num_rows)
                row.append(box)
            rows.append(row)
        return rows

    def reveal(self, coords: list):
        box = self.rows[coords[1]][coords[0]]
        if box.hidden == True:
            box.hidden = False
            box.isflagged = False
            self.rows[coords[1]][coords[0]] = box
            if box.bombs == 0:
                for adjacent in box.get_adjacent(self.num_cols, self.num_rows):
                    self.reveal(adjacent)

    def render(self):
        print("   ", end="   ")
        for i in range(self.num_cols):
            print(colored(f" {i} ", 'grey', 'on_white', attrs=['bold']), end="   ")
        print("\n")
        for row in self.rows:
            print(colored(f" {self.rows.index(row)} ", 'grey', 'on_white', attrs=['bold']), end="   ")
            for box in row:
                print(box.render(), end = "   ")
            print("\n")
                 
    
    def render_all(self):
        print("   ", end="   ")
        for i in range(self.num_cols):
            print(colored(f" {i} ", 'grey', 'on_white', attrs=['bold']), end="   ")
        print("\n")
        for row in self.rows:
            print(colored(f" {self.rows.index(row)} ", 'grey', 'on_white', attrs=['bold']), end="   ")
            for box in row:
                box.hidden = False
                print(box.render(), end = "   ")
            print("\n")

    def count_flags(self):
        flag_count = 0
        for row in self.rows:
            flags = filter(lambda x: x.isflagged == True, row)
            flag_count += len(list(flags))     
        return flag_count

    def count_hidden(self):
        hidden_count = 0
        for row in self.rows:
            hidden = filter(lambda box: box.hidden == True, row)
            hidden_count += len(list(hidden))
        return hidden_count
