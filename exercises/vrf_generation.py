for x in range(2,301):
    print('ip vrf vrf_{}'.format(x))
    print('rd 50000:{}'.format(x))
    print('route-target export 50000:{}'.format(x))
    print('route-target import 50000:{}'.format(x))