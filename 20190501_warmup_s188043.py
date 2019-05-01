'''Create the following function 
func(x)-> []
Calculate and return all prime factors of x and return as list

Ex: f(13195)-> [5, 7, 13, 29]'''
import math
def get_prime_factors(number):
    factors = []
    for num in range(1,number):
        if number %num == 0 and num % 2 != 0:
            factors.append(num)
    for val in factors:
        for num in range(3,val):
            if val % num == 0:
                factors.remove(val)
                break
    return factors

print(get_prime_factors(13195))
