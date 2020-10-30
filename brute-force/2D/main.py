from board import Board
from block import Block

import copy

aBlock = Block("A", {(0,0), (0,1), (0,2), (1,1)})

bBlock = Block("B", {(0,0), (0,1), (1,1)})

cBlock = Block("C", {(0,0), (1,0)})

solved = False

def solve(board, blocks):
  global solved
  while len(blocks) > 0 and not solved:
    block = blocks.pop()
    for space in board.available_spaces:
      # print(space)
      block.translate(space)
      # print(block.spaces)
      # block.show(3)
      for i in range(4):
        if board.can_fit(block):
          newBoard = board.place_block(block)
          newBlocks = copy.copy(blocks)
          solve(newBoard, newBlocks)
          if len(newBoard.available_spaces) == 0:
            solved = True
            print("")
            print("Yay! We did it!")
            break
        block.rotate()
        if solved:
          break
      if solved:
        break

        


if __name__ == "__main__":
  board = Board(3)

  print("Board")
  print("---")
  print("")

  board.show()
  

  print("Block: A")
  print("---")
  print("")

  aBlock.show(3)
  print("")

  print("Block: B")
  print("---")
  print("")

  bBlock.show(3)
  print("\n")

  print("Block: C")
  print("---")
  print("")

  cBlock.show(3)
  print("")

  boardHistory = [board]

  blocks = [aBlock, bBlock, cBlock]

  print("Start")
  print("---")
  print("")
  solve(board, blocks)