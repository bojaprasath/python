# Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52)
# Type 'copyright', 'credits' or 'license' for more information
# IPython 7.8.0 -- An enhanced Interactive Python. Type '?' for help.
# PyDev console: using IPython 7.8.0
# Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52)
# [Clang 6.0 (clang-600.0.57)] on darwin
# l1 = [ x *x for x in range(0,5)]
# l1
# Out[3]: [0, 1, 4, 9, 16]
# l2 = iter([x *x for x in range(0,5)])
# l1.__sizeof__()
# Out[5]: 104
# l2.__sizeof__()
# Out[6]: 32
#
# l2 = iter([x *x for x in range(0,5)])

with open('iterator.txt','w') as f:
    f.writelines([str(x) + '\n' for x in range(0,100000)])

with open('iterator.txt','r') as f:
    output = f.readlines()
    print(output.__sizeof__())
    # print(output)

with open('iterator.txt','r') as f:
    output = iter(f.readlines())
    print(output.__sizeof__())
    # print(output)
