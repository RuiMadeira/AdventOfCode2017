FILENAME = './input/AdventOfCode2017Day11Input.txt'


def challenge1():
    global CIRCULAR_LIST, INPUT_LENGTHS
    with open(FILENAME) as f:
        INPUT_LENGTHS = list(map(lambda x: int(x), f.readline().split(',')))
    current_position = 0
    skip_size = 0
    for length in INPUT_LENGTHS:
        print('Circular list: ' + str(CIRCULAR_LIST))
        reverse_end_position = current_position + length
        reverse_list(current_position, reverse_end_position)
        current_position = current_position + length + skip_size
        if current_position > len(CIRCULAR_LIST) - 1:
            current_position = current_position - len(CIRCULAR_LIST)
        skip_size += 1
    print(CIRCULAR_LIST)
    print(str(CIRCULAR_LIST[0] * CIRCULAR_LIST[1]))


challenge1()
