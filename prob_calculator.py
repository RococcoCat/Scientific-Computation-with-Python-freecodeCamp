import copy
import random
import re
# Consider using the modules imported above.

class Hat:
  
  def __init__(self, **kwargs):
    self.balls = kwargs
    self.contents = []    
    for key, value in self.balls.items():
      for i in range(value):
        self.contents.append(key)
  
  def draw(self, number):
    drawn = []
    n = 0
    if number > len(self.contents):
      return self.contents
    if len(self.contents) > 0:
      for i in range(number):
        n = random.randrange(len(self.contents))
        drawn.append(self.contents.pop(n))
      drawn.sort()
    return(drawn)
    
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

  # something wrong w/ hat copy, draw() keeps modifying original hat. fucks shit up
  prob = 0
  result = []
  success = 0
  count = 0
  req = 0 
  # expected balls is a dict
  # loop thru num experiments : performing this many experiments
  # draw num balls
  # each time, loop thru expected and check
  # if both con. met, success += 1
  # divide success by num_experiments
  for i in range(num_experiments):
    hatc = copy.deepcopy(hat)
    result = hatc.draw(num_balls_drawn)
    req = 0
    for key, value in expected_balls.items():
      count = 0
      for j in result:
        if j == key:
          count += 1
        if count >= value:
          req = req + 1
          break
      if req == len(expected_balls):
        success += 1
        
  prob = success / num_experiments
  return prob