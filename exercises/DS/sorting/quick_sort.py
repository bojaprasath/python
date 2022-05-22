# Quick sort in Python

# function to find the partition position
def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[low]

    # pointer for greater element
    left = low
    right = high

    # traverse through all elements
    # compare each element with pivot
    print(low)
    print(high)
    print(left)
    print(right)
    print('######')
    while left < right:

        # left <= right should come first . Otherwise it will fail
        while left < len(array) and array[left] <= pivot:
            print('pivot :{}'.format(pivot))
            # while left <= right:
            print('pivot :{}'.format(pivot))
            print('left value :{}'.format(array[left]))
            print('right value :{}'.format(array[right]))
            print('left index :{}'.format(left))
            print('right index :{}'.format(right))
            print('arr : {}'.format(array))
            left = left + 1
        while array[right] >= pivot:
            print('pivot :{}'.format(pivot))
            # while left <= right:
            print('pivot :{}'.format(pivot))
            print('left value :{}'.format(array[left]))
            print('right value :{}'.format(array[right]))
            print('left index :{}'.format(left))
            print('right index :{}'.format(right))
            print('arr : {}'.format(array))
            right = right - 1
        if left < right:
            print('arr before swap : {}'.format(array))
            array[left], array[right] = array[right], array[left]
            print('arr swapped : {}'.format(array))
    array[low], array[right] = array[right], array[low]
    return right



# function to perform quicksort
def quickSort(array, low, high):
    if low < high:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        splitpoint = partition(array, low, high)

        # recursive call on the left of pivot
        quickSort(array, low, splitpoint - 1)

        # recursive call on the right of pivot
        quickSort(array, splitpoint + 1, high)


data = [24,7,6,2,3,6,79,0,1,34,56,23,87,23]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)



#last index as pivot https://www.tutorialspoint.com/data_structures_algorithms/quick_sort_algorithm.htm