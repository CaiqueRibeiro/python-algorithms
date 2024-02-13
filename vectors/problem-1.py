# Find the number in array that do not repeat [5,3,5,1,3,4,7,7,4,3]

def find(v): # version using hash table. O(n)
  count = {}

  for x in v:
    if x in count:
      count[x] += 1
    else:
      count[x] = 1

  for x in v:
    if count[x] == 1:
      return x
  
  return None

print(find([5,3,5,1,3,4,7,7,4,3])) # expect to be 1

def findSorted(v): # version using sort. O(n log n)
  sorted_vector = sorted(v)

  if(sorted_vector[0] != sorted_vector[1]):
    return sorted_vector[0]
  if(sorted_vector[len(sorted_vector)-1] != sorted_vector[len(sorted_vector)-2]):
    return sorted_vector[len(sorted_vector)-1] 
  
  for i in range(2, len(sorted_vector)-1):
    if(sorted_vector[i] != sorted_vector[i-1] and sorted_vector[i] != sorted_vector[i+1]):
      return sorted_vector[i]
  return None

print(findSorted([5,3,5,1,3,4,7,7,4,3])) # expect to be 1