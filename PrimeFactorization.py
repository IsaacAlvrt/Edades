#Gets biggest prime number

n = int( input("n=") )
i = 2

print("Biggest prime factor:")

while i * i < n:
    while n%i == 0:
        n = n / i
    i = i + 1
