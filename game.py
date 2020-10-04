from time import sleep
import os

# 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# 2. Any live cell with two or three live neighbours lives on to the next generation.
# 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
# 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


def run(board):
    while True:
        board = next_generation(board)
        sleep(0.5)


def next_generation(board):
    size = len(board)
    result = []
    print("")
    print_board(board)
    for y in range(0, size):
        result.append(board[y].copy())
        for x in range(0, size):
            cell = board[y][x]
            cell_alive = cell == 1
            num_neighbours = neighbours(board, x, y)
            if cell_lives(cell_alive, num_neighbours):
                result[y][x] = 1
            else:
                result[y][x] = 0

    print_board(result)
    return result


def print_board(board):
    clear_terminal()
    size = len(board)
    print("")
    for y in range(0, size):
        for x in range(0, size):
            cell = board[y][x]
            end = ""
            if x == size - 1:
                end = "\n"
            print(str(cell), end=end, flush=True)


def clear_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Only handles POSIX
        os.system('clear')


def neighbours(board, x, y):
    size = len(board)
    count = 0
    if y > 0:
        count += board[y - 1][x]
    if y < size - 1:
        count += board[y + 1][x]
        if x > 0:
            count += board[y + 1][x - 1]
    if x > 0:
        count += board[y][x - 1]
        if y > 0:
            count += board[y - 1][x - 1]
    if x < size - 1:
        count += board[y][x + 1]
        if y > 0:
            count += board[y - 1][x + 1]
        if y < size - 1:
            count += board[y + 1][x + 1]
    return count


def cell_lives(cell_alive, num_neighbours):
    if num_neighbours < 2:
        return False
    elif num_neighbours > 3:
        return False
    elif cell_alive == False and num_neighbours != 3:
        return False

    return True


def cell_lives2(cell_alive, num_neighbours):
    if cell_alive == True:
        if num_neighbours < 2:
            return False
        elif num_neighbours > 3:
            return False
    else:
        if num_neighbours != 3:
            return False

    return True


def cell_lives3(cell_alive, num_neighbours):
    if cell_alive == True and num_neighbours == 2:
        return True
    if num_neighbours == 3:
        return True
    return False


if __name__ == '__main__':
    run([
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0],
    ])
