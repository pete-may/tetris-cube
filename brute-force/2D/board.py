class Board:
  def __init__(self, size):
    self.size = size
 
    self.available_spaces = set()
    for i in range(self.size):
  	  for j in range(self.size):
  	    self.available_spaces.add((i,j))

    self.text_matrix = []
    for i in range(self.size):
      row = []
      for j in range(self.size):
  	    row.append(" ")
      self.text_matrix.append(row)

  def show(self):
    # Need to flip it upside down to have y direction pointing up
    print("-------------")
    for j in range(self.size-1, -1 , -1):
      print("| ", end = '')
      for i in range(self.size):
        print(self.text_matrix[i][j], end = '')
        # print((i,j), end = '')
        if(i!=self.size-1):
          print(" | ", end = '')
      print(" |", end = '')
      print("")
      if(j!=0):
        print("-------------")

    print("-------------")
    # for i in range(self.size-1, -1 , -1):


  def can_fit(self, block):
    return block.spaces.issubset(self.available_spaces)

  def place_block(self, block):
    newBoard = Board(self.size)
    newBoard.available_spaces = self.available_spaces - block.spaces
    # newBoard.text_matrix = self.text_matrix
    newBoard.text_matrix = [row[:] for row in self.text_matrix]
    for space in block.spaces:
      newBoard.text_matrix[space[1]][space[0]] = block.id

    # print("old")
    print("")
    print("")
    self.show()
    # print("new")
    print("")
    print("")
    newBoard.show()

    return newBoard

  

