import math
import time
import numpy as np

def is_integer(n):
    return np.equal(np.mod(n, 1), 0)

batch_size = 16

def check_prime(n):
    sqrt_n = math.sqrt(n)
    n_float = float(n)
    numbers = range(2, int(sqrt_n) + 1)
    for i in range(0, len(numbers), batch_size):
        n_batch = np.array(numbers[i:i + batch_size])
        if any(is_integer(n_float / n_batch)):
            return False
    return True

# print('check 10000000', check_prime(10000000))
# print('check 10000019', check_prime(10000019))

t = time.time()
for i in range(2, 100000):
    check_prime(i)
print('Cost Time:', time.time() - t)
