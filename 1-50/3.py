# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def largest_prime_factor(number):
  largest = None
  current = 2
  maximum = number / current
  while current < maximum:
    if number % current == 0:
      if is_prime(number // current):
        return number // current
      if is_prime(current):
        largest = current
    current += 1
    maximum = number / current

  return largest


def is_prime(number):
  current = 2
  maximum = number / current

  while current <= maximum:
    if number % current == 0:
      return False
    else:
      current += 1
      maximum = number / current

  return True

print(largest_prime_factor(600851475143))