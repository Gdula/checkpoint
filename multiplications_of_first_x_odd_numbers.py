def multiplications_of_first_x_odd_numbers(x, start = 0):
    if x <= 0:
        raise(ValueError)("Numbers count parameter must be grater than zero")
    else:
        i = 0
        result = 1
        list_of_odd = []
        while len(list_of_odd) < x:
            if i % 2 != 0:
                list_of_odd.append(i)
            i += 1
        for i in list_of_odd:
            result *= i
        return result
