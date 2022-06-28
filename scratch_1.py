

a=int(input('Enter a number: '))

def numbers(a):

    for num in range(a):

        if num % 15 == 0:
            print("FizzBUzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
   
print(numbers(a))
