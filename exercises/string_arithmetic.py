import re

source = '3*4+5'
number_or_symbol = re.compile('(\d+|[^ 0-9])')
print(re.findall(number_or_symbol, source))
list = re.findall(number_or_symbol, source)
check = True
while check == True:
    while list.count('*') != 0:
        j = list.index('*')
        val = int(list[j-1]) * int(list[j+1])
        print(val)
        if j != 1:
            list = list[:j-1]
            # list.extend(list[j+1:])
        print(list)