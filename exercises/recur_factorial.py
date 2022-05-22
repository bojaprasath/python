import sys
print(sys.getrecursionlimit())
def recur_factorial(n):
   """Recursive function to
   print Fibonacci sequence"""
   if n <= 1:
       return 1
   else:
       return(n * recur_factorial(n-1))

# Change this value for a different result
nterms = 10

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# # check if the number of terms is valid
# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
#    for i in range(nterms):
#        print(recur_factorial(i))
print(sys.getrecursionlimit())
print(sys.setrecursionlimit(20000))
print(recur_factorial(10000))