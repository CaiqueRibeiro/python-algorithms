# Build an algorithm that, given the input [126, 15, 28, 17], return the output [[2, 3, 3, 7], [3,5], [2,2,7], [17]]
    # Looking at the output, we can see that it's the prime factorization of each element of the input.
    # So I will have to iterate throw each one of the element N of the input and see its prime factors.
    # Use Crive of Eratosthenes

def prime_factorization(number):
  factors = []
  divisor = 2

  while number > 1:
    while number % divisor == 0:
      factors.append(divisor)
      number /= divisor

    divisor += 1

  return factors

def problem_2(input):
  output = []
  for x in input:
    output.append(prime_factorization(x))

  return output

print(problem_2([126, 15, 28, 17]))