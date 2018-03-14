def get_common_elements(first, second, number):


    digits = []
    if len(first) == 0 or len(second) == 0:
        raise(ValueError)("Input list cannot be empty")

    else:
        for i in first:
            if i in second and i < number:
                digits.append(i)
                
        return digits
