import array
data1 = array.array('i',range(10**6))
data2 = list(range(10**6))
import sys
print(sys.getsizeof(data1))
print(sys.getsizeof(data2))
