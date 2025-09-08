user_input = input("Enter a sequence of comma-separated numbers (e.g., 3, 5, 7, 23): ")
numbers_as_strings = [num.strip() for num in user_input.split(',')]
numbers_as_integers = [int(num) for num in numbers_as_strings]
number_list = numbers_as_integers
number_tuple = tuple(numbers_as_integers)
print("Generated List:", number_list)
print("Generated Tuple:", number_tuple)