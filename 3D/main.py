from board import Board
from block import Block

import copy

# aBlock = Block("A", {(0,0,0), (1,0,0), (2,0,0), (1,0,1), (1,1,1)})

block1 = Block(1, {(0,0,0), (1,0,0), (1,0,1), (1,1,1), (2,1,1)})

block2 = Block(2, {(0,0,0),(1,0,0),(2,0,0),(3,0,0),(2,1,0)})

block3 = Block(3, {(0,0,0),(1,0,0),(1,1,0),(2,1,0),(3,1,0)})

block4 = Block(4, {(0,0,0),(0,1,0),(1,1,0),(-1,1,0),(0,1,-1), (0,2,-1)})

block5 = Block(5, {(0,0,0),(1,0,0),(0,1,0),(1,1,0),(1,1,-1)})

# block6 = Block(6, {(0,0,0),(0,0,1),(1,0,1),(1,1,1),(2,1,1)})

block6 = Block(6, {(0,0,0),(1,0,0),(2,0,0),(1,0,1),(0,1,0), (0,2,0)})

block7 = Block(7, {(0,0,0),(1,0,0),(2,0,0),(0,1,0),(0,1,-1)})

block8 = Block(8, {(0,0,0),(0,0,1),(0,1,1),(1,1,1),(2,1,1),(1,2,1)})

block9 = Block(9, {(0,0,0),(1,0,0),(1,1,0),(2,1,0),(2,1,-1)})

block10 = Block(10, {(0,0,0),(1,0,0),(2,0,0),(1,0,1),(1,1,1)})

block11 = Block(11, {(0,0,0),(1,0,0),(2,0,0),(2,1,0),(2,2,0)})

block12 = Block(12, {(0,0,0),(0,0,1),(1,0,1),(2,0,1),(2,1,1),(2,2,1)})

## 2x2x2 Test

# block1 = Block(1, {(0,0,0), (1,0,0), (0,1,0), (1,1,0), (0,0,1)})

# block2 = Block(2, {(0,0,0), (0,1,0), (1,1,0)})

## 3x3x3 Test

# block2 = Block(1, {(0,0,0), (1,0,0), (0,1,0), (1,1,0), (2,1,0), (2,2,0), (1,2,0), (0,2,0), (0,0,1), (1,0,1), (0,1,1), (1,1,1), (2,0,1), (2,1,1), (2,2,1), (0,2,1), (1,2,1)})

# block1 = Block(2, {(0,0,0), (1,0,0), (0,1,0), (1,1,0), (2,0,0), (2,1,0), (2,2,0), (1,2,0), (0,2,0), (2,0,-1)})

size = 4

solved = False

def solve(board, blocks):
  global solved, filename
  # board.show()
  while len(blocks) > 0 and not solved:
    block = blocks.pop()
    for space in board.available_spaces:
      # print(space)
      block.translate(space)
      # print(block.spaces)
      # block.print()
      for i in range(4):
        for j in range(4):
          for k in range(4):

            print("board")
            board.printState()
            print("potential block")
            block.printState()
            input("Press Enter to continue...")

            if board.can_fit(block):
              newBoard = board.place_block(block)
              newBlocks = copy.copy(blocks)
              solve(newBoard, newBlocks)
              # exit()
              if len(newBoard.available_spaces) == 0:
                solved = True
                print("")
                print("Yay! We did it!")
                newBoard.show()
                break
            block.rotateY()
            if solved:
              break
          block.rotateZ()
          if solved:
            break
        block.rotateX()
        if solved:
          break
      if solved:
        break


if __name__ == "__main__":

  board = Board(size)

  # block1.printState()

  # block2.printState()

  # exit()

  # aBlock.print()  

  # aBlock.translate((2,0,2))

  # aBlock.print()

  # aBlock.rotateZ()

  # aBlock.print()

  # aBlock.rotateX()

  # aBlock.print()


  # board.print()

  blocks = [block1, block2, block3, block4, block5, block6, block7, block8, block9, block10, block11, block12]


  # block1.printState()

  # block2.printState()

  # block3.printState()

  # block4.printState()

  # block5.printState()

  # block6.printState()

  # block7.printState()

  # block8.printState()

  # block9.printState()

  # block10.printState()

  # block11.printState()

  # block12.printState()

  # exit()

  # blocks = [block1, block2]

  solve(board, blocks)

  # print("Board")
  # print("---")
  # print("")

  # board.show()
  
  # print("Block: A")
  # print("---")
  # print("")

  # aBlock.show(4)
  # print("")



  # blocks = [aBlock, bBlock, cBlock, dBlock, eBlock]

  # print("Start")
  # print("---")
  # print("")
  # solve(board, blocks)