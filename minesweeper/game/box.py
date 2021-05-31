from termcolor import colored

class Box:

    def __init__(self, coords: list, bombs: list):
        self.x = coords[0]
        self.y = coords[1]
        self.isBomb = False
        self.bombs = None
        self.hidden = True
        self.isflagged = False


    def get_coords(self):
        return [self.x, self.y]


    def get_adjacent(self, num_cols: int, num_rows: int):
        coords = self.get_coords()
        adjacent = []
        for x in range(self.x - 1, self.x + 2):
            
            for y in range(self.y - 1, self.y + 2):
                if [x,y] == coords:
                    pass
                else:
                    if (-1 < x < num_cols) and (-1 < y < num_rows):
                        adjacent.append([x, y])
        return adjacent


    def count_bombs(self, bombs: list, cols: int, rows: int):
        if self.isBomb == False:
            numBombs = 0
            boxes = self.get_adjacent(cols, rows)
            for bomb in bombs:
                if bomb in boxes:
                    numBombs += 1
            self.bombs = numBombs
            return numBombs
        return None


    def render(self):
        if self.isBomb == True:
            output = colored(' B ', 'red', 'on_red', attrs=['bold'] )
        else:
            if self.bombs == 0:
                output = colored(f' 0 ', 'grey', 'on_grey', attrs=['bold'] )
            else:
                output = colored(f' {self.bombs} ', 'grey', 'on_cyan', attrs=['bold'] )

        if self.hidden == True:
            output = colored(' ? ', 'white', 'on_grey', attrs=['bold'] )
    

        if self.isflagged == True:
            output = colored(' F ', 'grey', 'on_yellow', attrs=['bold'] )
        #print(output, end = "   ")
        return output