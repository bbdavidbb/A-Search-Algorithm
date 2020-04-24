
from graph import dfs, bfs, a_star, manhattan_distance, hamming_distance, linear_conflict

from tests import test_single_astar, test_algorithm_eight, test_a_star_eight, test_a_star_fifteen, test_all_alg

def main():
    test_all_alg()
    # test_algorithm_eight(dfs)
    # test_algorithm_eight(bfs)
    # test_a_star_eight(hamming_distance)
    # test_a_star_eight(manhattan_distance)
    # test_a_star_eight(linear_conflict)



if __name__ == "__main__":
    main()