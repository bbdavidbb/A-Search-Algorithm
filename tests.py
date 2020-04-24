from puzzle import gen_puzzle_n, printPuzzle, is_solvable
from graph import dfs, bfs, a_star, reconstruct_path, manhattan_distance, hamming_distance, linear_conflict
import time

EIGHT_PSOL = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
FIFTEEN_PSOL = [[1, 2, 3, 4,], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
TWENTY_FOUR_PSOL = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 0]]

def test_algorithm_eight(algorithm):
    print("Begin Algorithm Test \n-------------------------------\n")
    print("Generating the puzzles")
    eight_puzzles = _gen_n_puzzles(10, 3, EIGHT_PSOL)
    print("The 8 puzzles: ")
    for next in eight_puzzles:
        printPuzzle(next)
        print("-------------------------------")
    fifteen_puzzles = _gen_n_puzzles(1, 4, FIFTEEN_PSOL)
    print("The 15 puzzles: ")
    for next in fifteen_puzzles:
        printPuzzle(next)
        print("-------------------------------")
    print("End Puzzle Generation\n-------------------------------\n")

    print("Begin 8 Puzzle Test \n-------------------------------\n")
    search_length = 0
    solution_length = 0
    start_time = time.time()
    count = 1
    for puzzle in eight_puzzles:
        print("Solving puzzle {} of eight puzzle".format(count))
        count += 1
        states_taken, final_puzzle = algorithm(puzzle, EIGHT_PSOL)
        search_length += states_taken
        if(final_puzzle is None):
            continue
        else:
            solution_length += final_puzzle.num_parents
    print(" %s seconds to complete eight puzzle tests" % (time.time() - start_time))
    print("Average steps to find an optimal solution {}".format(search_length / len(eight_puzzles)))
    print("Average steps for the optimal solution {}".format(solution_length / len(eight_puzzles)))
    print("\n End Algorithm test \n-------------------------------\n")



def test_a_star_eight(heuristic):
    print("Begin A_Star Test \n-------------------------------\n")
    print("Generating the puzzles")
    eight_puzzles = _gen_n_puzzles(10, 3, EIGHT_PSOL)
    print("The 8 puzzles: ")
    for next in eight_puzzles:
        printPuzzle(next)
        print("-------------------------------")

    print("Begin 8 Puzzle Test \n-------------------------------\n")
    search_length = 0
    solution_length = 0
    start_time = time.time()
    count = 1
    for puzzle in eight_puzzles:
        print("Solving puzzle {} of eight puzzle".format(count))
        count += 1
        states_taken, final_puzzle = a_star(puzzle, EIGHT_PSOL, heuristic)
        search_length += states_taken
        if(final_puzzle is None):
            continue
        else:
            solution_length += final_puzzle.num_parents
    print(" %s seconds to complete eight puzzle tests" % (time.time() - start_time))
    print("Average steps to find an optimal solution {}".format(search_length / len(eight_puzzles)))
    print("Average steps for the optimal solution {}".format(solution_length / len(eight_puzzles)))
    print("\n Begin 15 puzzle tests \n-------------------------------\n")



def test_a_star_fifteen(heuristic):
    print("Begin A_Star 15 puzzle Test \n-------------------------------\n")

    fifteen_puzzles = _gen_n_puzzles(1, 4, FIFTEEN_PSOL)
    print("The 15 puzzles: ")
    for next in fifteen_puzzles:
        printPuzzle(next)
        print("-------------------------------")
    print("\n Begin 15 puzzle tests \n-------------------------------\n")

    search_length = 0
    solution_length = 0
    start_time = time.time()
    count = 1
    for puzzle in fifteen_puzzles:
        print("Solving puzzle {} of fifteen puzzle".format(count))
        count += 1
        states_taken, final_puzzle = a_star(puzzle, FIFTEEN_PSOL, heuristic)
        search_length += states_taken
        if(final_puzzle is None):
            continue
        else:
            solution_length += final_puzzle.num_parents
    print(" %s seconds to complete 15 puzzle tests" % (time.time() - start_time))
    print("Number of steps to find an optimal solution: {}".format(search_length / len(fifteen_puzzles)))
    print("Number of steps for the optimal solution: {}".format(solution_length / len(fifteen_puzzles)))
    print("End A_Star 15 puzzle Test \n-------------------------------\n")

