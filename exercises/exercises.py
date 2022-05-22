# a = 5
# print(a)
# a = ('abcd', 786, 2.23, 'john', 70.2)
# print(a)
# print(a[0])
# a = [ 1,2,34,5,5,6,7,88,7,8,99,2,3,4,34,5,55,67,8,7,8,88,5]
# for i in a:
#     print('%d count : %d'%(i,a.count(i)))
#     while a.count(i) != 1:
#         del a[a.index(i)]
#
#
# t = [1,2,3,4,1,2,3,4]
# t = 'abcabc'
# out = []
# for i, x in enumerate(t):
#     print(i,x)
#     # if not i or x != t[i - 1]:
#     #     print(x)
#     #     out.append(x)
#     if not i:
#         print('done')
#         print(i)

# print(a)
# print(a.count(5))

# p = (4, 5)
# x, y = p
# print(x)
# print(y)
# import heapq
# nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# heap = list(nums)
# nums.append(50)
# print(heap)
# print(nums)
# heapq.heapify(heap)
# print(heap)
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
# print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
# print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]

# mat = [[0, 0, 0, 1],
#        [0, 1, 1, 1],
#        [1, 1, 1, 1],
#        [0, 0, 0, 0]]
# return_list = 0
# for i in mat:
#     if i.count(1) > return_list:
#         return_value = i
#         return_list = i.count(1)
#         return_index = mat.index(i)
# print(return_value)
# print(return_index)

# Python3 program to find the row
# with maximum number of 1s

# Function to find the index
# of first index of 1 in a
# boolean array arr[]
# def first(arr, low, high):
#     if high >= low:
#
#         # Get the middle index
#         mid = low + (high - low) // 2
#
#         # Check if the element at
#         # middle index is first 1
#         if (mid == 0 or arr[mid - 1] == 0) and arr[mid] == 1:
#             return mid
#
#             # If the element is 0,
#         # recur for right side
#         elif arr[mid] == 0:
#             return first(arr, (mid + 1), high)
#
#             # If element is not first 1,
#         # recur for left side
#         else:
#             return first(arr, low, (mid - 1))
#     return -1
#
#
# # Function that returns
# # index of row with maximum
# # number of 1s.
# def rowWithMax1s(mat):
#     # Initialize max values
#     R = len(mat)
#     C = len(mat[0])
#     max_row_index = 0
#     max = -1
#
#     # Traverse for each row and
#     # count number of 1s by finding
#     #  the index of first 1
#     for i in range(0, R):
#         index = first(mat[i], 0, C - 1)
#         if index != -1 and C - index > max:
#             max = C - index
#             max_row_index = i
#
#     return max_row_index
#
#
# # Driver Code
# mat = [[0, 0, 0, 1],
#        [0, 1, 1, 1],
#        [1, 1, 1,
#         1],
#        [0, 0, 0, 0]]
# print ("Index of row with maximum 1s is",
#        rowWithMax1s(mat))
#
# # This code is contributed
# # by shreyanshi_arun
#
#
#


# def pascal(h,nums=[[1]]):
#     if h == 1:
#         return  nums
#     new_list = [1]
#     for i in range(len(nums[-1])-1):
#         new_list.append(nums[-1][i] + nums[-1][i+1])
#     new_list.append(1)
#     nums.append(new_list)
#     return pascal(h-1,nums)
#
# print(pascal(3))
#
# a = [12,3,4]
# b  = a
# print(id(a))
# print(id(b))
# b.append(5)
# print(id(a))
# print(id(b))
# del a
# print(id(a))
# print(id(b))

# a = 1
# b = a
# a = 5
#
# print(id(a))
# print(id(b))
# # b.append(5)
# del a
#
# print(id(b))
# try:
#     print(id(a))
#     print(a)
# except:
#     pass
#
# print(b)



for i in range(3,100):
    flag = True
    for j in range(2,i):
        # print(i,j,i%j)
        if i%j == 0:
            flag = False
    if flag:
        print('Prime : %d'%i)

