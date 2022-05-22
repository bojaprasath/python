# https://www.youtube.com/watch?v=y-XRBLFVNm8
# https://www.codespeedy.com/find-kth-smallest-largest-element-in-unsorted-array-in-python/
# https://blog.finxter.com/find-the-k-th-largest-element-in-an-unsorted-array/
# https://www.youtube.com/watch?v=bkOpz2R4ZrM

def find_kth_largest(input, k):
    window = input[:k]
    window.sort()
    print(window)
    for i in range(k,len(input)):
        j = 0
        print(i)
        checkWindow = True
        while checkWindow:
            print(window[j],input[i])
            if window[j] < input[i]:
                window[j] = input[i]
                window.sort()
                j = j + 1
                print(window)
            checkWindow = False



    print(window)



def find_kth_largest_no_dups(input, k):
    window = input[:k]
    window.sort()
    print(window)
    for i in range(k,len(input)):
        j = 0
        # print(i)
        checkWindow = True
        checked = False
        while checkWindow:
            print('Comparing')
            print(window[j],input[i])
            if window[j] < input[i]:
                # window[j] = input[i]
                # window.sort()
                if j == k-1:
                    print(j)
                    print(window)
                    window = window[1:j+1]
                    print('#########')
                    print(window)
                    window.append(input[i])
                    print('added')
                    print(window)
                    checkWindow = False
                checked = True
                j = j + 1
            elif window[j] == input[i]:
                checkWindow = False
            else:
                if checked:
                    window[j-1] = input[i]
                checkWindow = False


find_kth_largest([5,1,3,8,8,7,9,2],3)

find_kth_largest_no_dups([5,1,3,8,8,7,9,2],3)