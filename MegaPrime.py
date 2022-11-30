# What is a megaprime? Question by Nathan Grosvenor
def is_prime(n):
    # check for it is a mega prime
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(n**0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def is_megaprime(n):
    # check for it is a mega prime
    if is_prime(n):
        for i in str(n):
            if not is_prime(int(i)):
                return False
        return True
    return False

def megaprime(max):
    return [i for i in range(1, max + 1) if is_megaprime(i)]

print(megaprime(10))
print(megaprime(37))
print(megaprime(1))
