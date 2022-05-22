
def first_norepeat(input):
    min_index = input.__len__()
    dict = {}
    for i in input:
        if i in dict:
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    for i in dict:
        print(i)
        if dict[i] == 1:
            min_index = input.index(i)
            print(min_index)
            return

    print('All characters are repeated')

input = 'abcxabcd'
first_norepeat(input)