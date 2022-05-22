# n=5
# for i in range(n):
#     out = ''
#     for j in range(i):
#         out = out + str('*')
#     print(out)

n=5
def triangle(num):
    # out = ''
    if num > 0:
        print(num)
        triangle(num-1)
        print(num)
        print('#'*num)

print(triangle(5))