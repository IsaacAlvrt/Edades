#fibonacci

def fib(n):
    x = 0
    y = 1
    #Opcion 1
    for i in range(1,n+1):
        print(x)
        z = x + y
        x = y
        y = z
    #Opcion 2
    """
    while x < n:
        print(x)
        z = x + y
        x = y
        y = z """

#result
fib(10)
