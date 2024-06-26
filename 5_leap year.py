num = int(input('Enter a number: '))

if (num % 400 == 0):
    print(num, 'is a leap year')
elif (num % 100 == 0):
    print(num, 'is not a leap year')
elif (num % 4 == 0):
    print(num, 'is a leap year')
else:
    print(num, 'is not a leap year')
