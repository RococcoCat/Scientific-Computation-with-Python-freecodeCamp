import numpy as np


def calculate(numbers):

  # raise error if length of inputted numbers > 9
  if len(numbers) != 9:
    raise ValueError( "List must contain nine numbers.")
  # make a list 3x3 list x with input of numbers
  x = [[],[],[]]
  for i in range(3):
    for j in range(3):
      x[i].append(numbers[i*3+j])
  


  a = 0
  b = 0
  means = []
  # gets mean of each axis and flattened
  # appends that to means
  means = []
  for i in range(3):
    if i == 2:
      # flattened
      a = np.mean(x)
      means.append(a)
    else:
      # axis = 0 / 1
      a = np.mean(x,axis=i)
      b = a.tolist()
      means.append(b)
      b = 0
  a = 0
  b = 0
      
  # variance
  varc = []
  for i in range(3):
    if i == 2:
      a = np.var(x)
      varc.append(a)
    else:
      a = np.var(x,axis=i)
      b = a.tolist()
      varc.append(b)
      b = 0
  a = 0
  b = 0
  
  # standard deviation
  stdDev = []
  for i in range(3):
    if i == 2:
      a = np.std(x)
      stdDev.append(a)
    else:
      a = np.std(x,axis=i)
      b  = a.tolist()
      stdDev.append(b)
      b = 0

  # maximum
  maxm = []
  for i in range(3):
    if i == 2:
      a = np.max(x)
      maxm.append(a)
    else:
      a = np.max(x,axis=i)
      b = a.tolist()
      maxm.append(b)
      b = 0

  # minimum
  minm = []
  for i in range(3):
    if i == 2:
      a = np.min(x)
      minm.append(a)
    else:
      a = np.min(x,axis=i)
      b = a.tolist()
      minm.append(b)
      b = 0

  # sum
  sums = []
  for i in range(3):
    if i == 2:
      a = np.sum(x)
      sums.append(a)
    else:
      a = np.sum(x,axis=i)
      b = a.tolist()
      sums.append(b)
      b = 0
  
  output = {'mean': [means[0],means[1],means[2]],
  'variance': [varc[0],varc[1],varc[2]],
  'standard deviation':[stdDev[0],stdDev[1],stdDev[2]],
  'max': [maxm[0],maxm[1],maxm[2]],
  'min': [minm[0],minm[1],minm[2]],
  'sum': [sums[0],sums[1],sums[2]]}
  
  return output
