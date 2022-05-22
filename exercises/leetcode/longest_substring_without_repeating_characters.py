## If not in dict
    # 1 . Add it to dict
    # 2 . Increase max len
## Else
    # Calculate newlen from i - dict[char]
    # check if newlen > maxlen
        # max len = currlen



def longest_substring(input):
    dict = {}
    start = 0
    maxlen = 0
    currlen = 0
    end = 0
    newstart = 0
    for i,char in enumerate(input):
        if char not in dict:
            dict[char] = i
            currlen = currlen + 1

        else:
            if maxlen < currlen:
                maxlen = currlen
                end = i - 1
                # print(end)
                newstart = dict[char] + 1
                currlen = i - dict[char]
                # print(newstart)
                # print(currlen)
            dict[char] = i

    if currlen > maxlen:
        start = newstart
        end = i
    # print('length')
    # print(currlen)
    # print(maxlen)
    if currlen == maxlen:
        print(input[start:end+1])
        print(input[newstart:i + 1])
    print(input[start:end+1])

longest_substring('abcdefbmnopqrstu')
longest_substring('abcdefbm')
longest_substring('abcdefcfab')