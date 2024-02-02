input1 = float(input("Please enter the first float number:\n"))
input2 = float(input("Please enter the second float number:\n"))

float_sum = input1 + input2

print(f"The sum of the previous floats is: {float_sum}\n")
print(f"The data type is {type(float_sum).__name__}\n")

input3 = int(input("Please enter the first integer number:\n"))
input4 = int(input("Please enter the second intger number:\n"))

diff = input3-input4


print(f"The difference of the previous integers is: {diff}\n")
print(f"The data type is {type(diff).__name__}\n")

input5 = float(input("Please enter the last float number:\n"))
input6 = int(input("Please enter the last integer number:\n"))

product = input5 * input6

print(f"The product of the previous numbers is: {product}\n")
print(f"The data type is {type(product).__name__}\n")