def find_largest(numbers):
    if not numbers:
        return None 
    largest = numbers[0] 
    for number in numbers:
        if number > largest:
            largest = number
    return largest