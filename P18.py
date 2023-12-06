# 2. Write a program to find whether an inputted number is perfect or not

def is_perfect_number(number):
    divisors = [i for i in range(1, number+1) if number % i == 0]
    return sum(divisors) == number

num = int(input("Enter a number: "))

if is_perfect_number(num):
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")
