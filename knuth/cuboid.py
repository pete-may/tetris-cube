import numpy as np

class Cuboid:
  def __init__(self, id, spaces):
    self.id = id
    self.spaces = spaces
    self.base = (0,0,0)

    self.normal = (1,0,0)

    self.setMinMax()

  def setMinMax(self):
    maxX = -10
    maxY = -10
    maxZ = -10
    minX = 10
    minY = 10
    minZ = 10

    for space in self.spaces:
      if maxX < space[0]:
        maxX = space[0]
      if minX > space[0]:
        minX = space[0]
      if maxY < space[1]:
        maxY = space[1]
      if minY > space[1]:
        minY = space[1]
      if maxZ < space[2]:
        maxZ = space[2]
      if minZ > space[2]:
        minZ = space[2]

    
    self.xLength = maxX-minX+1
    self.yLength = maxY-minY+1
    self.zLength = maxZ-minZ+1

  def normalize(self):
    minX = 10
    minY = 10
    minZ = 10

    for space in self.spaces:
      if minX > space[0]:
        minX = space[0]
      if minY > space[1]:
        minY = space[1]
      if minZ > space[2]:
        minZ = space[2]

    self.translate((abs(minX), abs(minY), abs(minZ)))
    self.base = (0,0,0)

  def setNormal(self, newNormal):
    c = np.cross(self.normal, newNormal)
    
    if (c==0).all():
      d = self.whatDirection(self.normal)
      # print(self.normal)
      axes = ['x','y','z']
      axes.remove(d)
      a = axes[0]
      self.rotate(a, 1, 2)

    elif (c>0).any():
      d = self.whatDirection(c)
      self.rotate(d, 1, 1)

    else:
      d = self.whatDirection(c)
      self.rotate(d, -1, 1)

    self.normal = newNormal

  # Spin around current normal
  def spin(self):
    a = self.whatDirection(self.normal)
    self.rotate(a, 1, 1)

  def whatDirection(self, n):
    # print(n)
    idx = np.where(n!=0)[0][0]
    # print(idx)
    return ['x','y','z'][idx]

  # Rotate on a given axis, units param indicates 90 degree increments
  def rotate(self, axis, direction, units):
    rotationMatrix = []
    c = np.rint(np.cos(units * direction * (np.pi/2)))
    s = np.rint(np.sin(units * direction * (np.pi/2)))
    if axis == 'x':
      rotationMatrix = np.array([[1, 0, 0], 
                                 [0, c,-s],
                                 [0, s, c]])
    elif axis == 'y':
      rotationMatrix = np.array([[ c, 0, s], 
                                 [ 0, 1, 0],
                                 [-s, 0, c]])
    elif axis == 'z':
      rotationMatrix = np.array([[c,-s, 0], 
                                 [s, c, 0],
                                 [0, 0, 1]])

    self.spaces = np.dot(self.spaces, rotationMatrix)
    self.setMinMax()

  def translate(self, pos):
    dx = pos[0] - self.base[0]
    dy = pos[1] - self.base[1]
    dz = pos[2] - self.base[2]

    newSpaces = []

    for point in self.spaces:
      newx = point[0] + dx
      newy = point[1] + dy
      newz = point[2] + dz
      newSpaces.append((newx,newy,newz))
      
    self.spaces = np.array(newSpaces)
    self.base = pos

  def print(self):
    print(str(self.id) + ", ",  end = '')
    spaces = []
    for space in self.spaces:
      spaces.append(np.array2string(space.astype(int), separator=','))
    print(", ".join(spaces))

  def print_processing(self, filename):
    string = str(self.id) + " " + str(len(self.spaces))
    for point in self.spaces:
      string += " " + str(point[0].astype(int)) + " " + str(point[1].astype(int)) + " " + str(point[2].astype(int))

    with open(filename, 'a') as f:
      print(string, file=f)

    # print(self.spaces)
    # print(self.base)
    # input("Press Enter to continue...")

  def printBase(self):
    print("Base:")
    print(self.base)

  def printLength(self):
    print("x length:")
    print(self.xLength)
    print("y length:")
    print(self.yLength)
    print("z length:")
    print(self.zLength)