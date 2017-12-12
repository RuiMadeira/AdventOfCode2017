FILENAME = './input/AdventOfCode2017Day1Input.txt'


def challenge1():
    final_sum = 0
    with open(FILENAME) as f:
        first_digit = int(f.read(1))
        digit = first_digit
        while True:
            digit_next = f.read(1)
            if not digit_next:
                print("End of file")
                break
            digit_next = int(digit_next)
            if digit == digit_next:
                print("Summing to final count:" + str(digit))
                final_sum += digit
            print("Read a character:", digit_next)
            digit = digit_next
        if digit == first_digit:
            final_sum += digit
    print(final_sum)


def challenge2():
    final_sum = 0
    numberList = []
    with open(FILENAME) as f:
        while True:
            c = f.read(1)
            if not c:
                print("End of file")
                break
            numberList.append(int(c))
    i = 0
    list_size = len(numberList)
    print("List Size:" + str(list_size))
    half_list_size = list_size // 2
    while i < list_size:
        if i <= (half_list_size - 1):
            if numberList[i] == numberList[i + half_list_size]:
                print("i is: " + str(i) + " Number is: " + str(numberList[i]) + " Pair position is: " + \
                    str(i + half_list_size) + " Pair Number is: " + str(numberList[i + half_list_size]))
                final_sum  += numberList[i]
        if i > (half_list_size - 1):
            if numberList[i] == numberList[i - half_list_size]:
                print("i is: " + str(i) + " Number is: " + str(numberList[i]) + " Pair position is: " + \
                        str(i - half_list_size) + " Pair Number is: " + str(numberList[i - half_list_size]))
                final_sum  += numberList[i]
        i += 1
    print(final_sum)


challenge2()
