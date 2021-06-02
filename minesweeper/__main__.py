from minesweeper.settings import Settings
from minesweeper.game.runner import Runner
import re
from os import system
from termcolor import colored

logo = colored('''

   __  __ _               _____                                   
  |  \/  (_)             / ____|                                  
  | \  / |_ _ __   ___  | (_____      _____  ___ _ __   ___ _ __  
  | |\/| | | '_ \ / _ \  \___ \ \ /\ / / _ \/ _ \ '_ \ / _ \ '__| 
  | |  | | | | | |  __/  ____) \ V  V /  __/  __/ |_) |  __/ |    
  |_|  |_|_|_| |_|\___| |_____/ \_/\_/ \___|\___| .__/ \___|_|    
                                               | |                
                                               |_|                
                                                                  
''', 'white', 'on_cyan', attrs=['bold'])
system('clear')
print(logo)
print("Please specify which level you'd like to play by typing 'easy', 'medium', or 'hard'.")

arg = input('\nYour Choice: ')
while not re.match('^(easy|medium|hard)$', arg):
    system('clear')
    print(logo)
    print("Please specify which level you'd like to play by typing 'easy', 'medium', or 'hard'.")
    arg = input('\nYour Choice: ')

setting = Settings.select(arg)

runner = Runner(setting.num_cols, setting.num_rows, setting.num_bombs)

runner.run()

