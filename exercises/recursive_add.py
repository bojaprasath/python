
def add_numbers(in_list):
    if len(in_list) == 1:
        return in_list[0]
    else:
        return  in_list[0] + add_numbers(in_list[1:])



print(add_numbers([1,2,3,4,5,6]))



def add_numbers(in_list):
    if len(in_list) == 1:
        return in_list[0]
    else:
        return  in_list[0] + add_numbers(in_list[1:])

