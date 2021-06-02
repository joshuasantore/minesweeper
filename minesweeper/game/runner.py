from minesweeper.game.board import Board
from os import system
import re
from termcolor import cprint

class Runner:
    def __init__(self, num_cols: int, num_rows: int, num_bombs):
        self.board = Board(num_rows, num_cols, num_bombs)
        self.num_bombs = num_bombs
        self.state = ''
        self.message = ''
        
    def count_flags_left(self):
        return self.num_bombs - self.board.count_flags()

    def validate_args(self, arg_string: str):
        if re.match(f'^(f|r) [0-{self.board.num_cols - 1}],[0-{self.board.num_rows - 1}]$', arg_string):
            return True
        return False
    
    def parse_args(self, arg_string: str):
        [arg, coords] = arg_string.split(' ')
        coords = coords.split(',')
        coords = [int(coords[0]), int(coords[1])]
        return [arg, coords]

    def flag(self, coords: list):
        if self.board.rows[coords[1]][coords[0]].hidden == True:
            if self.board.rows[coords[1]][coords[0]].isflagged == False:
                self.board.rows[coords[1]][coords[0]].isflagged = True
                self.message = f'{coords} flagged as bomb'
            else:
                self.board.rows[coords[1]][coords[0]].isflagged = False
                self.message = f'{coords} unflagged as bomb'
        else:
            self.message = f'{coords} unable to be flagged'


    def reveal(self, coords: list):  
        if self.board.rows[coords[1]][coords[0]].hidden == False:
            self.message = f'{coords} already revealed'       
        else:
            if self.board.rows[coords[1]][coords[0]].isflagged == True:
                self.message = f'{coords} cannot be revealed because it is flagged'
            else:
                if self.board.rows[coords[1]][coords[0]].isBomb == True:
                    self.board.reveal(coords)
                    self.message = f'revealed bomb at {coords}'  
                    self.state = 'loss'
                else:
                    self.board.reveal(coords)
                    self.message = f'revealed box at {coords}'  

    def run(self): 
        while self.state != 'loss' and self.state != 'win':  
            system('clear')
            print('\n')
            self.board.render()
            cprint(f'\n Hidden: {self.board.count_hidden()} ', 'white', 'on_grey')
            cprint(f'\n Flags: {self.count_flags_left()} ', 'grey', 'on_yellow')
            cprint(f'\n Message: {self.message} ', 'grey', 'on_cyan')
            print('\nPlease type (f) to flag a box or (r) to reveal a box followed by the coords as 2 numbers(x,y) separated by a comma')
            args = ''
            while not self.validate_args(args):
                system('clear')
                self.board.render()
                cprint(f'\n Hidden: {self.board.count_hidden()} ', 'white', 'on_grey')
                cprint(f'\n Flags: {self.count_flags_left()} ', 'grey', 'on_yellow')
                cprint(f'\n Message: {self.message} ', 'grey', 'on_cyan')
                print('\nPlease type (f) to flag a box or (r) to reveal a box followed by the coords as 2 numbers(x,y) separated by a comma')
                self.message = 'Invalid Input'
                args = input('Your Input: ')
            [arg, coords] = self.parse_args(args)
            if (arg == 'f'):
                self.flag(coords)
            if (arg == 'r'):
                self.reveal(coords)
            if (self.state != 'loss') and (self.board.count_hidden() == 0):
                self.state = 'win'
        
        system('clear')
        print('\n')
        self.board.render_all()
        print(f'Message: {self.message}')
        if self.state == 'loss':
            print('You lost! :(\nBetter luck next time...')
        if self.state == 'win':
            print('You won! :)\nTry a harder board next time...')



