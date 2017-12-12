FILENAME = './input/AdventOfCode2017Day5Input.txt'


def challenge1():
    instruction_list = []
    with open(FILENAME) as f:
        for instruction in f:
            instruction_list.append(int(instruction))
    step_counter = 0
    i = 0
    while 0 <= i < len(instruction_list):
        cur_i = i
        i += instruction_list[i]
        instruction_list[cur_i] += 1
        step_counter += 1
    print(step_counter)

def challenge2():
    instruction_list = []
    with open(FILENAME) as f:
        for instruction in f:
            instruction_list.append(int(instruction))
    step_counter = 0
    i = 0
    while 0 <= i < len(instruction_list):
        cur_i = i
        i += instruction_list[i]
        if instruction_list[cur_i] >= 3:
            instruction_list[cur_i] -= 1
        else:
            instruction_list[cur_i] += 1
        step_counter += 1
    print(step_counter)

challenge2()
