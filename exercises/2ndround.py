# # Input : fabbcdaeacf
# # Output: fabcde
# #
# # Tasks:
# #
# # 1) Identify the pattern between input and output
# # 2) Write a program to convert similar inputs into the appropriate output
#
#
# def pattern_find(input):
#     if len(input) == 0:
#         print('Please input non empty string')
#         return
#     output = ''
#     for i in input:
#         if i not in output:
#             output = output + i
#     return output
#
#
# print(pattern_find('fabbcdaeacf'))
#
# def pattern_find(input):
#
#
#     if len(input) == 0:
#         print('Please input non empty string')
#         return
#     output =set()
#     for i in input:
#         if i not in output:
#             output.add(i)
#     return output
#
#
# input = 'fabbcdaeacf'
# #output = ' fabcde'
# output = ''
# s = set(input)
# for i in input:
#     if i in s:
#         s.discard(i)
#     output = output + i
# print(output)
#
# # print(pattern_find('fabbcdaeacf'))
#
#
# input = 'fabbcdaeacf'
# #output = ' fabcde'
# output = ''
# llist = []
# for i in input:
#     if i not in llist:
#         llist.append(i)
#         output = output + i
# print(output)
#
# def remove_list(input,str,index):
#     new_list = []
#     n = 0
#     new_index = -1
#     for i in input:
#         new_index = new_index + 1
#         if i == str:
#             n = n + 1
#             print(n,index)
#             if n == index:
#                 del input[new_index]
#                 print(input)
#     print(input)
#
# input = ["can", "you",  "can", "a", "can", "?"]
# remove_list(input,'can',3)
#
#
# def RemoveIthWord(list, word, N):
#     count = 0
#
#     for i in range(0, len(list)):
#         if (list[i] == word):
#             count = count + 1
#
#             if (count == N):
#                 del (list[i])
#                 return True
#
#     return False
#
#
# # Driver code
# list = ['geeks', 'for', 'geeks']
# word = 'geeks'
# N = 2
#
# flag = RemoveIthWord(list, word, N)
#
# if (flag == True):
#     print("Updated list is: ", list)
# else:
#     print("Item not Updated")
#
# str = "geeksforgeeks"
# str = "geekspractice"
#
# def generate_output(str):
#     str1 = ''
#     str2 = ''
#     for i in str:
#         if str.count(i) > 1:
#             if i not in str2:
#                 str2 = str2 + i
#         else:
#             if i not in str1:
#                 str1 = str1 + i
#     print(str1)
#     print(str2)
#
# generate_output(str)
#
#
# #Longest Common Substring
# # Input :  X = "GeeksforGeeks",
# #          Y = "GeeksQuiz"
# # Output : Geeks
# #
# # Input : X = "zxabcdezy",
# #         Y = "yzabcdezx"
# # Output : abcdez
#
# def generate_longest(str1,str2):
#     n = len(str1)
#     longest = ''
#     for i in range(0,len(str1)):
#         for j in range(i,n):
#             print(str1[i:j])
#             if str1[i:j] in str2:
#                 if len(str1[i:j]) > len(longest):
#                     longest = str1[i:j]
#     print(longest)
#
#
#
# str1 = 'zxabcdezy'
# str2 = 'yzabcdezx'
# generate_longest(str1,str2)
#
#
# Input : "John is the son of John second.
#          Second son of John second is William second."
# Output : [('second', 4), ('John', 3), ('son', 2), ('is', 2)]
#
# Explanation :
# 1. The string will converted into list like this :
#     ['John', 'is', 'the', 'son', 'of', 'John',
#      'second', 'Second', 'son', 'of', 'John',
#      'second', 'is', 'William', 'second']
# 2. Now 'most_common(4)' will return four most
#    frequent words and its count in tuple.
#
#
# Input : "geeks for geeks is for geeks. By geeks
#          and for the geeks."
# Output : [('geeks', 5), ('for', 3)]
#
# Explanation :
# most_common(2) will return two most frequent words and their count.
#
# Recommended:


out_port = [21,22,23,24]
vlan_list = [100,200,300,400]
for port,vlan in zip(out_port,vlan_list):
    print(port)
    print(vlan)

