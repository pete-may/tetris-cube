add_library('peasycam')

from test_shape import TestShape

from block import Block
from board import Board

import copy

cubesize = 4

BLOCKS = []

blocks = []

COLORS = [255,255,0]

solved = False

presentBlock = None

paused = False
  
def setup():
  
  board = Board(cubesize)
  
  cam = PeasyCam(this, 600)

  size(800, 800, P3D)
  
  background(51)
  scale(0.5)

r = 0
def draw():
  global BLOCKS, r
  background(30)
  scale(0.5)
  # lights()
  # noStroke()
  noFill()
  stroke(255)
  
  rotateY(r);
  r=r+0.2
  
  for i in range(cubesize):
    for j in range(cubesize):
      for k in range(cubesize):
        pushMatrix()
        translate(i*100,-j*100,k*100)
        box(100);
        popMatrix()
  
  if (frameCount % 10 == 0):
    BLOCKS = []
    reader = createReader("shared-state")
    line = reader.readLine()
    
    while line:

      # Split eace line on a tab. 
      strs = line.split(" ")
      id = int(strs[0])
      pointsLen = int(strs[1])
      points = set()
      for x in range(pointsLen):
        i = int(strs[2 + (3 * x)])
        j = int(strs[2 + (3 * x) + 1])
        k = int(strs[2 + (3 * x) + 2])
        points.add((i, j, k))
        
      # print(points)
      BLOCKS.append(Block(id, points))
      
      line = reader.readLine()
      
  for block in BLOCKS:
    block.show()
