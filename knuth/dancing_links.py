from helper_classes import *
import random

class DLX:
  def __init__(self, X, S):

    # Initialize the sparse matrix
    
    ## build the root column header
    self.root = Head()
    self.root.left = self.root.right = self.root

    ## build the column headers
    for col in X:
      self.add_head(col)

    ## build the rows
    for row in S:
      self.add_row(row) 

    self.solution = []


  def add_head(self, col):
    h = Head(col)
    h.right = self.root
    h.left = self.root.left
    h.right.left = h.left.right = h
    h.up = h.down = h


  def add_row(self, row):
    # make first node in row
    name = row.pop()
    currNode = self.add_node(name)

    # add all other nodes
    for name in row:
      currNode = self.add_node(name, currNode)


  def add_node(self, name, node=None):
    selectedHead = None
    for head in TraverseRight(self.root):
      if head.name == name:
        selectedHead = head
        break

    selectedHead.size = selectedHead.size + 1
    
    newNode = Node()
    if node: 
      # add the new node to the previous node
      newNode.right = node
      newNode.left = node.left
      newNode.right.left = newNode.left.right = newNode
    else: 
      # this is the first node in the row
      newNode.left = newNode.right = newNode
  
    newNode.head = newNode.down = selectedHead
    newNode.up = selectedHead.up
    newNode.up.down = newNode.down.up = newNode

    return newNode


  def cover(self, head):
    head.remove()
    for row in TraverseDown(head):
      for node in TraverseRight(row):
        node.remove()


  def uncover(self, head):
    for row in TraverseUp(head):
      for node in TraverseLeft(row):
        node.restore()
    head.restore() 

  def pushSolutionRow(self, row):
    arr = [row.head.name]
    spaces = set()
    for node in TraverseRight(row):
      arr.append(node.head.name)
    for el in arr:
      if type(el) == int:
        blockID = el
      else:
        spaces.add(el)
    solutionRow = [blockID, spaces]
    self.solution.append(solutionRow)
    self.solution = sorted(self.solution, key=lambda x: x[0])


  def solve(self):
    # base case: no more columns means puzzle is solved
    if self.root.right == self.root:
      return True

    # select a column with the least amount of nodes
    minSize = float('inf')
    selectedHead = None
    for head in TraverseRight(self.root):
      if minSize > head.size:
        minSize = head.size
        selectedHead = head

    # if no rows in the selected column, then we need to backtrack
    if selectedHead.down == selectedHead:
      return False

    # select a column
    self.cover(selectedHead)

    rowsRandom = []
    for row in TraverseDown(selectedHead):
      rowsRandom.append(row)

    # select rows in random order
    random.shuffle(rowsRandom)
    for row in rowsRandom:
      # select a row
      for node in TraverseRight(row):
        self.cover(node.head)

      if self.solve():
        # found a solution, lets pop out of the stack, adding selected rows to the solution as we go
        self.pushSolutionRow(row)
        return True

      # unselect the row
      for node in TraverseLeft(row):
        self.uncover(node.head)

    # unselect the column
    self.uncover(selectedHead)

    # no solutions found at this level, we need to backtrack
    return False


  # print stuff

  def print_cols(self):
    for node in TraverseRight(self.root):
      print(node.head.name)


  def print_row(self, node):
    for n in TraverseRight(node):
      print(n.head.name, end = '')
    print()


  def print_col(self, node):
    for n in TraverseDown(node):
      print(n.head.name)