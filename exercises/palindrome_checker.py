# a = 'raddara'
# print(len(a)%2)
# if len(a) % 2 == 0:
#     list1 = list(a)[:int(len(a)/2)]
#     list2 = list(a)[int(len(a)/2):][::-1]
# else:
#     list1 = list(a)[:int(len(a) / 2)]
#     list2 = list(a)[int(len(a) / 2)+1:][::-1]
# print(list1)
# print(list2)
# #
# if list1 == list2:
#     print('palindrom')
# else:
#     print('no palindrome')
#
#
# a = 'raddara'
# print(reversed(a))


def isPlaindrome(string):
    # code here
    mid = len(string) // 2
    print(mid)
    i = 0
    j = len(string) -1
    while i < mid and j >= mid:
        print('i : {}'.format(i))
        print('j : {}'.format(j))
        print('i value : {}'.format(string[i]))
        print('j value : {}'.format(string[j]))
        if string[i] == string[j]:
            i = i + 1
            j = j - 1
        else:
            return 0
    return 1

#print(isPlaindrome('abaaaxaaba'))


def isPlaindrome(string):
    # code here
    start = 0
    end = len(string) -1
    while end - start > 0:
        if string[start] == string[end]:
            start+=1
            end-=1
        else:
            return False
    return True

# print(isPlaindrome('abaaaxaaba'))
# print(isPlaindrome('ababa'))
# print(isPlaindrome('abba'))
# print(isPlaindrome('abca'))


def isPlaindrome(num):
    # code here
    revNum = 0
    while num != 0:
        revNum = revNum * 10 + (num % 10)
        num = num // 10
    print(revNum)
    print(num)
    return num == revNum

print(isPlaindrome(121))
# print(isPlaindrome(12))
# print(isPlaindrome(21))
# print(isPlaindrome(12121))