# BINARY SEARCH ALGORITHMS
# O(log n) time complexity

# Recursive
def recursiveBinarySearch(array, min, max, target, attribute): # Works
  # Base case
  if max >= min:
    # Floor division for whole number
    middle = (max+min)//2 # Inaccuracy is compensated for since the search will immediately determine subset.
    
    if array[middle].__dict__[attribute] == target: # If middle is target
      print('Target is present at index ', middle)
    elif array[middle].__dict__[attribute] > target: # If target is behind
      return recursiveBinarySearch(array, min, middle - 1, target, attribute)
    else: # If target is ahead
      return recursiveBinarySearch(array, middle + 1, max, target, attribute)
  else: # Target is absent
    print('Target is absent')

# Iterative
def iterativeBinarySearch(array, min, max, target, attribute): # Works
  absent = True
  while min <= max:
    middle = (max+min)//2

    if array[middle].__dict__[attribute] < target:
      min = middle + 1
    elif array[middle].__dict__[attribute] > target:
      max = middle - 1
    else:
      print("Target is present at index", middle)
      absent = False # Using return makes this tedious in main.py
      break
  
  # Since return doesn't work
  if absent:
    print("Target is absent")