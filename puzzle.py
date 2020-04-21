import random
from copy import deepcopy
# generate an nxn puzzle
def gen_puzzle_n(n):
    size = n * n
    temp = list(range(size))
    temp = sorted(temp, key=lambda x: random.random())
    puzzle = [temp[i:i + n] for i in range(0, len(temp), n)]
    return puzzle

def move(puzzle, direction):
    x, y = coord_of_tile(puzzle, 0)
    x2, y2 = x + direction[0], y + direction[1]
    if x2 not in range(len(puzzle)) or y2 not in range(len(puzzle[0])):
        return None
    nPuzzle = deepcopy(puzzle)
    nPuzzle[x][y], nPuzzle[x2][y2] = nPuzzle[x2][y2], nPuzzle[x][y]
    return nPuzzle

# find the 2d coordinates of the 0 tile
def coord_of_tile(puzzle, tile_to_find):
    for x, column in enumerate(puzzle):
        for y, tile in enumerate(column):
            if tile == tile_to_find:
                return x, y
def up(puzzle):
    return move(puzzle, [1, 0])

def down(puzzle):
    return move(puzzle, [-1, 0])

def left(puzzle):
    return move(puzzle, [0, 1])

def right(puzzle):
    return move(puzzle, [0, -1])

def printPuzzle(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            print(puzzle[i][j], end=' ')
        print()

# def main():
#     # some testing
#     test = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
#
#     test2 = gen_puzzle_n(3)
#     printPuzzle(test)
#     right(test)
#     print("---------")
#     printPuzzle(test2)
#     print("---------")
#     up(test2)
#     printPuzzle(test2)
#
#
# if __name__ == "__main__":
#     main()