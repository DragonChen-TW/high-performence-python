import math

def check_prime(n):
    sqrt_n = math.sqrt(n)
    n_float = float(n)
    for i in range(2, int(sqrt_n) + 1):
        if (n_float / i).is_integer():
            return False
    return True

print('check 1000000', check_prime(1000000))
print('check 1000019', check_prime(1000019))