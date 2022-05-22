def anagram(s,t):
    if len(s) != len(t):
        return False
    dicts = {}
    dictt = {}
    for i in range(len(s)):
        dicts[s[i]] = 1 + dicts.get(s[i],
                                    0)
        dictt[t[i]] = 1 + dictt.get(t[i], 0)
        # print('dict : {}'.format(dictt))
        # print(dicts)
    # for c in dicts:
    #     if dicts[c] != dictt.get(c,0):
    #         return False
    if dicts != dictt:
        return False

    return True
print(anagram('caar','raca'))
print(anagram('car','bed'))