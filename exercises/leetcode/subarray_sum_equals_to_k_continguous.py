#Kadanes

def get_sub_array(input):
    max_so_far = input[0]
    current_sum = 0
    start = 0
    current_ptr = 0
    for i,num in enumerate(input):
        current_sum = current_sum + num
        print(current_sum)
        if max_so_far < current_sum:
            max_so_far = current_sum
            print('Current Ptr : {}'.format(i))
        if num > 0:
            end = i
        if current_sum < 0:
            current_sum = 0
            start = i

    print('MAX UM : {}, start : {} end : {}'.format(max_so_far,start+1,end))
    print('Sub array : {}'.format(input[start+1:end+1]))


get_sub_array([-2,-3,4,-1,-2,1,5,-3])
get_sub_array([-2,-1,-3,4,-1,2,5,-4,9])
get_sub_array([-2,-2,4,-1,-2,1,5,-3])