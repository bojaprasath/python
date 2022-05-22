def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            print(' L : %s'%L)
            print('R : %s'%R)
            print('arr : %s'%arr)
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        print('arr1 : %s'%arr)
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        print('arr1 : %s' % arr)
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        print('arr2 : %s' % arr)




# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11,13]
    print ("Given array is %s "%arr)
    mergeSort(arr)
    print("Sorted array is %s"%arr)

# This code is contributed by Mayank Khanna

