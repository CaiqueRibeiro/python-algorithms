# Given an array of integers and a number n, find out which n integers form the biggest sum.
# It can be all from beginning, all to end, part of beginning and part of end
# but it cannot be from the middle.

def calc(v, n):
  biggestSum = sum(v[0:n]) # 0 to n - 1
  factor = n - 1
  while(factor >= 0):
    currentSum = 0
    for i in range(0, factor): # 0 to n - 1
      currentSum += v[i]

    for i in range(1, n - factor + 1):
      currentSum += v[len(v) - i]

    factor -= 1

    biggestSum = max(biggestSum, currentSum)

  return biggestSum

print(calc([5, 0, -1, 3, -2, 5, 7, 9], 4)) # expect to be 26