FILENAME = './input/AdventOfCode2017Day6Input.txt'

# Aprendizagem: Demorei mesmo muito tempo para resolver a 2 tarefa. Como melhoramento diria que devia ter
# reflectido mais sobre o problema em si, o que era pedido e no contexto do que era pedido. Pois talvez por ai
# tivesse percebido logo ou entendido que a minha primeira percepção não fazia sentido.
# Ler e reflectir!

def get_chosen_block(memory_blocks):
    max_block = max(memory_blocks)
    indexes = []
    i = 0
    for block in memory_blocks:
        if block == max_block:
            indexes.append(i)
        i += 1
    indexes.sort()
    return indexes[0]


def redistribute(memory_blocks, chosen_index):
    iterations = memory_blocks[chosen_index]
    memory_blocks[chosen_index] = 0
    index_to_add = chosen_index + 1
    while iterations > 0:
        if index_to_add >= len(memory_blocks):
            index_to_add = 0
        memory_blocks[index_to_add] += 1
        index_to_add += 1
        iterations -= 1
    return memory_blocks


def challenge1():
    memory_blocks = []
    with open(FILENAME) as f:
        for memory_line in f:
            input_blocks = memory_line.split()
            for block in input_blocks:
                memory_blocks.append(int(block))
    states_seen = []
    cycles = 0
    while str(memory_blocks) not in states_seen:
        cycles += 1
        states_seen.append(str(memory_blocks))
        memory_blocks = redistribute(memory_blocks, get_chosen_block(memory_blocks))
    print(cycles)


def challenge2():
    memory_blocks = []
    with open(FILENAME) as f:
        for memory_line in f:
            input_blocks = memory_line.split()
            for block in input_blocks:
                memory_blocks.append(int(block))
    init_state = ""
    states_seen = []
    cycles = 0
    cycles_init = 0
    first = True
    while True:
        cycles += 1
        states_seen.append(str(memory_blocks))
        memory_blocks = redistribute(memory_blocks, get_chosen_block(memory_blocks))
        if str(memory_blocks) == init_state:
            break
        if (str(memory_blocks) in states_seen) and first:
            cycles_init = cycles
            init_state = str(memory_blocks)
            first = False
    print(cycles-cycles_init)


challenge2()
