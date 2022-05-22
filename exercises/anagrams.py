def anagrams(str1,str2):
    already_checked = []
    if len(str1) != len(str2):
        print('They are not anagrams')
        return
    str1 = list(str1)
    str2 = list(str2)
    for i in str1:
        if i not in already_checked:
            if str1.count(i) != str2.count(i):
                print('They are not anagrams')
                return
            else:
                already_checked.append(i)
    print('They are anagrams')

anagrams('below','elbow')


dict = {'a': 1}
for i,j in dict.items():
    print(i,j)
    locals()[i] = j
print(a)




