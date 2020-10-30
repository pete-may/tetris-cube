from board import Board
from block import Block

import copy

block1 = Block(1, {(0,0,0), (1,0,0), (1,0,1), (1,1,1), (2,1,1)})

block2 = Block(2, {(0,0,0),(1,0,0),(2,0,0),(3,0,0),(2,1,0)})

block3 = Block(3, {(0,0,0),(1,0,0),(1,1,0),(2,1,0),(3,1,0)})

block4 = Block(4, {(0,0,0),(0,1,0),(1,1,0),(-1,1,0),(0,1,-1), (0,2,-1)})

block5 = Block(5, {(0,0,0),(1,0,0),(0,1,0),(1,1,0),(1,1,-1)})

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


# solve from bottom to top
def chooseSpace(spaces):
  for lowestY in range(4):
    for space in spaces:
      if lowestY is space[1]:
        return space


def solve(board, blocks):
  global solved, filename
  # board.show()
  while len(blocks) > 0 and not solved:
    block = blocks.pop()
    for space in sorted(board.available_spaces, key=lambda x: x[1]):
      # space = chooseSpace(board.available_spaces)
      # print(space)
      block.translate(space)
      # print(block.spaces)
      # block.print()
      for i in range(4):
        for j in range(4):
          for k in range(4):

            # print("board")
            board.print_processing(block)
            # print("potential block")
            # block.print_processing()
            # input("Press Enter to continue...")

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

  # Testing

  # block1.print_processing()

  # block2.print_processing()

  # block3.print_processing()

  # block4.print_processing()

  # block5.print_processing()

  # block6.print_processing()

  # block7.print_processing()

  # block8.print_processing()

  # block9.print_processing()

  # block10.print_processing()

  # block11.print_processing()

  # block12.print_processing()

  # blocks = [block1, block2]


  board = Board(size)

  blocks = [block1, block2, block3, block4, block5, block6, block7, block8, block9, block10, block11, block12]

  solve(board, blocks)
