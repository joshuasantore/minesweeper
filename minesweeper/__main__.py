from minesweeper.settings import Settings
from minesweeper.game.runner import Runner
import re
from os import system

print('Terminal Minesweeper!')
print("Please specify which level you'd like to play by typing 'easy', 'medium', or 'hard'.")

arg = input('')
while not re.match('^(easy|medium|hard)$', arg):
    system('clear')
    print('Terminal Minesweeper!')
    print("Please specify which level you'd like to play by typing 'easy', 'medium', or 'hard'.")
    arg = input('')

setting = Settings.select(arg)

runner = Runner(setting.num_cols, setting.num_rows, setting.num_bombs)

runner.run()

