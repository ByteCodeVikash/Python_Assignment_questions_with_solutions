#8. Write a python program to multiply all the numbers in a list.

def multiply_list(input_list):
    result = 1
    for num in input_list:
        result *= num
    return result

# Example usage
my_list = [1, 2, 3, 4]
result = multiply_list(my_list)
print("Result of multiplying all numbers in the list:", result)

    
    