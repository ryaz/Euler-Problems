# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(number):
  num_string = str(number)
  left = 0
  right = len(num_string) - 1
  while left < right:
    if not num_string[left] == num_string[right]:
      return False
    left += 1
    right -= 1

  return True

def solver():
  maximum = -1

  for i in range(100, 1000):
    for j in range(100, 1000):
      if is_palindrome(i * j):
        if i * j > maximum:
          maximum = i * j

  return maximum

print(solver())
