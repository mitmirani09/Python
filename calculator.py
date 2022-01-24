#calculator using functions and if else

# add two numbers
def add(num1, num2):
	return num1 + num2

# subtract two numbers
def subtract(num1, num2):
	return num1 - num2

#  multiply two numbers
def multiply(num1, num2):
	return num1 * num2

#  divide two numbers
def divide(num1, num2):
	return num1 / num2

print("Please choose operation to perform: \n" 
		"1. Add\n" 
		"2. Subtract\n" 
		"3. Multiply\n"
		"4. Divide\n")


# Take input from the user
choice = int(input("Your choice:"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if choice == 1:
	print(number_1, "+", number_2, "=",add(number_1, number_2))

elif choice == 2:
	print(number_1, "-", number_2, "=",subtract(number_1, number_2))

elif choice == 3:
	print(number_1, "*", number_2, "=",multiply(number_1, number_2))

elif choice == 4:
	print(number_1, "/", number_2, "=",divide(number_1, number_2))
else:
	print("Invalid choice")
