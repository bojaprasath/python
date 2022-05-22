s = set('asdasasdaeujbcvbghjc')
order_list = [x for x in range(97,122)]
for i,element in enumerate(s):
    print(element,ord(element))
    order_list.remove(ord(element))
print(order_list)
print(order_list.__len__() == 0)
