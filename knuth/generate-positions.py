from cuboid import Cuboid

filename = "/Users/petermay/Documents/Processing/Tetris/shared-state"

# block1 = Cuboid(1, {(0,0,0), (1,0,0), (1,0,1), (1,1,1), (2,1,1)})

# block2 = Cuboid(2, {(0,0,0),(1,0,0),(2,0,0),(3,0,0),(2,1,0)})

# block3 = Cuboid(3, {(0,0,0),(1,0,0),(1,1,0),(2,1,0),(3,1,0)})

# block4 = Cuboid(4, {(0,0,0),(0,1,0),(1,1,0),(-1,1,0),(0,1,-1), (0,2,-1)})

# block5 = Cuboid(5, {(0,0,0),(1,0,0),(0,1,0),(1,1,0),(1,1,-1)})

# block6 = Cuboid(6, {(0,0,0),(1,0,0),(2,0,0),(1,0,1),(0,1,0), (0,2,0)})

# block7 = Cuboid(7, {(0,0,0),(1,0,0),(2,0,0),(0,1,0),(0,1,-1)})

# block8 = Cuboid(8, {(0,0,0),(0,0,1),(0,1,1),(1,1,1),(2,1,1),(1,2,1)})

# block9 = Cuboid(9, {(0,0,0),(1,0,0),(1,1,0),(2,1,0),(2,1,-1)})

# block10 = Cuboid(10, {(0,0,0),(1,0,0),(2,0,0),(1,0,1),(1,1,1)})

# block11 = Cuboid(11, {(0,0,0),(1,0,0),(2,0,0),(2,1,0),(2,2,0)})

# block12 = Cuboid(12, {(0,0,0),(0,0,1),(1,0,1),(2,0,1),(2,1,1),(2,2,1)})

# blocks = [block1, block2, block3, block4, block5, block6, block7, block8, block9, block10, block11, block12]

## 2x2x2 Test

block1 = Cuboid(1, {(0,0,0), (1,0,0), (0,1,0), (1,1,0), (0,0,1)})

block2 = Cuboid(2, {(0,0,0), (0,1,0), (1,1,0)})

blocks = [block1, block2]


boardSize = 2

blockNum = input() 
# print(blockNum) 

cuboid = blocks[int(blockNum)-1]

# cuboid = Cuboid(1, {(0,0,0), (1,0,0), (0,1,0), (1,1,0), (0,0,1)})

# cuboid = Cuboid(1, {(0,0,0)})

def move_block_around():
  while(cuboid.xLength + cuboid.base[0] < boardSize+1):
    # print("what")
    while(cuboid.yLength + cuboid.base[1] < boardSize+1):
      # print("the")
      while(cuboid.zLength + cuboid.base[2] < boardSize+1):
        # print("heck")

        # print(cuboid.xLength)
        # print(cuboid.yLength)
        # print(cuboid.zLength)
        # cuboid.print_processing(filename)
        # print(cuboid.zLength)
        # print(cuboid.base[2])
        cuboid.print()
        cuboid.print_processing(filename)

        cuboid.translate((cuboid.base[0],cuboid.base[1],cuboid.base[2]+1))
      cuboid.translate((cuboid.base[0],cuboid.base[1],0))
      cuboid.translate((cuboid.base[0],cuboid.base[1]+1,cuboid.base[2]))
    cuboid.translate((cuboid.base[0],0,cuboid.base[2]))
    cuboid.translate((cuboid.base[0]+1,cuboid.base[1],cuboid.base[2]))
    
  cuboid.translate((0,0,0))


# cuboid.print_processing(filename)

cuboid.normalize()

move_block_around()

# cuboid.print_processing(filename)

# spin x4

cuboid.rotateX()

cuboid.normalize()

move_block_around()

# cuboid.print_processing(filename)

cuboid.rotateX()

cuboid.normalize()

move_block_around()

# cuboid.print_processing(filename)

cuboid.rotateX()

cuboid.normalize()

move_block_around()

# cuboid.print_processing(filename)

cuboid.rotateX()

cuboid.normalize()

# move_block_around()

# cuboid.print_processing(filename)

# new normal

cuboid.rotateZ()

cuboid.normalize()

move_block_around()

# cuboid.print_processing(filename)

# spin x4

cuboid.rotateY()

cuboid.normalize()

move_block_around()

# cuboid.print_processing(filename)

cuboid.rotateY()

cuboid.normalize()

move_block_around()

# cuboid.print_processing(filename)

cuboid.rotateY()

cuboid.normalize()

move_block_around()

# cuboid.print_processing(filename)

cuboid.rotateY()

cuboid.normalize()

# move_block_around()

# cuboid.print_processing(filename)

# new normal

cuboid.rotateZ()

cuboid.normalize()

move_block_around()

# cuboid.print_processing(filename)

# spin x4

cuboid.rotateX()

cuboid.normalize()

move_block_around()

# cuboid.print_processing(filename)

cuboid.rotateX()

cuboid.normalize()

move_block_around()

# cuboid.print_processing(filename)

cuboid.rotateX()

cuboid.normalize()

move_block_around()

# cuboid.print_processing(filename)

cuboid.rotateX()

cuboid.normalize()

# move_block_around()

# cuboid.print_processing(filename)

# new normal

cuboid.rotateZ()

cuboid.normalize()

move_block_around()

# cuboid.print_processing(filename)

# spin x4

cuboid.rotateY()

cuboid.normalize()

move_block_around()

# cuboid.print_processing(filename)

cuboid.rotateY()

cuboid.normalize()

move_block_around()

# cuboid.print_processing(filename)

cuboid.rotateY()

cuboid.normalize()

move_block_around()

# cuboid.print_processing(filename)

cuboid.rotateY()

cuboid.normalize()

# move_block_around()

# cuboid.print_processing(filename)

# new normal

cuboid.rotateX()

cuboid.normalize()

move_block_around()

# cuboid.print_processing(filename)

# spin x4

cuboid.rotateZ()

cuboid.normalize()

move_block_around()

# cuboid.print_processing(filename)

cuboid.rotateZ()

cuboid.normalize()

move_block_around()

# cuboid.print_processing(filename)

cuboid.rotateZ()

cuboid.normalize()

move_block_around()

# cuboid.print_processing(filename)

cuboid.rotateZ()

cuboid.normalize()

# move_block_around()

# cuboid.print_processing(filename)

# new normal

cuboid.rotateX()

cuboid.rotateX()

cuboid.normalize()

move_block_around()

# cuboid.print_processing(filename)

# spin x4

cuboid.rotateZ()

cuboid.normalize()

move_block_around()

# cuboid.print_processing(filename)

cuboid.rotateZ()

cuboid.normalize()

move_block_around()

# cuboid.print_processing(filename)

cuboid.rotateZ()

cuboid.normalize()

move_block_around()

# cuboid.print_processing(filename)

cuboid.rotateZ()

cuboid.normalize()

# move_block_around()

# cuboid.print_processing(filename)


