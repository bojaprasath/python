def calculateScore(text, prefixString, suffixString):
    text1 = text
    prefix1 = prefixString
    suffix1 = suffixString
    prefix_match = ''
    suffix_match = ''
    # for i in range(1,len(text1)):
    #     for j in range(len(prefix1),1,-1):
    #         #print(i,j)
    #         print(text1[:i],prefix1[-i:])
    #         if text1[:i] == prefix1[-j:]:
    #             print('matching %s : %s'%(text1[:i],prefix1[-j:]))
    #             prefix_match = text1[:i]
    #             print(prefix_match)
    # #####PREFIX
    # print('SUFFIX')
    i = 0
    j = 0
    while i < len(text1):
            #print(i,j)
            print(text1[-i:],suffix1[:j])
            if text1[-i:] == suffix1[:j]:
                print('matching %s : %s'%(text1[-i:],suffix1[:j]))
                suffix_match = text1[-i:]
                print(suffix_match)
    # print('prefix match : %s'%prefix_match)
    # print('suffix match: %s'%suffix_match)
    # text_score = len(prefix_match) + len(suffix_match)
    # return  text_score



print(calculateScore('abracadabra','habrahabr','bracket'))
