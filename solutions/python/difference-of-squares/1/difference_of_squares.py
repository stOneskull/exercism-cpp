def square_of_sum(count):
    the_sum = sum(range(1, count + 1))
    return the_sum * the_sum


def sum_of_squares(count):
    return sum(num * num for num in range(1, count + 1))


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)