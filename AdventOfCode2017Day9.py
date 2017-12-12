FILENAME = './input/AdventOfCode2017Day9Input.txt'
GROUP_ID_COUNTER = 1
GROUPS = dict(parent='', id=0, value='', children=[])
CURRENT_GROUP = GROUPS


def analyze_non_garbage_char(char):
    global GROUP_ID_COUNTER, CURRENT_GROUP, GROUPS
    if char == '{':
        new_group = {
            'parent': CURRENT_GROUP,
            'id': GROUP_ID_COUNTER,
            'value': '',
            'children': []
        }
        CURRENT_GROUP['children'].append(new_group)
        CURRENT_GROUP = new_group
        GROUP_ID_COUNTER += 1
    elif char == '}':
        CURRENT_GROUP = CURRENT_GROUP['parent']
    elif ',':
        return
    else:
        CURRENT_GROUP['value'] = CURRENT_GROUP['value'] + char


def current_degree_count(group, degree):
    total_score = degree
    if len(group['children']) == 0:
        return degree
    else:
        current_degree = degree + 1
        for child in group['children']:
            total_score += current_degree_count(child, current_degree)
        return total_score


def count_score():
    total_score = 0
    current_degree = 1
    for child in GROUPS['children']:
        total_score += current_degree_count(child, current_degree)
    return total_score


def challenge1():
    inside_garbage = False
    ignore_next = False
    garbage_count = 0
    with open(FILENAME) as f:
        while True:
            char = f.read(1)
            if not char:
                break
            if ignore_next:
                ignore_next = False
            else:
                if char == '<':
                    if inside_garbage:
                        garbage_count += 1
                    else:
                        inside_garbage = True
                elif char == '>':
                    inside_garbage = False
                elif char == '!':
                    ignore_next = True
                else:
                    if not inside_garbage:
                        analyze_non_garbage_char(char)
                    else:
                        garbage_count += 1
    print(count_score())
    print(garbage_count)


challenge1()
