num1 = int(input("Enter number 1: "))
           
num2 = int(input("Enter number 2: "))
           
num3 = int(input("Enter number 3: "))
           
num4 = int(input("Enter number 4: "))
           
num5 = int(input("Enter number 5: "))

max = num1
if num2 > max:
    max = num2

if num3 > max:
    max = num3

if num4 > max:
    max = num4

if num5 > max:
    max = num5

print("Maximum number is: ",max)

min = num1
if num2 < min:
    min = num2

if num3 < min:
    min = num3

if num4 < min:
    min = num4

if num5 < min:
    min = num5

print("Minimum number is: ",min)
