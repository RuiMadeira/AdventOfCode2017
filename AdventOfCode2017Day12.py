FILENAME = './input/AdventOfCode2017Day12Input.txt'


def add_neighbours(name, programs, new_set, visited_names):
    visited_names.append(name)
    new_set.append(name)
    for neighbour in programs[name]:
        if neighbour not in visited_names:
            add_neighbours(neighbour, programs, new_set, visited_names)


def challenge1And2():
    programs = {}
    sets = []
    visited_names = []
    with open(FILENAME) as f:
        for line in f:
            line_split = line.split()[::-1]
            name = line_split.pop()
            line_split.pop()
            programs[name] = list(map(lambda x: x.replace(',', ''), line_split))
    for name in programs:
        if name not in visited_names:
            new_set = []
            sets.append(new_set)
            add_neighbours(name, programs, new_set, visited_names)
    for _set in sets:
        if "0" in _set:
            print('Len of the set containing 0: ' + str(len(_set)))
    print('Total number of sets: ' + str(len(sets)))


challenge1And2()
