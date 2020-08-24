filename = "/Users/peter.may@ibm.com/Documents/Processing/Tetris/shared-state"

class Block:
  def __init__(self, id, spaces):
    self.id = id
    self.spaces = spaces
    self.pivot = (0,0,0)

  def rotateZ(self):
    newSpaces = set()
    for point in self.spaces:
      x, y = point[0], point[1]
      ox, oy = self.pivot[0], self.pivot[1]
      newx = ox + (y-oy)
      newy = oy - (x-ox)
      newSpaces.add((newx,newy, point[2]))
      
    self.spaces = newSpaces
  
  def rotateY(self):
    newSpaces = set()
    for point in self.spaces:
      x, z = point[0], point[2]
      ox, oz = self.pivot[0], self.pivot[2]
      newx = ox + (z-oz)
      newz = oz - (x-ox)
      newSpaces.add((newx, point[1], newz))

    self.spaces = newSpaces
  
  def rotateX(self):
    newSpaces = set()
    for point in self.spaces:
      z, y = point[2], point[1]
      oz, oy = self.pivot[2], self.pivot[1]
      newz = oz + (y-oy)
      newy = oy - (z-oz)
      newSpaces.add((point[0], newy, newz))


      
    self.spaces = newSpaces
  # # Every block start with a pivot at 0,0. Translate() moves the block's pivot arount the board.
  def translate(self, pos):
    dx = pos[0] - self.pivot[0]
    dy = pos[1] - self.pivot[1]
    dz = pos[2] - self.pivot[2]

    newSpaces = set()

    for point in self.spaces:
      newx = point[0] + dx
      newy = point[1] + dy
      newz = point[2] + dz
      newSpaces.add((newx,newy,newz))
      
    # print(self.spaces)
    self.spaces = newSpaces
    # print(self.spaces)
    self.pivot = pos

  def show(self):
    print("\"" + str(self.id) + "\", ",  end = '')
    print(self.spaces)

  def printState(self):
    string = str(self.id) + " " + str(len(self.spaces))
    for point in self.spaces:
      string += " " + str(point[0]) + " " + str(point[1]) + " " + str(point[2])
    with open(filename, 'a') as f:
      print(string, file=f)

    # print(self.spaces)
    # input("Press Enter to continue...")
