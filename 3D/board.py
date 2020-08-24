import copy

filename = "/Users/peter.may@ibm.com/Documents/Processing/Tetris/shared-state"

smallestBlockSize = 5

class Board:
  def __init__(self, size):
    self.size = size

    self.available_spaces = set()
    for i in range(size):
      for j in range(size):
        for k in range(size):
          self.available_spaces.add((i,j,k))

    self.contained_blocks = []

  def show(self):
    for block in self.contained_blocks:
      block.show()

  def can_fit(self, block):
    canFit = block.spaces.issubset(self.available_spaces)
    if not canFit:
      return False

    noGaps = self.no_gaps(block)
    if not noGaps:
        return False
    
    return True
    

  def place_block(self, block):
    newBoard = Board(self.size)
    newBoard.available_spaces = self.available_spaces - block.spaces
    newBoard.contained_blocks = copy.copy(self.contained_blocks)
    newBoard.contained_blocks.append(block)


    return newBoard

  def no_gaps(self, block):
    postBlockSpaces = self.available_spaces - block.spaces
    if postBlockSpaces == 0:
      return True
    gaps = []
    while len(postBlockSpaces) > 0:
      currentSpace = postBlockSpaces.pop()
      currentGap = []
      unprocessed = {currentSpace}

      while len(unprocessed) > 0:
        unprocessedSpace = unprocessed.pop()
        for space in postBlockSpaces:
          if self.is_adjacent(unprocessedSpace, space):
            unprocessed.add(space)

        # print(unprocessed)
        # print(unprocessedSpace)
        # print("These are the spaces left: " + str(postBlockSpaces))
        # print("Lets remove this one: " + str(unprocessedSpace))
        if unprocessedSpace is not currentSpace:
          postBlockSpaces.remove(unprocessedSpace)
        currentGap.append(unprocessedSpace)
      gaps.append(currentGap)

    # print("these are the gaps:")
    # for gap in gaps:
    #   print(gap)

    min = 100
    for gap in gaps:
      if len(gap) < min:
        min = len(gap)

    if min < smallestBlockSize:
      return False
    
    return True
   
  def is_adjacent(self, p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2]) == 1

  def printState(self):
    open(filename, 'w').close()
    for block in self.contained_blocks:
      block.printState()
    input("Press Enter to continue...")


