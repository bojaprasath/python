import random
def ipv4_generator():
    return '.'.join(str(random.randint(0,255)) for _ in range(0,4))


print(ipv4_generator())


def ipv6_generator():
    return '.'.join(str(random.randint(0,255)) for _ in range(0,4))


print(ipv6_generator())