def test_single_astar(heuristic):
    """
    Test a* algorithm with given heuristic on a single eight puzzle

    """
    print("Testing a* on a single random 8 puzzle")
    random_puzzle = _gen_1_puzzle(3, EIGHT_PSOL)
    printPuzzle(random_puzzle)


    print("Testing A* with Heuristic")
    start_time = time.time()
    states_taken, final = a_star(random_puzzle, EIGHT_PSOL, heuristic)
    print(" %s seconds to solve with A* Heuristic" % (time.time() - start_time))
    print("{} steps to find an optimal solution".format(states_taken))
    print("{} steps for the actual optimal solution".format(final.num_parents))
    print("\n----------- End A* Huerist Testing ---------------\n")


def test_all_alg():
    """
    Test all algorithms dfs, bfs, and a* with all heuristics used
    on a single randomly generated 8 puzzle
    """
    print("Testing all algorithms on a random 8 puzzle")
    random_puzzle = _gen_1_puzzle(3, EIGHT_PSOL)
    printPuzzle(random_puzzle)

    print("\nTesting DFS")
    start_time = time.time()
    states_taken, final = dfs(random_puzzle, EIGHT_PSOL)
    if final is None:
        print("Error this puzzle is not solvable")
        return
    print(" %s seconds to solve with DFS" % (time.time() - start_time))
    print("{} steps to find an optimal solution".format(states_taken))
    print("{} steps for the actual optimal solution".format(final.num_parents))
    print("\n----------- End DFS Testing ---------------\n")

    print("Testing BFS")
    start_time = time.time()
    states_taken, final = bfs(random_puzzle, EIGHT_PSOL)
    print(" %s seconds to solve with BFS" % (time.time() - start_time))
    print("{} steps to find an optimal solution".format(states_taken))
    print("{} steps for the actual optimal solution".format(final.num_parents))
    print("\n----------- End BFS Testing ---------------\n")

    print("Testing A* with Hamming Heuristic")
    start_time = time.time()
    states_taken, final = a_star(random_puzzle, EIGHT_PSOL, hamming_distance)
    print(" %s seconds to solve with A* Hamming Distance Heuristic" % (time.time() - start_time))
    print("{} steps to find an optimal solution".format(states_taken))
    print("{} steps for the actual optimal solution".format(final.num_parents))
    print("\n----------- End A* Hamming Testing ---------------\n")

    print("Testing A* with Manhattan Heuristic")
    start_time = time.time()
    states_taken, final = a_star(random_puzzle, EIGHT_PSOL, manhattan_distance)
    print("%s seconds to solve with A* with Manhattan Distance Heuristic" % (time.time() - start_time))
    print("{} steps to find an optimal solution".format(states_taken))
    print("{} steps for the actual optimal solution".format(final.num_parents))
    print("\n----------- End A* Manhattan Testing ---------------\n")

    print("Testing A* with Linear Conflict Heuristic")
    start_time = time.time()
    states_taken, final = a_star(random_puzzle, EIGHT_PSOL, linear_conflict)
    print("%s seconds to solve with A* with Linear Conflict Heuristic" % (time.time() - start_time))
    print("{} steps to find an optimal solution".format(states_taken))
    print("{} steps for the actual optimal solution".format(final.num_parents))
    print("\n----------- End A* Manhattan Testing ---------------\n")


def _gen_n_puzzles(num_puzzles, m, final_state):
    puzzle_list = []
    for i in range(num_puzzles):
        puzzle = gen_puzzle_n(m)
        while not is_solvable(puzzle, final_state, m):
            puzzle = gen_puzzle_n(m)
        puzzle_list.append(puzzle)
    return puzzle_list

def _gen_1_puzzle(m, final_state):
    puzzle = []
    puzzle = gen_puzzle_n(m)
    while not is_solvable(puzzle, final_state, m):
        puzzle = gen_puzzle_n(m)
    return puzzle
