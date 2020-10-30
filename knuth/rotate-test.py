from cuboid import Cuboid

import numpy as np

filename = "/Users/petermay/Documents/Processing/Tetris/shared-state"

block1 = Cuboid(1, np.array([(0,0,0), (1,0,0), (0,1,0), (1,1,0), (0,0,1)]))

block2 = Cuboid(2, np.array([(0,0,0), (0,1,0), (1,1,0)]))

blocks = [block1, block2]

boardSize = 2

# blockNum = input() 

# cuboid = blocks[int(blockNum)-1]

cuboid = blocks[1]

cuboid.print_processing(filename)

cuboid.rotate('x', 1, 1)

# cuboid.normalize()

cuboid.printBase()

cuboid.printLength()

cuboid.print_processing(filename)

cuboid.rotate('x', 1, 1)

# cuboid.normalize()

cuboid.printBase()

cuboid.printLength()

cuboid.print_processing(filename)

cuboid.rotate('x', 1, 1)

# cuboid.normalize()

cuboid.printBase()

cuboid.printLength()

cuboid.print_processing(filename)

cuboid.rotate('x', 1, 1)

# cuboid.normalize()

cuboid.printBase()

cuboid.printLength()

cuboid.print_processing(filename)

cuboid.print()

