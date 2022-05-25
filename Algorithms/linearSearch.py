# LINEAR SEARCH ALGORITHMS
# O(n) time complexity

# Iterative
def iterativeLinearSearch(array, target, attribute): # Works
  for i in range(0, len(array)):
    # If target is found
    if array[i].__dict__[attribute] == target:
      print("Target is present at index", i) # Return index
      break
    elif array[i].__dict__[attribute] != array[-1]: # If still being looped
      continue # Keep going
    else: 
      print("Target is absent")


# Recursive
def recursiveLinearSearch(array, f, l, target, attribute): # Works
  # f and l denote first and last index of the array
  try:
    if l < f:
      print("Target is absent")
    elif array[f].__dict__[attribute] == target:
      print("Target is present at index ", f)
    elif array[l].__dict__[attribute] == target:
      print("Target is present at index ", l)
    else:
      # Close in from both sides of the list
      return recursiveLinearSearch(array, f+1, l-1, target, attribute)
  except RecursionError:
    print("StackOverflowError\n")
  
