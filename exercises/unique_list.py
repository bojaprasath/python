 # support 2.3 as well as 2.4
try: set
except NameError:
    from sets import Set as set

def unique(s):

    try:
        return list(set(s))
    except TypeError:
        pass
    t = list(s)
    try:
        t.sort()
    except TypeError:
        del t  # Move on to the next method
    else:
     # the sort worked, so we're fine -- do the weeding
        pass
     #    return [x for i, x in enumerate(t) if not i or x != t[i-1]] # Brute force is all that's left
     #    out = []
     #    print('done')
     #    for i, x in enumerate(t):
     #        print(i, x)
     #        if not i or x != t[i - 1]:
     #            print(x)
     #            out.append(x)
    u = []
    for x in s:
        if x not in u:
            u.append(x)
    return u


print(unique([1,2,3,1,2,3]))
print(unique('abcabc'))
print(unique(([1, 2], [2, 3], [1, 2])))