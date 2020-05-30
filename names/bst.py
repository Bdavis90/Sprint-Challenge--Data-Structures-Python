"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class BSTNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  # Insert the given value into the tree
  def insert(self, value):
        # Recursive
    if value < self.value:
      if self.left is None:
        self.left = BSTNode(value)
      else:
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = BSTNode(value)
      else:
        self.right.insert(value)

              
  # Return True if the tree contains the value
  # False if it does not
  def contains(self, target):
    if self.value == target:
      return True
    elif target < self.value:
      if self.left is None:
        return False
      else:
        return self.left.contains(target)
    else:
      if self.right is None:
        return False
      else:
        return self.right.contains(target)


# Return the maximum value found in the tree
  def get_max(self):
    curr_max = self.value
    if self.right is None:
      return curr_max
    else:
      return self.right.get_max()
    
    # curr_max = self
    # while curr_max.right:
    #     curr_max = curr_max.right
    # return curr_max.value

    # Call the function `fn` on the value of each node
  def for_each(self, fn):
    fn(self.value)

    if self.left:
      self.left.for_each(fn)
    
    if self.right:
      self.right.for_each(fn)
