class Rectangle:
  import re
  def __init__(self, width, height):
    self.width = width
    self.height = height
    
  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    area = self.width * self.height
    return area

  def get_perimeter(self):
    perimeter = 2 * self.width + 2 * self.height
    return perimeter

  def get_diagonal(self):
    diagonal = (self.width ** 2 + self.height ** 2) ** .5
    return diagonal

  def get_picture(self):
    picture = ""
    error = "Too big for picture."
    if self.width > 50 or self.height > 50:
      return error
    for i in range(self.height):
      picture += self.width * "*" + "\n"
    print(picture)
    return picture
        

  def get_amount_inside(self, shape):
    numW = int(self.width / shape.width)
    numH = int(self.height / shape.height)
    num = numW * numH
    return num

  def __str__(self):
    return (("Rectangle(width={0}, height={1})").format(self.width, self.height))
  


class Square(Rectangle):
  width = 0
  height = 0
  
  def __init__(self, width):
    self.width = width
    self.height = width
    
  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, width):
    self.width = width
    self.height = width

  def set_height(self, height):
    self.height = height
    self.width = height
    
  def __str__(self):
    return (("Square(side={0})").format(self.width))
