from minesweeper.game.box import Box
from termcolor import colored


box = Box([2,2], [[1,2], [3,4], [5,5]])


# init values
def test_creation(): 
    assert box.x == 2
    assert box.y == 2
    

#coords
def test_get_coords():
    assert box.get_coords() == [2,2]
    

#adjacent
def test_adjacent_surrounded():
    adjacent = box.get_adjacent(10,10)
    coords = box.get_coords()
    assert len(adjacent) == 8 
    assert coords not in adjacent
    # 8 values because box is surrounded by 8 other valid boxes
    assert adjacent == [[1, 1], [1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2], [3, 3]]

def test_adjacent_where_edge():
    # New box just to test edge case 
    adjacent = box.get_adjacent(2,3)
    # 5 values because box is on an edge
    assert adjacent == [[1, 1], [1, 2], [1, 3], [2, 1], [2, 3]]
    

def test_adjacent_where_corner():
    adjacent = box.get_adjacent(2,2)
    # 3 boxes because box is touching 2 edges
    assert adjacent == [[1, 1], [1, 2], [2, 1]]

# setbombs
def test_set_bombs():
    box.setBombs([[1,1],[1,2], [2,0]], 2, 2)
    assert box.bombs == 2

# render
def test_render_hidden():
    assert box.render() == colored(' ? ', 'white', 'on_grey', attrs=['bold'] )
    
def test_render_bomb():
    box.isBomb = True
    box.hidden = False
    assert box.render() == colored(' B ', 'red', 'on_red', attrs=['bold'] )

def test_render_bomb():
    box.isBomb = True
    box.hidden = True
    box.isflagged = True
    assert box.render() == colored(' F ', 'grey', 'on_yellow', attrs=['bold'] )

def test_render_num_bombs():
    box.isBomb = False
    box.hidden = False
    box.isflagged = False
    box.bombs = 3
    assert box.render() == colored(' 3 ', 'grey', 'on_cyan', attrs=['bold'] )