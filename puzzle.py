import random
from copy import deepcopy
from itertools import chain

def gen_puzzle_n(n):
    """
    Generate a puzzle of size nxn

    @param n(int) The len of row and col
    @return puzzle(2d list) An nxn 2d list
    """
    size = n * n
    temp = list(range(size))
    temp = sorted(temp, key=lambda x: random.random())
    puzzle = [temp[i:i + n] for i in range(0, len(temp), n)]
    return puzzle

def move(puzzle, direction):
    """
    Swap a tile with the empty tile if possible

    @param puzzle A 2d list in which the tile is swapped
    @param direction The direction the tile is moved
    @return A copy of the puzzle with the tile swapped with the empty tile
    or none if the empty tile is not in that direction
    """
    x, y = coord_of_tile(puzzle, 0)
    x2, y2 = x + direction[0], y + direction[1]
    if x2 not in range(len(puzzle)) or y2 not in range(len(puzzle[0])):
        return None
    nPuzzle = deepcopy(puzzle)
    nPuzzle[x][y], nPuzzle[x2][y2] = nPuzzle[x2][y2], nPuzzle[x][y]
    return nPuzzle

def coord_of_tile(puzzle, tile_to_find):
    """
    Find the 2D coordinates of a tile give a puzzle

    @param puzzle A 2d list
    @param tile_to_find An int within the constraints of the puzzle
    """
    for x, column in enumerate(puzzle):
        for y, tile in enumerate(column):
            if tile == tile_to_find:
                return x, y
def up(puzzle):
    """
    Swap a tile with the empty tile in the up direction

    @param puzzle a 2d list
    @return the puzzle with the tile swapped or None otherwise
    """
    return move(puzzle, [1, 0])

def down(puzzle):
    """
    Swap a tile with the empty tile in the down direction

    @param puzzle a 2d list
    @return the puzzle with the tile swapped or None otherwise
    """
    return move(puzzle, [-1, 0])

def left(puzzle):
    """
    Swap a tile with the empty tile in the left direction

    @param puzzle a 2d list
    @return the puzzle with the tile swapped or None otherwise
    """
    return move(puzzle, [0, 1])

def right(puzzle):
    """
    Swap a tile with the empty tile in the right direction

    @param puzzle a 2d list
    @return the puzzle with the tile swapped or None otherwise
    """
    return move(puzzle, [0, -1])


def printPuzzle(puzzle):
    """
    Print a puzzle in the standard grid format

    @param puzzle a 2d list
    """
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            print(puzzle[i][j], end=' ')
        print()

def is_solvable(puzzle, final_state, n):
    """
    Determine if a given puzzle is solvable with the given final solution

    @param puzzle a 2d list
    @param final_state The solved state of the puzzle
    @param n the len of the puzzle's row/col
    @return True if the puzzle is solvable False othewise
    """
    flatten_puzzle = list(chain.from_iterable(puzzle)) # flatten the list
    inversions = inv_count(flatten_puzzle, final_state, n)
    puzzle_zero_row, puzzle_zero_column = coord_of_tile(puzzle, 0)
    puzzle_zero_row = puzzle_zero_row // n
    puzzle_zero_column = puzzle_zero_column % n
    final_zero_row,  final_zero_column = coord_of_tile(final_state, 0)
    final_zero_column = final_zero_column % n
    manhattan = abs(puzzle_zero_row - final_zero_row) + abs(puzzle_zero_column - final_zero_column)
    if manhattan % 2 == 0 and inversions % 2 == 0:
        return True
    if manhattan % 2 == 1 and inversions % 2 == 1:
        return True
    return False


def inv_count(puzzle, final_state, n):
    """
    Count the number of inversions in a puzzle

    @param puzzle a 2d list
    @param final_state The solved state of the puzzle
    @param n the len of the puzzle's row/col
    @return An int that is the number of inversions
    """
    inversions = 0
    n_2 = n * n
    for i, tile in [(i, tile) for i, tile in enumerate(puzzle) if tile != len(puzzle)]:
        for j in range(i+1, n_2):
            if puzzle[j] < tile:
                inversions += 1
    return inversions


