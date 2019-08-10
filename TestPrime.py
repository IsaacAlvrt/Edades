#Test if a number is prime

n = int( input("number=") )

if n == 2:
    print("your number is prime")

for i in range(2,n):
    if n%i == 0:
        print("Your number is NOT prime :c")
        break
    else:
        print("your number is prime")
        break


"""Prime numbers:
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
167, 173, 179, 181, 191, 193, 197, 199  """
