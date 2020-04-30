import itertools
import heapq


class IDAstarApproach:
    def heuristic(self, board, target):
        """
        :param board: current state of the board for which heuristic is to be calculated
        :param target: target board
        :return: heuristic calculated using Hamming distance
        """
        heuristic = 0
        for i in range(len(board)):
            if target[i] != board[i]:
                heuristic += 1

        return heuristic

    def npuzzle(self, puzzle):
        """
        :param puzzle: input puzzle or the starting state of the puzzle
        :return: depth of the search tree or the number of moves it takes to solve the puzzle
        """
        # initialize the required varaibles
        rows = len(puzzle)
        col = len(puzzle[0])
        initial_board = list(itertools.chain(*puzzle))
        target_board = [i for i in range(1, rows * col)] + [0]

        # all information (such as depth, f_score, index of the blank tile)
        # related to each possible state is stored in a heap
        state_info = [(0, 0, initial_board.index(0), initial_board)]
        heapq.heapify(state_info)
        # a dictionary is maintained to check if the state has already been explored previously
        cost = dict()
        cost[tuple(initial_board)] = 0

        while state_info:
            f_score, g_score, zero_index, current_board = heapq.heappop(state_info)
            print("popped from heap", f_score, "for board", current_board)

            if current_board == target_board:
                return g_score

            # shift blank tile to either right, left, top or bottom
            for zero_shift in (1, -1, col, -col):
                new_zero_index = zero_index + zero_shift

                # check if the blank tile is shifted by just 1 step in either of 4 directions
                if abs(int(zero_index / col) - int(new_zero_index / col)) + \
                        abs(zero_index % col - new_zero_index % col) != 1:
                    continue

                # check if the blank tile is within the size of the board
                if 0 <= new_zero_index < rows * col:
                    # swap position of blank tile with new position
                    new_board = current_board.copy()
                    temp = new_board[new_zero_index]
                    new_board[new_zero_index] = new_board[zero_index]
                    new_board[zero_index] = temp

                    # compute heuristic and add it along with depth to get f_score
                    f_score = g_score + 1 + self.heuristic(new_board, target_board)

                    # if cost already exists then check if new f_score is less than it
                    if f_score < cost.get(tuple(new_board), 999):
                        cost[tuple(new_board)] = f_score
                        heapq.heappush(state_info, (f_score, g_score + 1, new_zero_index, new_board))

        return -1


board = AstarApproach()
# print("number of moves required to solve the puzzle using IDA* is", board.npuzzle([[4,1,2],[5,0,3]]))
print("number of moves required to solve the puzzle using IDA* is", board.npuzzle([[3,2,4],[1,5,0]]))