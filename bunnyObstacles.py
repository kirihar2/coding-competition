from collections import deque

def solution(m):
    print(bfs(m))
    
def bfs(p):
    def get_neighbors(m,pos):
        row=pos[0]
        col = pos[1]
        neighbors = []
        if row >0: 
            neighbors.append((row-1,col))
        if row < len(m) -1: 
            neighbors.append((row+1,col))
        if col < len(m[0]) -1: 
            neighbors.append((row,col+1))
        if col > 0: 
            neighbors.append((row,col-1))
        return neighbors
    def find(m,start,end):
        #BFS
        q = deque() 
        # (node,current length of path, has demolished wall)
        q.appendleft([start,0,False])
        min_dist = [[None for i in range(len(m[0]))] for j in range(len(m))]
        while len(q) > 0: 
            node,l,has_demolished = q.pop()
            curr_dist = min_dist[node[0]][node[1]]
            if curr_dist == None:
                min_dist[node[0]][node[1]] = l
            else:
                min_dist[node[0]][node[1]] = min(min_dist[node[0]][node[1]],l)

            neighbors = get_neighbors(m,node)
            for neighbor in neighbors:
                i,j = neighbor
                if min_dist[i][j] != None and min_dist[i][j]> 0:
                    continue
                if m[i][j] == 1 and not has_demolished:
                    q.appendleft([neighbor,l+1,True])
                elif m[i][j] == 1 and min_dist[i][j] == None:
                    min_dist[i][j] = -1
                elif m[i][j] == 0:
                    q.appendleft([neighbor,l+1,has_demolished])
                
        return 1
    return find(p,(0,0),(len(p)-1,len(p[0])-1))
def print_graph(m):
    for i in m:
	    for j in i:
	        print(j,end=' ')
	    print()


# m = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0]]
# print_graph(m)
# solution(m)


# -*- coding: utf-8 -*-
from collections import deque

# INDEX
#
# - class Board(list)
# - class Cell(tuple)
# - def answer(m)
# - def whatIfIRemovedThis(wall, m, start, end)


class Board(dict):

    traversable_value = 0
    nontraversable_value = 1
    unvisited_value = None
    unreachable_value = None

    def __init__(self, m):
        super(Board, self).__init__()
        self.default_factory = None
        self.height = len(m)
        self.width = len(m[0])
        for r, row in enumerate(m):
            assert self.width == len(row)
            for c, val in enumerate(row):
                self[r, c] = Cell(self, (r, c), val)

    def __getitem__(self, item):
        if isinstance(item, Cell):
            return self[item.coordinates].value
        return super(Board, self).__getitem__(item)

    def __setitem__(self, key, value):
        if isinstance(key, Cell):
            self[key.coordinates].value = value
        else:
            super(Board, self).__setitem__(key, value)


class Cell(object):
    """ A cell on a board is keyed by the cell's coordinates. """

    def __init__(self, board, coordinates, value):
        self.coordinates = coordinates
        self.board = board
        self.value = value
        self.min_dist_to = None

    def __repr__(self):
        return "%s @ %s" % (self.value, self.coordinates)

    def get_neighbors(self):
        """ Yields self's neighbors in up, down, left, right order. """

        r, c = self.coordinates
        for coordinates in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            try:
                yield self.board[coordinates]
            except KeyError:
                # outside of the board
                pass
    def __lt__(self,other):
        return self.value < other.value
    def is_traversable_in(self, board):
        return board[self] == board.traversable_value

    def is_a_wall_in(self, board):
        return board[self] == board.nontraversable_value

    def is_unvisited_in(self, board):
        return board[self] == board.unvisited_value

    def is_unreachable_from(self, other):
        # it is a bug if passed a non-cell
        assert isinstance(other, Cell)

        # hard to understand
        return other.min_dist_to[self] == self.board.unreachable_value

    # O(h*w) time complexity
    def gen_min_dist_to(self, board):
        """ A BFS Single Source Shortest Path algorithm appropriate for
        graphs with unweighted edges or graphs with weighted edges but
        where every edge has the same weight
        """

        if self.is_a_wall_in(board):
            return None

        min_dist_to = Board(
            [[Board.unvisited_value] * board.width] * board.height)
        min_dist_to[self] = 1

        cells = deque([self])

        while cells:  # h*w iterations
            cell = cells.popleft()
            min_dist_to_cell = min_dist_to[cell]

            for neighbor in cell.get_neighbors():
                is_traversable = neighbor.is_traversable_in(board)
                is_unvisited = neighbor.is_unvisited_in(min_dist_to)

                if is_traversable and is_unvisited:
                    min_dist_to_neighbor = min_dist_to_cell + 1

                    # Setting minDistsTo[.] to an int also marks it as visited.
                    min_dist_to[neighbor] = min_dist_to_neighbor

                    # Each cell gets appended to the cells queue only once.
                    cells.append(neighbor)

        self.min_dist_to = min_dist_to


def answer(board_martrix):
    """ O(h*w) time complexity """

    board = Board(board_martrix)
    best_conceivable_result = board.height + board.width - 1

    start = board[0, 0]
    end = board[board.height-1, board.width-1]

    start.gen_min_dist_to(board)  # O(h*w) time

    if end.is_unreachable_from(start):
        # This happens in test case 3 where it is necessary
        # to remove a wall to have a path from start to end.
        best_result = 2**31 - 1
    else:
        best_result = start.min_dist_to[end.coordinates].value

    if best_result == best_conceivable_result:
        # We cannot do any better than this.
        return best_conceivable_result

    end.gen_min_dist_to(board)  # O(h*w) time

    for r in range(board.height):     # h iterations
        for c in range(board.width):  # w iterations

            cell = board[r, c]

            if cell.is_a_wall_in(board):
                wall = cell

                # See if you can get a shorter path from start to end by
                # removing this wall.
                potentially_better_result = what_if_removed_this(
                    wall, board, start, end)  # O(1) time

                best_result = min(best_result, potentially_better_result)

    return best_result


def what_if_removed_this(wall, board_matrix, start, end):

    best_result = 2**31 - 1

    # [up, down, left, right] = list( wall.getNeighbors() )
    for incoming in wall.get_neighbors():
        for outgoing in wall.get_neighbors():

            # 16 iterations
            if (incoming == outgoing or  # already consider
                    incoming.is_a_wall_in(board_matrix) or
                    outgoing.is_a_wall_in(board_matrix) or
                    incoming.is_unreachable_from(start) or
                    outgoing.is_unreachable_from(end)):
                continue

            min_dist_from_start_to_incoming = start.min_dist_to[incoming]
            min_dist_from_outgoing_to_end = end.min_dist_to[outgoing]

            potentially_better_result = (
                min_dist_from_start_to_incoming + 1 +
                min_dist_from_outgoing_to_end)

            best_result = min(best_result, potentially_better_result)

    return best_result

m = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
print(answer(m))