def triplet_to_sum(input,total):
    input.sort()
    print(input)
    for i in range(len(input)-2):
        j = i + 1
        k = len(input) -1
        while(j < k):
            if total == input[i] + input[j] + input[k]:
                print('Triplet is {} {} {}'.format(input[i],input[j],input[k]))
                return True
            elif total > input[i] + input[j] + input[k]:
                j+=1
            else:
                k-=1
    return False

#https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/



input = [1, 4, 45, 6, 10, 8]
print(len(input))
print(triplet_to_sum(input, 22))
input = [0, -1, 2, -3, 1]
print(triplet_to_sum(input, 0))