def calculate_average(numbers):
    if not numbers:
        return 0
    if all(isinstance(num, (int, float)) for num in numbers):
        total = sum(numbers)
        average = total / len(numbers)
        return average
    else:
        return "Error: List contains non-numeric elements."

#Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = [10, 20, 0, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = [10, 20, 'a', 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")
