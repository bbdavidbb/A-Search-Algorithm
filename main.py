from puzzle import is_solvable, printPuzzle
from graph import dfs, bfs, a_star, manhattan_distance, hamming_distance, linear_conflict, reconstruct_path
from tests import test_single_astar, test_algorithm_eight, test_a_star_eight, test_a_star_fifteen, test_all_alg

def main():

    print("Enter 1 to test DFS,BFS, and A* on a single random 8 puzzle problem")
    print("Enter 2 to test DFS on 10 random 8-puzzle problems ")
    print("Enter 3 to test BFS on 10 random 8-puzzle problems ")
    print("Enter 4 to test A* with Hamming Distance Heuristic on 10 random 8-puzzle problems ")
    print("Enter 5 to test A* with Manhattan Distance Heuristic on 10 random 8-puzzle problems ")
    print("Enter 6 to test A* with Linear-Conflict Heuristic on 10 random 8-puzzle problems ")
    user_input = input("Enter here: ")

    if user_input == "1":
        test_all_alg()
    elif user_input == "2":
        test_algorithm_eight(dfs)
    elif user_input == "3":
        test_algorithm_eight(bfs)
    elif user_input == "4":
        test_a_star_eight(hamming_distance)
    elif user_input == "5":
        test_a_star_eight(manhattan_distance)
    elif user_input == "6":
        test_a_star_eight(linear_conflict)
    else:
        print("Invalid input")


if __name__ == "__main__":
    main()