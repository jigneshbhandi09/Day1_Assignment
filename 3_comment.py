num = int(input('Enter a number: ')) #take a number from user

if (num % 400 == 0):
    # If the number is divisible by 400, it is a leap year
    print(num, 'is a leap year')
elif (num % 100 == 0):
    # If the number is divisible by 100 but not by 400, it is not a leap year
    print(num, 'is not a leap year')
elif (num % 4 == 0):
    # If the number is divisible by 4 but not by 100, it is a leap year
    print(num, 'is a leap year')
else:
    print(num, 'is not a leap year')

