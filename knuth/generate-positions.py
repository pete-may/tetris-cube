from cuboid import Cuboid

import numpy as np

## 2x2x2 Test

# block1 = Cuboid(1, np.array([(0,0,0), (1,0,0), (0,1,0), (1,1,0), (0,0,1)]))

# block2 = Cuboid(2, np.array([(0,0,0), (0,1,0), (1,1,0)]))

# blocks = [block1, block2]

# blockNum = input() 
# # print(val) 

# cuboid = blocks[int(blockNum)-1]

filename = "/Users/petermay/Documents/Processing/Tetris/shared-state"

block1 = Cuboid(1, np.array([(0,0,0), (1,0,0), (1,0,1), (1,1,1), (2,1,1)]))

block2 = Cuboid(2, np.array([(0,0,0),(1,0,0),(2,0,0),(3,0,0),(2,1,0)]))

block3 = Cuboid(3, np.array([(0,0,0),(1,0,0),(1,1,0),(2,1,0),(3,1,0)]))

block4 = Cuboid(4, np.array([(0,0,0),(0,1,0),(1,1,0),(-1,1,0),(0,1,-1), (0,2,-1)]))

block5 = Cuboid(5, np.array([(0,0,0),(1,0,0),(0,1,0),(1,1,0),(1,1,-1)]))

block6 = Cuboid(6, np.array([(0,0,0),(1,0,0),(2,0,0),(1,0,1),(0,1,0), (0,2,0)]))

block7 = Cuboid(7, np.array([(0,0,0),(1,0,0),(2,0,0),(0,1,0),(0,1,-1)]))

block8 = Cuboid(8, np.array([(0,0,0),(0,0,1),(0,1,1),(1,1,1),(2,1,1),(1,2,1)]))

block9 = Cuboid(9, np.array([(0,0,0),(1,0,0),(1,1,0),(2,1,0),(2,1,-1)]))

block10 = Cuboid(10, np.array([(0,0,0),(1,0,0),(2,0,0),(1,0,1),(1,1,1)]))

block11 = Cuboid(11, np.array([(0,0,0),(1,0,0),(2,0,0),(2,1,0),(2,2,0)]))

block12 = Cuboid(12, np.array([(0,0,0),(0,0,1),(1,0,1),(2,0,1),(2,1,1),(2,2,1)]))

blocks = [block1, block2, block3, block4, block5, block6, block7, block8, block9, block10, block11, block12]

normals = np.array([(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)])

boardSize = 4

def move_block_around(positions):
  while(cuboid.xLength + cuboid.base[0] < boardSize+1):
    while(cuboid.yLength + cuboid.base[1] < boardSize+1):
      while(cuboid.zLength + cuboid.base[2] < boardSize+1):
        
        position = []
        for s in cuboid.spaces:
          position.append(tuple(s))
        positions.add(frozenset(position))

        cuboid.translate((cuboid.base[0],cuboid.base[1],cuboid.base[2]+1))
      cuboid.translate((cuboid.base[0],cuboid.base[1],0))
      cuboid.translate((cuboid.base[0],cuboid.base[1]+1,cuboid.base[2]))
    cuboid.translate((cuboid.base[0],0,cuboid.base[2]))
    cuboid.translate((cuboid.base[0]+1,cuboid.base[1],cuboid.base[2]))
  cuboid.translate((0,0,0))

for block in blocks:
  cuboid = block
  positions = set()

  for n in normals:
    cuboid.setNormal(n)
    cuboid.normalize()

    for _ in range(4):
      move_block_around(positions)
      cuboid.spin()
      cuboid.normalize()

  for p in positions:
    print(str(cuboid.id),  end='')
    spaces = []
    for space in p:
      print(", ", end='')
      print(tuple(np.array(space).astype(int)), end='')
      spaces.append(tuple(np.array(space).astype(int)))
    print()
