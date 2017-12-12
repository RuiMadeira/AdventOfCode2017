TARGET_NUM = 277678
#TARGET_NUM = 13

def challenge1():
    #states = ["right", "up", "left", "down"]
    currentState = "right"
    x, y = 0, 0
    n_col_max, n_line_max = 1, 1
    n_col_min, n_line_min = -1, -1
    i = 1
    while i < TARGET_NUM:
        print("i: " + str(i))
        print("x: " + str(x))
        print("y: " + str(y))
        print("state: " + currentState)
        print("---------------")
        if x < n_col_max and currentState == "right":
            x += 1
            i += 1
            continue
        if y > n_line_min and currentState == "up":
            y -= 1
            i += 1
            continue
        if x > n_col_min and currentState == "left":
            x -= 1
            i += 1
            continue
        if y < n_line_max and currentState == "down":
            y += 1
            i += 1
            continue

        if x == n_col_max and currentState == "right":
            n_col_max += 1
            currentState = "up"
            continue
        if x == n_col_min and currentState == "left":
            n_col_min += -1
            currentState = "down"
            continue
        if y == n_line_max and currentState == "down":
            n_line_max += 1
            currentState = "right"
            continue
        if y == n_line_min and currentState == "up":
            n_line_min += -1
            currentState = "left"
            continue
    steps_required = abs(x) + abs(y)
    print(steps_required)


def challenge2():
    matrix_size = TARGET_NUM // 100
    matrix = [[0 for x in range(matrix_size)] for y in range(matrix_size)]
    displacement = matrix_size // 2
    # states = ["right", "up", "left", "down"]
    currentState = "right"
    x, y = 0, 0
    n_col_max, n_line_max = 1, 1
    n_col_min, n_line_min = -1, -1
    i = 0
    matrix[displacement][displacement] = 1
    while i < TARGET_NUM:
        print("i: " + str(i))
        print("x: " + str(x))
        print("y: " + str(y))
        print("state: " + currentState)
        #print(matrix)
        print("---------------")
        if x < n_col_max and currentState == "right":
            x += 1
            i = calculate_neighbours(matrix, x, y, displacement)
            matrix[displacement + x][displacement + y] = i
            continue
        if y > n_line_min and currentState == "up":
            y -= 1
            i = calculate_neighbours(matrix, x, y, displacement)
            matrix[displacement + x][displacement + y] = i
            continue
        if x > n_col_min and currentState == "left":
            x -= 1
            i = calculate_neighbours(matrix, x, y, displacement)
            matrix[displacement + x][displacement + y] = i
            continue
        if y < n_line_max and currentState == "down":
            y += 1
            i = calculate_neighbours(matrix, x, y, displacement)
            matrix[displacement + x][displacement + y] = i
            continue

        if x == n_col_max and currentState == "right":
            n_col_max += 1
            currentState = "up"
            continue
        if x == n_col_min and currentState == "left":
            n_col_min += -1
            currentState = "down"
            continue
        if y == n_line_max and currentState == "down":
            n_line_max += 1
            currentState = "right"
            continue
        if y == n_line_min and currentState == "up":
            n_line_min += -1
            currentState = "left"
            continue
    print(i)


def calculate_neighbours(matrix, x, y, displacement):
    sum_total = 0

    sum_total += matrix[displacement + x + 1][displacement + y]
    sum_total += matrix[displacement + x][displacement + y + 1]

    sum_total += matrix[displacement + x - 1][displacement + y]
    sum_total += matrix[displacement + x][displacement + y - 1]

    sum_total += matrix[displacement + x + 1][displacement + y + 1]
    sum_total += matrix[displacement + x - 1][displacement + y - 1]

    sum_total += matrix[displacement + x + 1][displacement + y - 1]
    sum_total += matrix[displacement + x - 1][displacement + y + 1]
    return sum_total


challenge2()
