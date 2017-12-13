FILENAME = './input/AdventOfCode2017Day11Input.txt'

MATRIX_GRID_SIZE = 10000


def get_x_y(step, x, y):
    if step == 'n':
        y -= 2
    elif step == 'ne':
        y -= 1
        x += 2
    elif step == 'se':
        y += 1
        x += 2
    elif step == 's':
        y += 2
    elif step == 'sw':
        y += 1
        x -= 2
    elif step == 'nw':
        y -= 1
        x -= 2
    return x, y


def calc_hex_distance(x, y):
    hex_distance = 0
    step = ''
    while x != 0 or y != 0:
        if x > 0 and y > 0:
            step = 'nw'
        elif x > 0 and y <= 0:
            step = 'sw'
        elif x < 0 and y > 0:
            step = 'ne'
        elif x < 0 and y <= 0:
            step = 'se'
        elif x == 0 and y > 0:
            step = 'n'
        elif x == 0 and y < 0:
            step = 's'
        x, y = get_x_y(step, x, y)
        hex_distance += 1
    return hex_distance


def challenge1():
    x = (MATRIX_GRID_SIZE / 2) + 1.5
    y = (MATRIX_GRID_SIZE / 2) + 1
    max_hex_distance = 0
    with open(FILENAME) as f:
        for line in f:
            for step in line.split(','):
                x, y = get_x_y(step, x, y)
                x_distance = (MATRIX_GRID_SIZE / 2) + 1.5 - x
                y_distance = (MATRIX_GRID_SIZE / 2) + 1 - y
                current_hex_distance = calc_hex_distance(x_distance, y_distance)
                if current_hex_distance > max_hex_distance:
                    max_hex_distance = current_hex_distance
        x_distance = (MATRIX_GRID_SIZE / 2) + 1.5 - x
        y_distance = (MATRIX_GRID_SIZE / 2) + 1 - y
        print('Final hex distance: ' + str(calc_hex_distance(x_distance, y_distance)))
        print('Max hex distance: ' + str(max_hex_distance))


challenge1()
