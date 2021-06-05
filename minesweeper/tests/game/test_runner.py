from minesweeper.game.runner import Runner
from minesweeper.game.board import Board
from time import sleep
runner = Runner(10,10,10)

# init values
def test_creation():
    assert isinstance(runner.board, Board)
    assert runner.num_bombs == 10
    assert runner.state == ''

def test_count_flags_left():
    assert runner.count_flags_left() == 10

def test_validate_args():
    runner = Runner(16,16,15)
    assert runner.validate_args('f 1,1') == True
    assert runner.validate_args('f 8,8') == True
    assert runner.validate_args('f 10,1') == True
    assert runner.validate_args('r 10,1') == True
    assert runner.validate_args('r 20,1') == False
    assert runner.validate_args('f 20,1') == False
    assert runner.validate_args('invalid input') == False

def test_parse_args():
    [arg, coords] = runner.parse_args('f 1,1')  
    assert arg == 'f'
    assert coords == [1,1]

    [arg, coords] = runner.parse_args('r 5,8')
    assert arg == 'r'
    assert coords == [5,8]

def test_flag():
    runner.flag([3,2])
    assert runner.board.rows[2][3].isflagged == True

def test_reveal():
    runner.reveal([5,2]) 
    if (runner.board.rows[2][5].isBomb == True):
        assert runner.message == 'revealed bomb at [5, 2]'
    else:
        assert runner.message == 'revealed box at [5, 2]'
        runner.reveal([5,2])
        assert runner.message == '[5, 2] already revealed'
    # If you want visual confirmation of tests success un-comment the next line
    #runner.board.render()


# Leave commented out unless you need to test something specific about the gameplay <3

'''
def test_run():
    runner = Runner(5,5,5)
    runner.run()
'''

