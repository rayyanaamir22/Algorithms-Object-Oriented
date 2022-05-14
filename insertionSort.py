# INSERTION SORT
# O(n^2) time complexity -- WORST

def insertionSort(array, attribute): # Can I make the attribute to sort by a parameter???????
  # Linear loop
  for i in range(len(array)):
    # Store current element for comparison with previous one
    temp = array[i]
    j = i - 1
    
    # Quadratic loop
    # WHILE previous element is greater than temp
    while j >= 0 and temp.__dict__[attribute] < array[j].__dict__[attribute]:
      # Move previous element forward
      array[j+1] = array[j]
      j -= 1

    # Move current element ahead
    array[j+1] = temp