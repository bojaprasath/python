a = 'aaaabbbddddcddddaaabbaa'
alist = list(a[0])
# alist = []
ret_value = ''
count = 0
for i in a:
    if i in alist:
        alist.append(i)
    else:
        ret_value = ret_value + str(len(alist)) + str(alist[-1])
        alist = [i]
    count = count + 1
    if count == len(a):
        # ret_value = ret_value + '1' + str(i)
        ret_value = ret_value + str(len(alist)) + str(i)
print(alist)
print(ret_value)



