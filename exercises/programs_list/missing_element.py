from functools import reduce
from operator import ixor
def find_missing_element(input, n):
    res = reduce(lambda x, y: x ^y , range(1, n+1))
    #res = reduce(ixor, range(1, n+1))
    res_array = reduce(lambda x, y: x ^y , input)
    return res_array - res


print(find_missing_element([1,2,3,4], 5))


