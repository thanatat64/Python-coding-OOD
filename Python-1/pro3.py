print(" "+ "*** Summation of each digit ***")
num = int(input("Enter a positive number : "))
sum = 0
if num < 10**30:
    while num > 0:
        sum += num % 10
        num //= 10
print("Summation of each digit =  " + str(sum))