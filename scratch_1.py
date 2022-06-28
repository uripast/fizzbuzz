'''
Write a program or script that prints out the numbers between 1 and MAX_NUMBER.

 (MAX_NUMBER=100 being default)

* For each number that is divisible by three, “Fizz” is printed.
* For each number that is divisible by five, “Buzz” is printed.
* For each number that is divisible by both three and five, “FizzBuzz” is printed.
* Else, the number is printed as is.

For example, a typical output for this would start as follows:

```bash
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, PyBuzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, FizzBuzz, 31, 32, Fizz, 34, Buzz, Fizz, …
```
'''

maxn=int(input('Enter a number: '))

def numbers(maxn):

    for num in range(maxn):

        if num % 15 == 0:
            print("FizzBUzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
    #return num


print(numbers(maxn))
