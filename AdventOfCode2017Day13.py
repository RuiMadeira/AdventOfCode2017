import copy

FILENAME = './input/AdventOfCode2017Day13Input.txt'


def advance_layers(layers, last_layer):
    for layer in range(0, last_layer + 1):
        if layer in layers:
            if layers[layer]['state'] == 'asc':
                if layers[layer]['pointer'] == layers[layer]['depth'] - 1:
                    layers[layer]['pointer'] = layers[layer]['pointer'] - 1
                    layers[layer]['state'] = 'desc'
                else:
                    layers[layer]['pointer'] = layers[layer]['pointer'] + 1
            else:
                if layers[layer]['pointer'] == 0:
                    layers[layer]['pointer'] = layers[layer]['pointer'] + 1
                    layers[layer]['state'] = 'asc'
                else:
                    layers[layer]['pointer'] = layers[layer]['pointer'] - 1


# My original algorithm was not fast enough for doing all possible combinations until we are not caught. So browsing
# through Reddit I found out that there is an equation to calculate the current position of a scanner and the
# is not so difficult to arrive to it, so I did my own version of this just for the delay part.
def delay_layers(layers, delay):
    if delay == 0:
        return
    for layer in layers:
        #print('layer: ' + str(layer))
        #print('delay: ' + str(delay))
        times_cycle = delay // ((layers[layer]['depth']-1) * 2)
        #print('times cycle: ' + str(times_cycle))
        middle = (layers[layer]['depth']-1) + (((layers[layer]['depth']-1)*2) * times_cycle)
        #print('middle: ' + str(middle))
        if delay > middle:
            layers[layer]['pointer'] = (layers[layer]['depth']-1) - (delay - middle)
            layers[layer]['state'] = 'desc'
        else:
            layers[layer]['pointer'] = (layers[layer]['depth']-1) - (middle - delay)
            layers[layer]['state'] = 'asc'
        #print('pointer result: ' + str(layers[layer]['pointer']))


# Same commentary: function to calculate position since the onds used in challenge one are not optimised
def calc_pos(delay, position, layer):
    final_moment = delay + position
    depth = layer['depth']
    times_cycle = final_moment // ((depth - 1) * 2)
    middle = (depth - 1) + (((depth - 1) * 2) * times_cycle)
    if final_moment > middle:
        return (depth - 1) - (final_moment - middle)
    else:
        return (depth - 1) - (middle - final_moment)


def challenge1():
    layers = {}
    last_layer = 0
    with open(FILENAME) as f:
        for line in f:
            line_split = line.split(':')
            layers[int(line_split[0])] = {'pointer': 0, 'depth': int(line_split[1]), 'state': 'asc'}
            last_layer = int(line_split[0])
    severity = 0
    for layer in range(0, last_layer + 1):
        if layer in layers.keys():
            if layers[layer]['pointer'] == 0:
                severity += (layer * layers[layer]['depth'])
        advance_layers(layers, last_layer)
    print('Severity of trip: ' + str(severity))


def challenge2():
    layers_init = {}
    last_layer = 0
    with open(FILENAME) as f:
        for line in f:
            line_split = line.split(':')
            layers_init[int(line_split[0])] = {'pointer': 0, 'depth': int(line_split[1]), 'state': 'asc'}
            last_layer = int(line_split[0])
    for possibility in range(0, last_layer * 10000000):
        caught = False
        layers = copy.deepcopy(layers_init)
        delay_layers(layers, possibility)
        #print(layers)
        print(possibility)
        position = 0
        for layer in range(0, last_layer + 1):
            if layer in layers.keys():
                #if layers[layer]['pointer'] == 0:
                if calc_pos(possibility, position, layers[layer]) == 0:
                    caught = True
                    break
            position += 1
            #advance_layers(layers, last_layer)
        if not caught:
            print('Not getting caught by delaying: ' + str(possibility))
            break


challenge2()
