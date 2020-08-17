import multiprocessing

from functools import partial
from multiprocessing.pool import ThreadPool

import time

class timer:
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        self.start = time.time()
        return None

    def __exit__(self, type, value, traceback):
        elapsed_time = (time.time() - self.start)
        print(self.message.format(elapsed_time))



def factorize_naive(n):
    """ A naive factorization method. Take integer 'n', return list of
        factors.
    """
    if n < 2:
        return []
    factors = []
    p = 2

    while True:
        if n == 1:
            return factors

        r = n % p
        if r == 0:
            factors.append(p)
            n = n / p
        elif p * p >= n:
            factors.append(n)
            return factors
        elif p > 2:
            # Advance in steps of 2 over odd numbers
            p += 2
        else:
            # If p == 2, get to 3
            p += 1
    assert False, "unreachable"


def factorize_naive_run(n, drs={}):
    drs[n] = factorize_naive(n)
    return drs



### Multiprocess version

workers = 200
input_data = [n for n in range(100000)]

with timer('Elapsed: {}s'):
    with multiprocessing.Pool(workers) as pool:
        pool.map(partial(factorize_naive_run), input_data)


### Thread version
# workers = 10
# input_data = [n for n in range(100000)]
#
# with timer('Elapsed: {}s'):
#     with ThreadPool(workers) as pool:
#         pool.map(partial(factorize_naive_run), input_data)