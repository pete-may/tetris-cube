COLORS = [[255,255,0], [255,0,0], [0,0,255]]


class Block:
  def __init__(self, id, spaces):
    self.id = id
    self.spaces = spaces
    self.pivot = (0,0,0)

  def show(self):
    pushMatrix()
    stroke(0);
    idx = (self.id - 1) % 3
    fill(COLORS[idx][0], COLORS[idx][1], COLORS[idx][2])
    # fill(255,255,0)
    for point in self.spaces:
      pushMatrix()
      translate(point[0]*100,-point[1]*100,point[2]*100)
      box(100)
      popMatrix()
    popMatrix()
