# Build an algorithm that, given the input [3, 1, 4, 6, 1, 5], return the output [5, 2, 7, 14, 2, 10]
    # Verifying the input and output, we can see that the output is the sum of the input and the fibonacci sequence.
    # So I'll have to iterate through each element N of the input and sum it with the fibonacci number in the position N.

def fibo(v):
  if v == 0 or v == 1:
    return 1
  
  i = 0
  j = 1

  for k in range(2, v+1):
    t = j
    j = i + j
    i = t

  return j

def problem_1(input):
  output = []
  for x in input:
    output.append(x + fibo(x))

  return output

print(problem_1([3, 1, 4, 6, 1, 5]))
