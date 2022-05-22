def recur_fibo(n):
   """Recursive function to
   print Fibonacci sequence"""
   if n <= 2:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

# # Change this value for a different result
# nterms = 9
#
#
#
# # uncomment to take input from the user
# #nterms = int(input("How many terms? "))
#
# # check if the number of terms is valid
# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
#    for i in range(nterms):
#        print(recur_fibo(i))

print(recur_fibo(10))
print('done')


# Function for nth Fibonacci number
def Fibonacci(n):

	# Check if input is 0 then it will
	# print incorrect input
	if n < 0:
		print("Incorrect input")

	# Check if n is 0
	# then it will return 0
	elif n == 0:
		return 0

	# Check if n is 1,2
	# it will return 1
	elif n == 1 or n == 2:
		return 1

	else:
		return Fibonacci(n-1) + Fibonacci(n-2)

# Driver Program
print(Fibonacci(10))

# This code is contributed by Saket Modi
# then corrected and improved by Himanshu Kanojiya

# Function for nth fibonacci
# number - Space Optimisataion
# Taking 1st two fibonacci numbers as 0 and 1

def fibonacci(n):
    a = 0
    b = 1

    # Check is n is less
    # than 0
    if n < 0:
        print("Incorrect input")

    # Check is n is equal
    # to 0
    elif n == 0:
        return 0

    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b


# Driver Program
print(fibonacci(50))

# This code is contributed by Saket Modi
# Then corrected and improved by Himanshu Kanojiya
