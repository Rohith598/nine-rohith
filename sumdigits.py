def sum_digits(n):
    return sum(int(digit) for digit in str(abs(n)))
print(sum_digits(123456))
