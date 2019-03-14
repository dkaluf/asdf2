num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))
num5 = int(input("Enter number 5: "))
num6 = int(input("Enter number 6: "))
num7 = int(input("Enter number 7: "))
num8 = int(input("Enter number 8: "))
num9 = int(input("Enter number 9: "))      
num10 = int(input("Enter number 10: "))

while num1 < 0:
    num1 = int(input("Enter number 1: "))

while num1 > 1000:
    num1 = int(input("Enter number 1: "))
           
while num2 < 0:
    num2 = int(input("Enter number 2: "))

while num2 > 1000:
    num2 = int(input("Enter number 2: "))
           
while num3 < 0:
    num3 = int(input("Enter number 3: "))

while num3 > 1000:
    num3 = int(input("Enter number 3: "))
           
while num4 < 0:
    num4 = int(input("Enter number 4: "))

while num4 > 1000:
    num4 = int(input("Enter number 4: "))
           
while num5 < 0:
    num5 = int(input("Enter number 5: "))

while num5 > 1000:
    num5 = int(input("Enter number 5: "))
	
while num6 < 0:
    num6 = int(input("Enter number 6: "))

while num6 > 1000:
    num6 = int(input("Enter number 6: "))
           
while num7 < 0:
    num7 = int(input("Enter number 7: "))

while num7 > 1000:
    num7 = int(input("Enter number 7: "))
           
while num8 < 0:
    num8 = int(input("Enter number 8: "))

while num8 > 1000:
    num8 = int(input("Enter number 8: "))
           
while num9 < 0:
    num9 = int(input("Enter number 9: "))

while num9 > 1000:
    num9 = int(input("Enter number 9: "))
           
while num10 < 0:
    num5 = int(input("Enter number 10: "))

while num10 > 1000:
    num10 = int(input("Enter number 10: "))

max = num1

if num2 > max:
    max = num2

if num3 > max:
    max = num3

if num4 > max:
    max = num4

if num5 > max:
    max = num5
	
if num6 > max:
    max = num6
	
if num7 > max:
    max = num7
	
if num8 > max:
    max = num8
	
if num9 > max:
    max = num9
	
if num10 > max:
    max = num10


min = num1

if num2 < min:
    min = num2

if num3 < min:
    min = num3

if num4 < min:
    min = num4

if num5 < min:
    min = num5
	
if num6 < min:
    min = num6
	
if num7 < min:
    min = num7
	
if num8 < min:
    min = num8
	
if num9 < min:
    min = num9
	
if num10 < min:
    min = num10

def print_results():
	print("Maximum number is: ",max)
	print("Minimum number is: ",min)

print_results()
