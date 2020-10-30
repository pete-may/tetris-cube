class Node:
  def remove(self):
    self.up.down = self.down
    self.down.up = self.up
    self.head.size = self.head.size - 1

  def restore(self):
    self.up.down = self.down.up = self
    self.head.size = self.head.size + 1


class Head(Node):
  def __init__(self, name=None):
    self.size = 0
    self.name = name

  def remove(self):
    self.right.left = self.left
    self.left.right = self.right

  def restore(self):
    self.right.left = self.left.right = self


class TraverseRight:
  def __init__(self, node):
    self.node = self.start = node

  def __iter__(self):
    return self

  def __next__(self):
    if self.node.right == self.start:
      raise StopIteration
    else:
      self.node = self.node.right
      return self.node


class TraverseLeft:
  def __init__(self, node):
    self.node = self.start = node

  def __iter__(self):
    return self

  def __next__(self):
    if self.node.left == self.start:
      raise StopIteration
    else:
      self.node = self.node.left
      return self.node


class TraverseDown:
  def __init__(self, node):
    self.node = self.start = node

  def __iter__(self):
    return self

  def __next__(self):
    if self.node.down == self.start:
      raise StopIteration
    else:
      self.node = self.node.down
      return self.node


class TraverseUp:
  def __init__(self, node):
    self.node = self.start = node

  def __iter__(self):
    return self

  def __next__(self):
    if self.node.up == self.start:
      raise StopIteration
    else:
      self.node = self.node.up
      return self.node