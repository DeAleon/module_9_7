def is_prime(func):
    def wrapper(*args, **kwargs):
        number = func(*args, **kwargs)
        for i in range(2, number):
            if number % i == 0 and number != i:
                print('Составное')
                return number
            else:
                print('Простое')
                return number

    return wrapper


@is_prime
def sum_three(*number):
    sum_number = sum(number)
    return sum_number


result = sum_three(2, 3, 6)
print(result)
