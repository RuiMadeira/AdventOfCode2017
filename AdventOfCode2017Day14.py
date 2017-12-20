from functools import reduce
import binascii

INPUT = 'jxqlasbh'
NUM_OF_ROWS = 128

CIRCULAR_LIST = list(range(0, 256))
INPUT_LENGTHS = []
END_SEQUENCE = [17, 31, 73, 47, 23]
TOTAL_ROUNDS = 64


# Using the hasher from day 10

def reverse_list(init_position, end_position):
    global CIRCULAR_LIST
    #print('Init Position: ' + str(init_position))
    #print('End Position: ' + str(end_position))
    if end_position < len(CIRCULAR_LIST):
        selected_part = CIRCULAR_LIST[init_position:end_position:]
    else:
        selected_part = CIRCULAR_LIST[init_position::]
        offset = end_position - len(CIRCULAR_LIST)
        selected_part = selected_part + CIRCULAR_LIST[0:offset:]
    #print('Selected part: ' + str(selected_part))
    reversed_part = selected_part[::-1]
    #print('Reversed part: ' + str(reversed_part))
    for i in reversed_part:
        if init_position > len(CIRCULAR_LIST) - 1:
            init_position = 0
        CIRCULAR_LIST[init_position] = i
        init_position += 1


def calc_dense_hash():
    pos = 0
    dense_hash = []
    for i in range(0, 16):
        to_hash = CIRCULAR_LIST[pos:pos+16]
        hash_result = reduce(lambda x, y: x ^ y, to_hash)
        pos += 16
        dense_hash.append(hash_result)
    return dense_hash


def dense_hash_to_hex(dense_hash):
    result = list(map(lambda x: '0x{:02x}'.format(x).replace('0x', ''), dense_hash))
    return ''.join(result)


def hasher(input):
    global CIRCULAR_LIST, INPUT_LENGTHS
    INPUT_LENGTHS = list(map(lambda x: ord(x), list(input)))
    INPUT_LENGTHS = INPUT_LENGTHS + END_SEQUENCE
    i = 0
    current_position = 0
    skip_size = 0
    while i < 64:
        for length in INPUT_LENGTHS:
            #print('Circular list: ' + str(CIRCULAR_LIST))
            reverse_end_position = current_position + length
            reverse_list(current_position, reverse_end_position)
            current_position = current_position + length + skip_size
            if current_position > len(CIRCULAR_LIST) - 1:
                current_position = current_position % len(CIRCULAR_LIST)
            skip_size += 1
        i += 1
    dense_hash = calc_dense_hash()
    #print('Dense Hash: ' + str(dense_hash))
    final_representation = dense_hash_to_hex(dense_hash)
    #print(final_representation)
    return final_representation


def challenge1():
    global CIRCULAR_LIST
    occupied_count = 0
    CIRCULAR_LIST = list(range(0, 256))
    for i in range(0, NUM_OF_ROWS):
        hashed = hasher(INPUT + '-' + str(i))
        line = list(map(lambda x: bin(x).replace('0b', ''), list(binascii.unhexlify(hashed))))
        for n in line:
            occupied_count += n.count('1')
        print(i)
        CIRCULAR_LIST = list(range(0, 256))
    print(occupied_count)


def count_region(matrix, i):
    if i not in matrix.keys():
        return
    if matrix[i] == '1':
        matrix[i] = 'c'
        count_region(matrix, (i[0] + 1, i[1]))
        count_region(matrix, (i[0] - 1, i[1]))
        count_region(matrix, (i[0], i[1] + 1))
        count_region(matrix, (i[0], i[1] - 1))


def count_regions(matrix):
    regions = 0
    for i in matrix.keys():
        if matrix[i] != 'c' and matrix[i] == '1':
            regions += 1
            count_region(matrix, i)
    return regions


def challenge2():
    global CIRCULAR_LIST
    occupied_count = 0
    CIRCULAR_LIST = list(range(0, 256))
    matrix = {}
    for row in range(0, NUM_OF_ROWS):
        hashed = hasher(INPUT + '-' + str(row))
        line = list(map(lambda x: '{0:08b}'.format(x), list(binascii.unhexlify(hashed))))
        column = 0
        for i in line:
            for digit in i:
                matrix[row, column] = digit
                column += 1
        CIRCULAR_LIST = list(range(0, 256))
    print(count_regions(matrix))


challenge2()
