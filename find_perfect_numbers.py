import math
import unittest


def is_perfect_number(num: int) -> dict:
    # scenario 1
    divisors = []
    if not isinstance(num, int) or num <= 1:
        # Return empty list and total 0 for invalid input (perfect numbers must be natural numbers)
        return {"divisors": [], "total": 0, "is_perfect": False}

    for d in range(1, int(math.sqrt(num)) + 1):
        if num % d == 0:
            divisors.append(d)
            # Avoid adding the square root twice
            # and avoid adding the number itself
            if d != num // d and d != 1:
                divisors.append(num//d)
    divisors.sort()
    return {
        "divisors": divisors,
        "total": sum(divisors),
        "is_perfect": sum(divisors) == num,
    }

def find_mersenne_primes(n: int) -> list:
    # scenario 2 1
    n = 1000 if n > 1000 else n
    # Sieve of Eratosthenes to find all primes up to n
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(math.sqrt(n)) +1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False

    primes = [ p for p in range(2, n) if sieve[p]]

    mersenne_primes = []
    for p in primes:
        # Bitwise operation to calculate Mersenne number (much more efficient than pow)
        mersenne = (1 << p) - 1
        # Check if the Mersenne number is prime and less than n
        if mersenne < n and sieve[mersenne]:
            mersenne_primes.append(mersenne)
    
    return mersenne_primes

def find_perfect_numbers(n: int) -> list:
    # scenario 2 2
    perfect_numbers = []
    # calculate max useful Mersenne prime
    max_mersenne = 1<<(int(math.log(math.sqrt(n)+1, 2)))
    sieve = [True] * (max_mersenne + 1)
    # Sieve of Eratosthenes to find all primes up to max_mersenne
    sieve[0] = sieve[1] = False

    for i in range(2, int(math.sqrt(max_mersenne)) +1):
        if sieve[i]:
            for j in range(i*i, max_mersenne+1, i):
                sieve[j] = False
    primes = [ p for p in range(2, max_mersenne) if sieve[p]]

    for p in primes:
        mersenne = (1 << p) - 1
        if mersenne < len(sieve):
            if sieve[mersenne]:
                pn = (2**(p -1)) * mersenne
                if pn <= n:
                    perfect_numbers.append(pn)
        else:
            break
    return perfect_numbers
    

class TestPerfectNumbers(unittest.TestCase):

    def test_perfect_number(self):
        self.assertEqual(is_perfect_number(6), {'divisors': [1, 2, 3], 'total': 6, 'is_perfect': True})
        self.assertEqual(is_perfect_number(10), {'divisors': [1, 2, 5], 'total': 8, 'is_perfect': False})
        self.assertEqual(is_perfect_number(28), {'divisors': [1, 2, 4, 7, 14], 'total': 28, 'is_perfect': True})

    def test_find_mersenne_primes(self):
        self.assertEqual(find_mersenne_primes(100), [3, 7, 31])

    def test_find_perfect_numbers(self):
        self.assertEqual(find_perfect_numbers(100000000), [6, 28, 496, 8128, 33550336])

if __name__ == "__main__":

    unittest.main()
