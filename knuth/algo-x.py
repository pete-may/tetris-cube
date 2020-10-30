from dancing_links import DLX
from cuboid import Cuboid
import numpy as np

filename = "/Users/petermay/Documents/Processing/Tetris/shared-state"

import sys

boardSize=4

blockNum = 12

X = set()
S = []

for x in range(blockNum):
  X.add(x+1)

for x in range(boardSize):
  for y in range(boardSize):
    for z in range(boardSize):
      X.add((x,y,z))


with open(sys.argv[1], 'r') as f:
  lines = [line.rstrip() for line in f]
  for line in lines:
    S.append(set(eval(line)))

# print(X)
# print(S)

dancingLinks = DLX(X, S)

print("Solved: " + str(dancingLinks.solve()))

print()

for row in dancingLinks.solution:
  print(row)

print()

open(filename, 'w').close()

for row in sorted(dancingLinks.solution, key=lambda row: min(row[1], key = lambda point: point[1])[1]):
  cuboid=Cuboid(row[0],np.array(list(row[1])))
  cuboid.print_processing(filename)
  print(row)

# for row in dancingLinks.solution:
#   print(min(row[1], key = lambda point: point[1]))

