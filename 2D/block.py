class Block:
  def __init__(self, id, spaces):
    self.id = id
    self.spaces = spaces
    self.pivot = (0,0)

  def rotate(self):
    newSpaces = set()
    for point in self.spaces:
      x, y = point
      ox, oy = self.pivot
      newx = ox + (y-oy)
      newy = oy - (x-ox)
      newSpaces.add((newx,newy))
      
    self.spaces = newSpaces



  # # Every block start with a pivot at 0,0. Translate() moves the block's pivot arount the board.
  def translate(self, pos):
    dx = pos[0] - self.pivot[0]
    dy = pos[1] - self.pivot[1]

    newSpaces = set()

    for point in self.spaces:
      newx = point[0] + dx
      newy = point[1] + dy
      newSpaces.add((newx,newy))
      
    self.spaces = newSpaces
    self.pivot = pos

  def show(self, board_size):
    # Need to flip it upside down to have y direction pointing up
    # for j in range(board_size-1, -1, -1):
    #   row = []
    #   for i in range(board_size):
    #     if (i,j) in self.spaces: 
    #       row.append(self.id)
    #     else: 
    #       row.append('X')
    #   print(' '.join(row), '\n')


    # Need to flip it upside down to have y direction pointing up
    print("-------------")
    for j in range(board_size-1, -1 , -1):
      print("| ", end = '')
      for i in range(board_size):
        if (i,j) in self.spaces: 
          print(self.id,  end = '')
          # print((i,j),  end = '')
        else: 
          print(' ',  end = '')
        if(i!=board_size-1):
          print(" | ", end = '')
      print(" |", end = '')
      print("")
      if(j!=0):
        print("-------------")

    print("-------------")
    # for i in range(self.size-1, -1 , -1):


