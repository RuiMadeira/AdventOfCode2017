INPUT_FILE = 'AdventOfCodeDay8Input.txt'


def constraint_fulfilled(registers, register_to_compare, condition, value):
    register_value = 0
    if register_to_compare in registers:
        register_value = registers[register_to_compare]
    if condition == '>':
        return register_value > value
    if condition == '<':
        return register_value < value
    if condition == '>=':
        return register_value >= value
    if condition == '<=':
        return register_value <= value
    if condition == '==':
        return register_value == value
    if condition == '!=':
        return register_value != value
    return False


def get_value(instruction, value):
    new_value = value
    if instruction == 'dec':
        new_value = - new_value
    return new_value


def operate_command(registers, register_to_operate, instruction, value):
    if register_to_operate not in registers:
        registers[register_to_operate] = get_value(instruction, value)
    else:
        registers[register_to_operate] += get_value(instruction, value)


def get_max(registers):
    max_register = 0
    for i in registers.values():
        if i > max_register:
            max_register = i
    return max_register


def challenge1():
    with open(INPUT_FILE) as f:
        registers = {}
        for line in f:
            command = line.split()
            register_to_operate = command[0]
            instruction = command[1]
            value = int(command[2])
            register_to_compare = command[4]
            condition = command[5]
            value_to_compare = int(command[6])
            if constraint_fulfilled(registers, register_to_compare, condition, value_to_compare):
                operate_command(registers, register_to_operate, instruction, value)
            print(registers)
        print(get_max(registers))


def challenge2():
    with open(INPUT_FILE) as f:
        registers = {}
        max_register = 0
        for line in f:
            command = line.split()
            register_to_operate = command[0]
            instruction = command[1]
            value = int(command[2])
            register_to_compare = command[4]
            condition = command[5]
            value_to_compare = int(command[6])
            if constraint_fulfilled(registers, register_to_compare, condition, value_to_compare):
                operate_command(registers, register_to_operate, instruction, value)
            current_max = get_max(registers)
            if current_max > max_register:
                max_register = current_max
        print(max_register)


challenge2()
