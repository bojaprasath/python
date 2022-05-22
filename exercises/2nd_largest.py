def get_largest(data,n):
    data.sort()
    print(data[::-1][n-1])
    print(data[n - 1])



data = [2,3,4,23,5,56,7435,345]
get_largest(data,1)


def get_largest(data,n):
    if len(data) < n:
        print('data has less no of values')
        return False
    for i in range(len(data)):
        j = i + 1
        while j < len(data):
            if data[i] > data[j]:
                data[i],data[j] = data[j],data[i]
            elif data[i] == data[j]:
                del data[j]
            print(data[i],data[j])
            j = j + 1


    print(data)
    print(data[n-1])

data = [2,3,2,3,4,23,5,56,7435,345]
get_largest(data,1)