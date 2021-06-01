from minesweeper.game.board import Board

board = Board(10,10,10)

# init values
def test_creation():
    assert board.num_cols == 10
    assert board.num_rows == 10
    assert len(board.bombs) == 10
    
# generate bombs
def test_generate_bombs():
    bombs = board.generate_bombs(5)
    for bomb in bombs:
        assert bombs.count(bomb) == 1

# generate board
def test_generate_rows():
    rows = board.generate_rows()
    assert len(rows) == 10
    assert len(rows[0]) == 10


def test_count_hidden():
    assert board.count_hidden() == 100
    board.rows[5][5].hidden = False
    board.rows[6][6].hidden = False
    assert board.count_hidden() == 98
    board.rows[5][5].hidden = True
    board.rows[6][6].hidden = True
    assert board.count_hidden() == 100
    
# reveal coords, recursively if 0 bombs surrounding
def test_reveal():
    assert board.rows[1][1].hidden == True
    board.reveal([1,1])
    box = board.rows[1][1]
    assert box.hidden == False

# count flags used
def test_flag_used():
    flags = board.count_flags()
    assert flags == 0
    board.rows[1][1].isflagged = True
    board.rows[4][7].isflagged = True
    board.rows[9][8].isflagged = True
    flags = board.count_flags()
    assert flags == 3

# render each box based on its state
def test_render():
    '''print("\n")
    board.render()'''
    # Due to the randomness of the board, this test should be manually checked when needed.
    # Just uncomment the above if you're working on the board mechanics
    pass

# change all boxes state to unhidden and render them
def test_render_all():
    '''print("\n")
    board.render_all()'''
    # Due to the randomness of the board, this test should be manually checked when needed.
    # Just uncomment the above if you're working on the board mechanics
    pass


