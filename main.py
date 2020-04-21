from puzzle import gen_puzzle_n, printPuzzle
from graph import dfs, a_star, reconstruct_path


# things to add:
# a way to tell if an n-puzzle problem is solvable
# other algorithms such as bfs or even djikstra
# different heuristics for a*
# expand test cases beyond 8-puzzle problems
def main():
    # some testing
    random_test = gen_puzzle_n(3)
    final_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    fast_test = [[5,4,0], [6, 3, 8], [2, 1, 7]] # 164 steps for a* and 66666 for dfs

    states_taken, path = a_star(fast_test, final_state)
    #states_taken, path = dfs(fast_test, final_state)

    print("Initial Puzzle: ")
    printPuzzle(fast_test)
    print("------------------")

    step_count = 1
    for next_puzzle in path:
        print("Step number: {}".format(step_count))
        step_count += 1
        printPuzzle(next_puzzle.state)
        print(next_puzzle.direction)
        print("---------")

    print("only {} steps were needed to arrive at the solution".format(len(path)))
    print("{} actual steps were needed to find the solution ".format(states_taken))

if __name__ == "__main__":
    main()