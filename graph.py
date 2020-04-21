from puzzle import coord_of_tile, gen_puzzle_n, printPuzzle, up, down, left, right
from bisect import insort, bisect_left
from queue import PriorityQueue


class Node:
    def __init__(self, state, parent, direction):
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
    stack = []
    states_taken = []
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

    return len(states_taken), reconstruct_path(current)

def a_star(initial_state, final_state):
    p_queue = PriorityQueue() # open list
    states_taken = [] # closed list
    current = Node(initial_state, None, None)

    def add_state(n_state, direction):
        if state_is_valid(n_state, states_taken):
            node_to_add = Node(n_state, current, direction)
            cost = node_to_add.num_parents + manhattan_distance(node_to_add.state, final_state) # heuristic function
            p_queue.put( (cost, node_to_add) )


    while current.state != final_state:
        insort(states_taken, current.state)
        add_state(up(current.state), "up")
        add_state(down(current.state), "down")
        add_state(left(current.state), "left")
        add_state(right(current.state), "right")

        if not p_queue.qsize() == 0:
            _, n_add = p_queue.get_nowait()
            current = n_add
        else: # failed to find a soultion
            return len(states_taken), None

    return len(states_taken), reconstruct_path(current)

def state_is_valid(state, states_taken):
	return (state != None and find_state(states_taken, state) == None)

# find the state if it exists using binary search
def find_state(collection, value):
	i = bisect_left(collection, value)
	if i != len(collection) and collection[i] == value:
		return i
	return None

def reconstruct_path(node):
    path = []
    while node.direction != None:
        path.append(node)
        node = node.parent
    path.reverse()
    return path

def manhattan_distance(current_state, final_state):
	distance_between = 0
	for column in current_state:
		for tile in column:
			current_coords, final_coords = coord_of_tile(current_state, tile), coord_of_tile(final_state, tile)
			distance_between += abs(current_coords[0] - final_coords[0]) + abs(current_coords[1] - final_coords[1])
	return distance_between

