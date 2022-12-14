#addition
def add(num1, num2):
	return num1 + num2

def subtract(num1, num2):
    return num1 - num2
 
def multiply(num1, num2):
    return num1 * num2
 
def divide(num1, num2):
    return num1 / num2

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

encoded_operation = int(input("Select operation from 1, 2, 3, 4:"))

num1=int(input("Enter First number"))
num2=int(input("Enter second number"))

if encoded_operation ==1:
	print(f'{num1} + {num2} = {add(num1, num2)}')

elif encoded_operation ==2:
	print(f'{num1} + {num2} = {subtract(num1, num2)}')

elif encoded_operation ==3:
	print(f'{num1} + {num2} = {multiply(num1, num2)}')

elif encoded_operation ==4:
	print(f'{num1} + {num2} = {divide(num1, num2)}')

else:
	print('Invalid input')