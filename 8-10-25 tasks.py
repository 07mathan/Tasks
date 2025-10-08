#task1
num = int(input("Enter the number:"))
if  num % 2 ==0:
    print("number is even")
else:
    print("number is odd")

#task2
age = int(input("Check eligible for vote:"))
if age >= 18:
    print("Eligible for vote")
else:
    print("Not Eligible for vote")

# task 3
num = int(input("Enter a number:"))
if num % 3 == 0 and num % 5 == 0:
    print("fizz buzz")
elif num % 5 == 0:
    print("buzz")
elif num % 3 == 0:
    print("fizz")
else:
    print("not divisible")

