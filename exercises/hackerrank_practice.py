def compare(l1, l2):
    t1 = l1[:]
    t2 = l2[:]
    # print(t1,t2)
    for ele in l1:
        try:
            t2.remove(ele)
        except:
            return False
    # if len(t2) == 0:
    #     for ele in l2:
    #         try:
    #             if t1.remove(ele):
    #                 continue
    #         except:
    #             return False
    if len(t2) == 0:
        return True
    return False

l = []
s = 'abba'
for i in range(len(s)):
    for j in range(len(s) + 1):
        if s[i:j] is not '':
            l.append(s[i:j])
count = 0
for i in range(len(l)):
    for j in range(len(l)):
        if i != j and len(l[i]) == len(l[j]):
            if (compare(list(l[i][:]), list(l[j][:]))):
                print(list(l[i][:]), list(l[j][:]))
                count = count + 1
anagrams = count/2
print(int(anagrams))