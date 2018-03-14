def delete_even_elements_lower_than_x(numbers, x):
    if len(numbers) == 0:
        raise(ValueError)("Input list cannot be empty!")
    else:
        for i in numbers[:]:
            if i % 2 == 0 and i<x:
                numbers.remove(i)
        return numbers
