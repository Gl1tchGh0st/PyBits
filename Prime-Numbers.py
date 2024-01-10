# Printing prime numbers in a range
print("-- Output all prime numbers in a range --")
lower = input("Enter the lower number: ")
int(lower)
upper = input("Enter the higher number: ")
int(upper)
for num in range(lower, upper+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num) # Prime number
