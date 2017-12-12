FILENAME = './input/AdventOfCode2017Day2Input.txt'


def challenge1():
    final_sum = 0
    with open(FILENAME) as f:
        for line in f:
            line = line.split()
            min_e = int(line[0])
            max_e = int(line[0])
            for e in line:
                e_str = int(e)
                if e_str < min_e:
                    min_e = e_str
                if e_str > max_e:
                    max_e = e_str
            final_sum += (max_e - min_e)
    print(final_sum)


def challenge2():
    final_sum = 0
    with open(FILENAME) as f:
        for line in f:
            line = line.split()
            n1 = 0
            n2 = 0
            for e in line:
                for c in line:
                    e_int = int(e) 
                    c_int = int(c)
                    if  (e_int != c_int) and (e_int % c_int == 0):
                        n2 = e_int
                        n1 = c_int
                        break
            final_sum += (n2 / n1)
    print(final_sum)


challenge2()
