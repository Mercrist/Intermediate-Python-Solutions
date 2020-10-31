def is_prime(n):
    '''is_prime(n) -> boolean
    returns True if n is prime, False otherwise'''
    if n < 2:
        return False
    for divisor in range(2,int(n**0.5)+1):
        if n % divisor == 0:
            return False
    return True

def sum_of_prime_cubes(n):
    '''sum_of_prime_cubes(n) -> int
    returns sum of cubes of all primes <=n'''
    return sum([n**3 for n in range (n+1) if is_prime (n)])

# test case
print(sum_of_prime_cubes(10))   # should be 503
print(sum_of_prime_cubes(200))  # this is your answer
