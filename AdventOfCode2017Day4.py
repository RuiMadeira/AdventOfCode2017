FILENAME = './input/AdventOfCode2017Day4Input.txt'


def challenge1():
    final_count = 0
    with open(FILENAME) as f:
        for line in f:
            word_list = []
            valid = True
            line = line.split()
            for word in line:
                if word not in word_list:
                    word_list.append(word)
                else:
                    valid = False
                    break
            if valid:
                final_count += 1
    print(final_count)


def challenge2():
    final_count = 0
    with open(FILENAME) as f:
        for line in f:
            word_list_sets = []
            valid = True
            line = line.split()
            for word in line:
                char_set = list(word)
                char_set.sort()
                print("Char set: " + str(char_set))
                print("Word list sets: " + str(word_list_sets))
                if char_set not in word_list_sets:
                    word_list_sets.append(char_set)
                else:
                    valid = False
                    break
            if valid:
                final_count += 1
    print(final_count)


challenge2()
