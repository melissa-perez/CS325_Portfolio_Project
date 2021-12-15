# Author: Melissa Marie Perez
# Date: 11/21/2021
# Description: The Puzzle.py files contains
# the solve_puzzle and helper functions. The solve_puzzle
# function takes in a 2-D list of characters that are either
# the character -(empty) or #(blocked). It will then attempt
# to solve a path from the start to end locations provided(tuples).
# If no path exists, None is returned.
# If a path exists, the path(tuples) taken to reach the end and the
# LRUD string representation of the directions are returned as a list.

from collections import deque
from typing import List


def solve_puzzle(Board: List[List], Source: tuple, Destination: tuple):
    """
    Takes in a puzzle Board and a source and destination to solve
    the path. Uses helper functions to split up logic.

    :param Board: List[List]
    :param Source: tuple
    :param Destination: tuple
    :return: List[List] or None
    """
    row_count = len(Board)
    col_count = len(Board[0])
    prev = solve(Board, Source, Destination, row_count, col_count)

    return construct_path(Source, Destination, prev)


def solve(puzzle: List[List], source: tuple, destination: tuple, rows: int, cols: int):
    """
    This helper method performs a breadth first search to find a path to
    the destination location from the source. Either the destination location is
    eventually found or no path is possible. The result is a 2d matrix of previous
    steps taken for each square which is used to construct the path in construct_path.

    :param destination: tuple
    :param puzzle: List[List]
    :param source: tuple
    :param rows: int
    :param cols: int
    :return: List[List]
    """
    q = deque()
    q.append(source)
    visited = [[False] * cols for _ in range(rows)]
    visited[source[0]][source[1]] = True
    previous_tracker = [[None] * cols for _ in range(rows)]
    found_destination = False

    while q and not found_destination:
        current_x, current_y = q.popleft()
        for adj_x, adj_y, direction in [[0, 1, 'R'], [1, 0, 'D'], [0, -1, 'L'], [-1, 0, 'U']]:
            neighbor_x = current_x + adj_x
            neighbor_y = current_y + adj_y
            # check to see if valid neighbor, not blocked (#), and not yet visited
            if rows > neighbor_x >= 0 and cols > neighbor_y >= 0 \
                    and puzzle[neighbor_x][neighbor_y] != "#" and not \
                    visited[neighbor_x][neighbor_y]:
                q.append((neighbor_x, neighbor_y))
                visited[neighbor_x][neighbor_y] = True
                previous_tracker[neighbor_x][neighbor_y] = (current_x, current_y, direction)
                if (neighbor_x, neighbor_y) == destination:
                    found_destination = True
                    break
    return previous_tracker


def construct_path(source: tuple, destination: tuple, previous: List[List]):
    """
    Reconstructs the path taken to go from destination to source.
    Path and directions must be reversed.
    Both the directions and x,y coordinates are returned.
    If no path was found, then None is returned.

    :param source: tuple
    :param destination: tuple
    :param previous: List[List]
    :return: List[List] or None
    """
    path = []
    directions = []
    at = destination
    path.append(at)
    at = previous[at[0]][at[1]]
    while at:
        path.append((at[0], at[1]))
        directions.append(at[2])
        at = previous[at[0]][at[1]]
    path.reverse()
    directions.reverse()
    if (path[0][0], path[0][1]) == source:
        return [path, directions]
    return None


if __name__ == "__main__":
    board_input = [
        ['-', '-', '-', '-', '-'],
        ['-', '-', '#', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['#', '-', '#', '#', '-'],
    ]
    start = (0, 0)
    end = (3, 4)
    print(solve_puzzle(board_input, start, end))
    board_input = [['-', '#', '-'], ['-', '#', '-'], ['-', '#', '-']]
    start = (0, 0)
    end = (2, 2)
    print(solve_puzzle(board_input, start, end))
