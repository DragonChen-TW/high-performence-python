import math
import time

def check_prime(n):
    sqrt_n = math.sqrt(n)
    n_float = float(n)
    for i in range(2, int(sqrt_n) + 1):
        if (n_float / i).is_integer():
            return False
    return True

# print('check 10000000', check_prime(10000000))
# print('check 10000019', check_prime(10000019))

t = time.time()
for i in range(2, 100000):
    check_prime(i)
print('Cost Time:', time.time() - t)
