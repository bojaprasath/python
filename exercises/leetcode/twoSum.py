
def twoSum(input, target):
    sum = 0
    i = 0
    j = i + 1
    while i <= len(input) -2 and \
        j <= len(input) -1:
        print(i, j)
        sum = input[i] + input[j]
        if sum != target:
            if j == len(input)-1:
                i = i + 1
                j = i + 1
            else:
                j = j + 1
        else:
            return i,j
    return None

# print(twoSum([2,7,11,15,34,6,1,3,5], 4))


def twoSum(input, target):
    dict_seen = {}
    for i,num in enumerate(input):
        if target-num in dict_seen:
            print(dict_seen[target-num],i)
            return dict_seen[target-num],i
        else:
            dict_seen[num] = i
    return None

print(twoSum([2,7,11,15,34,6,1,3,5], 35))

# Given
# an
# array
# of
# integers
# nums and an
# integer
# target,
# return indices
# of
# the
# two
# numbers
# such
# that
# they
# add
# up
# to
# target.
#
# You
# may
# assume
# that
# each
# input
# would
# have
# exactly
# one
# solution, and you
# may
# not use
# the
# same
# element
# twice.
#
# You
# can
# return the
# answer in any
# order.
#
# Example
# 1:
#
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Output: Because
# nums[0] + nums[1] == 9, we
# return [0, 1].
# Example
# 2:
#
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
# Example
# 3:
#
# Input: nums = [3, 3], target = 6
# Output: [0, 1]
# https://www.youtube.com/watch?v=xZFoZvhnVTU