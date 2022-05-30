# LINEAR SEARCH ALGORITHMS
# O(n) time complexity

# Iterative
def iterativeLinearSearch(array, target, attribute): # Works
  for i in range(0, len(array)):
    # If target is found
    if array[i].__dict__[attribute] == target:
      return i # Return index
    
  return -1 # Occurs if loop is completed

# Recursive
def recursiveLinearSearch(array, f, l, target, attribute): # Works
  # f and l denote first and last index of the array
  try:
    if l < f:
      return -1
    elif array[f].__dict__[attribute] == target:
      return f
    elif array[l].__dict__[attribute] == target:
      return l
    else:
      # Close in from both sides of the list
      return recursiveLinearSearch(array, f+1, l-1, target, attribute)
  except RecursionError:
    print("StackOverflowError\n")
