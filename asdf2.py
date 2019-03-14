num1 = int(input("Enter number 1: "))
while num1 < 0:
    num1 = int(input("Enter number 1: "))

while num1 > 1000:
    num1 = int(input("Enter number 1: "))
           
num2 = int(input("Enter number 2: "))
while num2 < 0:
    num2 = int(input("Enter number 2: "))

while num2 > 1000:
    num2 = int(input("Enter number 2: "))
           
num3 = int(input("Enter number 3: "))
while num3 < 0:
    num3 = int(input("Enter number 3: "))

while num3 > 1000:
    num3 = int(input("Enter number 3: "))
           
num4 = int(input("Enter number 4: "))
while num4 < 0:
    num4 = int(input("Enter number 4: "))

while num4 > 1000:
    num4 = int(input("Enter number 4: "))
           
num5 = int(input("Enter number 5: "))
while num5 < 0:
    num5 = int(input("Enter number 5: "))

while num5 > 1000:
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

print("The largest number is: ",max)

min = num1

if num2 < min:
    min = num2

if num3 < min:
    min = num3

if num4 < min:
    min = num4

if num5 < min:
    min = num5

print("The smallest number is: ",min)
