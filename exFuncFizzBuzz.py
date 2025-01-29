def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
        quit
    elif num % 3 == 0:
        print("Fizz")
        quit
    elif num % 5 == 0:
        print("Buzz")
        quit
    else:
        print(num)
