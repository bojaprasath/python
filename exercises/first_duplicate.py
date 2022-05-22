list = [1,2,3,4,5,1,2,3,4,5]
list = [2,1,3,5,4,3,2]
seen_list = []
for i in list:
    if i not in seen_list:
        seen_list.append(i)
    else:
        print(i)
        break