# Given an array of integers, build bars with height of the integer values, separated by 1 unit.
# Find out which two bars form the biggest rectangle area.

def calc(v):
  area = 0
  left_pointer = 0
  right_pointer = len(v) - 1

  while left_pointer < right_pointer:
    height = min(v[left_pointer, v[right_pointer]])
    width = right_pointer - left_pointer
    current_area = height * width
    area = max(area, current_area)

    if v[left_pointer] < v[right_pointer]:
      left_pointer += 1
    else:
      right_pointer -= 1

  return area

print(calc([3, 1, 2, 4, 5])) # expect to be 12