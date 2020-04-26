import math
from collections import deque
from puzzle import coord_of_tile, gen_puzzle_n, printPuzzle, up, down, left, right
from bisect import insort, bisect_left
from queue import PriorityQueue


class Node:
    """"
    Represents a puzzle node in the graph

    Attributes:
    state: A 2D list representing the puzzle
    parent: The parent Node of this Node
    direction: The move that was taken to end up at this Node
    num_parents: The distance from this node to root; the iniitial puzzle
    """
    def __init__(self, state, parent, direction):
        """
        The constructor
        """
        self.state = state
        self.parent = parent
        self.direction = direction
        if parent is None:
            self.num_parents = 0
        else:
            self.num_parents = parent.num_parents + 1

    # a fix for the priority queue error
    def __lt__(self, other):
        return False


def dfs(initial_state, final_state):
    """
    Perform a depth first search with the given initial and final states

    @param initial_state(2D List) The initial puzzle
    @param final_state(2D list) The final desired puzzle a 2D list

    @return
    states_taken (int): The number of states traversed to find the solution
    current (Node): The final state of the search; None of if not found

    """
    stack = [] # open set; The stack used in DFS
    states_taken = [] # closed set used to a a sort of lookup table
    current = Node(initial_state, None, None)

    def add_state(n_state, direction):
        if state_is_valid(n_state, states_taken):
            stack.append(Node(n_state, current, direction))

    while current.state != final_state:
        insort(states_taken, current.state) # add current to list while maintaining a sorted order
        add_state(up(current.state), "up")
        add_state(down(current.state), "down")
        add_state(left(current.state), "left")
        add_state(right(current.state), "right")

        if not len(stack) == 0:
            current = stack.pop()
        else: # failed to find a solution
            return len(states_taken), None

    return len(states_taken), current


def bfs(initial_state, final_state):
    """
    Perform a Breadth First Search with the given initial and final states

    @param initial_state(2D List) The initial puzzle
    @param final_state(2D list) The final desired puzzle a 2D list

    @return
    states_taken (int): The number of states traversed to find the solution
    current (Node): The final state of the search; None of if not found

    """
    queue = deque()
    states_taken = []
    current = Node(initial_state, None, None)

    def add_state(n_state, direction):
        if state_is_valid(n_state, states_taken):
            queue.append(Node(n_state, current, direction))

    while current.state != final_state:
        insort(states_taken, current.state)  # add current to list while maintaining a sorted order
        add_state(up(current.state), "up")
        add_state(down(current.state), "down")
        add_state(left(current.state), "left")
        add_state(right(current.state), "right")

        if not len(queue) == 0:
            current = queue.popleft()
        else:  # failed to find a solution
            return len(states_taken), None

    return len(states_taken), current

def a_star(initial_state, final_state, heuristic):
    """
    Perform a A* Search with the given initial and final states

    @param initial_state(2D List) The initial puzzle
    @param final_state(2D list) The final desired puzzle a 2D list
    @param heuristic(function) The heuristic function used in the equation f = g(x) + h(x)

    @return
    states_taken (int): The number of states traversed to find the solution
    current (Node): The final state of the search; None of if not found

    """
    p_queue = PriorityQueue() # open list
    states_taken = [] # closed list will maintain nodes with have already seen
    current = Node(initial_state, None, None) # initial node

    # Add state to the p_queue if it has not been seen
    def add_state(n_state, direction):
        if state_is_valid(n_state, states_taken): # detertermine if the state has not been seen
            node_to_add = Node(n_state, current, direction) # make state a node
            cost = node_to_add.num_parents + heuristic(node_to_add.state, final_state) # compute heuristic cost
            p_queue.put( (cost, node_to_add) ) # insert node into priority queue according to computed cost

    while current.state != final_state:
        insort(states_taken, current.state)  # put current into states_taken while maintain sorted order for searching
        add_state(up(current.state), "up")  # go through all directions and add their nodes to states_taken if valid
        add_state(down(current.state), "down")
        add_state(left(current.state), "left")
        add_state(right(current.state), "right")

        if not p_queue.qsize() == 0:  # deque from p_queue and make that node current node to search
            _, n_add = p_queue.get_nowait()
            current = n_add
        else: # failed to find a solution i.e we're cycling through nodes we have already seen
            return len(states_taken), None

    return len(states_taken), current

def state_is_valid(state, states_taken):
    """
    Determine if the state is in the collection

    @param state (2D list) The state to find
    @param states_taken (list) The list of states we have seen

    @return True if the state has not been seen False otherwise

    """
    return (state != None and find_state(states_taken, state) == None)


def find_state(collection, value):
    """
    Determine if the state is in the collection using binary search

    @param value (2D list) The state to find
    @param collection (list) The list of states we have seen

    @return None if the state hasn't been seen; an int otherwise

    """
    i = bisect_left(collection, value)
    if i != len(collection) and collection[i] == value:
        return i
    return None


def reconstruct_path(node):
    """
    Given the final node a search reconstruct the path from that node
    to initial then inverse the list to give the path
    from initial to final node

    @param node (2d list) The final node

    @return path (list) The reverse path from node to parent
    """
    path = []
    while node.direction != None:
        path.append(node)
        node = node.parent
    path.reverse()
    return path


def hamming_distance(current_state, final_state):
    """
    Counts the number of misplaced tiles between current and final states

    @param current_state (2d list) The current state of the puzzle
    @param final_state (2d list) The desired final state of the puzzle

    @return misplaced (int) A count of the number of misplaced tiles
    """
    misplaced = 0
    for x, row in enumerate(current_state):
        for y, tile in enumerate(row):
            if tile != final_state[x][y]:
                misplaced += 1
    return misplaced

def manhattan_distance(current_state, final_state):
    """
    Also known as taxicab geometry find the distance between current and final state

    @param current_state (2d list) The current state of the puzzle
    @param final_state (2d list) The desired final state of the puzzle

    @return distance_betwwen (int) The distance between the states
    """
    distance_between = 0
    for row in current_state:
        for tile in row:
            current_coords, final_coords = coord_of_tile(current_state, tile), coord_of_tile(final_state, tile)
            distance_between += abs(current_coords[0] - final_coords[0]) + abs(current_coords[1] - final_coords[1])
    return distance_between


def linear_conflict(current_state, final_state):
    """
    Count the number of conflicts i.e a tile in the current state is being blocked
    by another tile in it's final desired position in either rowise or columnwise
    Used in tandem with Manhattan Distance for better heuristics

    @param current_state (2d list) The current state of the puzzle
    @param final_state (2d list) The desired final state of the puzzle

    @return lin_conflicts (int) The number of linear conflicts + the manhattan distance
    """
    lin_conflicts = 0
    n = int(math.sqrt(len(current_state)))
    for row in range(n):
        for col in range(n):
            if current_state[row][col] == 0:
                continue
            tile = current_state[row][col]
            final_x, final_y = coord_of_tile(final_state, tile)
            if row == final_x:
                for r_col in range(col, n):
                    if tile > current_state[row][r_col]:
                        lin_conflicts += 1
            elif col == final_y:
                for c_row in range(row, n):
                    if tile > current_state[c_row][col]:
                        lin_conflicts +=1

    return manhattan_distance(current_state, final_state) + 2 * lin_conflicts

