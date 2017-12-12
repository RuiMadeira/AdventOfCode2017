FILENAME = './input/AdventOfCode2017Day7Input.txt'

def get_root(tree):
    for node in tree.values():
        if node['parent'] == '':
            return node['name']


def set_parents(tree):
    for node in tree.values():
        for child in node['childs']:
            tree[child]['parent'] = node['name']


def challenge1():
    programs = {}
    programs_name = ''
    with open(FILENAME) as f:
        for line in f:
            components = line.split()
            programs_name = components.pop(0)
            weight = components.pop(0).replace('(', '').replace(')', '')
            if len(components) > 0:
                components.pop(0)
                childs = []
            for child in components:
                childs.append(child.replace(',', ''))
            program = {
                'name': programs_name,
                'weight': weight,
                'childs': childs,
                'parent': ''
            }
            programs[programs_name] = program
    set_parents(programs)
    print(get_root(programs))


def get_weights(tree, node):
    if len(node['childs']) == 0:
        return 0
    else:
        sum_total = 0
        for child in node['childs']:
            sum_total += get_weights(tree, tree[child]) + tree[child]['weight']
        return sum_total


def compute_child_weights(tree):
    for node in tree.values():
        node['weights'] = get_weights(tree, node)


def get_problem(weights):
    buckets = []
    for weight in weights:
        if len(buckets) == 0:
            buckets.append([weight])
    if len(buckets) > 0:
        for bucket in buckets:
            if len(bucket) == 1:
                return bucket


def are_balanced_(weights):
    if len(weights) == 0:
        return True
    weight_choosen = weights[0]
    for weight in weights:
        if weight != weight_choosen:
            return False
    return True


def get_winning_balance(weights):
    weights_counts = {}
    for weight in weights:
        if weight not in weights_counts:
            weights_counts[weight] = 1
        else:
            weights_counts[weight] += 1
    max = 0
    number = 0
    for i in weights_counts.keys():
        if weights_counts[i] > max:
            max = weights_counts[i]
            number = i
    return number


# for all childs if they have same balance then you are the issue and value should be balance - sum of childs
# else call function with "odd child"
def get_problem_childs(tree, node, balance):
    weights = []
    for child in node['childs']:
        weights.append(tree[child]['weight'] + tree[child]['weights'])
    if are_balanced_(weights):
        return balance - node['weights']
    else:
        winning_balance = get_winning_balance(weights)
        for child in node['childs']:
            if tree[child]['weight'] + tree[child]['weights'] != winning_balance:
                return get_problem_childs(tree, tree[child], winning_balance)


def challenge2():
    programs = {}
    programs_name = ''
    with open(FILENAME) as f:
        for line in f:
            components = line.split()
            programs_name = components.pop(0)
            weight = int(components.pop(0).replace('(', '').replace(')', ''))
            childs = []
            if len(components) > 0:
                components.pop(0)
            for child in components:
                childs.append(child.replace(',', ''))
            program = {
                'name': programs_name,
                'weight': weight,
                'childs': childs,
                'parent': ''
            }
            programs[programs_name] = program
    set_parents(programs)
    compute_child_weights(programs)
    root = programs[get_root(programs)]
    print(programs)
    print(get_problem_childs(programs, root, root['weight']))


challenge2()
