class Category:
  category = ""
  balance = 0
  ledger = []
    
  def __init__(self, category):
      self.category = category
      self.ledger = []
        
  def check_funds(self, amount):
    if amount <= self.balance:
      return True
    else:
      return False
        
  def deposit(self, amount, description = ""):
    self.balance = self.balance + amount
    self.ledger.append({"amount": amount, "description": description})


  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      self.balance += -amount
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def get_balance(self):
    return self.balance

  def transfer(self, amount, destination):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + destination.category)
      destination.deposit(amount, "Transfer from " + self.category)
      return True
    else:
      return False
  def  __str__ (self):
    # draw line w/ 30 * and category name centered
    line = ""
    items = []
    spent = []
    entry = ""
    output = ""
    nameLen = len(self.category)
    if nameLen % 2 == 0:
      line = int(15 - nameLen/2) * "*" + self.category + int(15 - nameLen/2) * "*"
    else:
      line = int((30 - nameLen)/2) * "*" + self.category + int((30 - nameLen)/2) * "*"
    for j in self.ledger:
      if len(j["description"]) <= 23:
        items.append(j["description"])
      else:
        items.append(j["description"][:23])
      x = format(j["amount"],".2f")
      if len(x) <= 7:
        spent.append(x)
      else:                  
        spent.append(x[:7])
    for i in range(len(items)):
      entry = entry + items[i] + (30 - (len(items[i]) + len(spent[i]))) * " " + spent[i] + "\n"
    output = line + "\n" + entry + "Total: " + str(self.balance)
    return output
    
def create_spend_chart(categories):
  
    # categories: list of categories
    # show percentage spent in each category
    # % calc only w/ withdrawals
    # width of chart determined by # of categories
    # each category 3 spaces + 1 for ending

  title = "Percentage spent by category\n"
  width = len(categories) * 3
  graph = ""
  total = 0
  values = []
    
    # calculate percentages by amount spent in each category
    # calculate by withdrawals
  percentages = []
  w = 0
  withdrawals = []
  percent = 0
  for i in categories:            # goes thru categories and adds withdrawals to a list
    for j in i.ledger:
      if j["amount"] < 0:
        w = j["amount"]
    withdrawals.append({i.category: w})
        
  for i in withdrawals:
    for key in i:
        total += i[key]

  import math
    
  for i in withdrawals:           # calculate percentages spent
    for key in i:
      if -int(i[key]) >= 10:
        percent = (-int(i[key])/ total) * 100
        percent = int(percent/10) * 10
        percentages.append({str(key): percent})   
      else:
        percent = 0
        percentages.append({str(key): percent})
        
  graph = []
  line = ""
  graphstr = ""
  dot = 0

    # creates empty graph
  for i in range(100,-1,-10):
    if len(str(i)) == 3:
      line = str(i) + "|" 
    elif len(str(i)) == 2:
      line = " " + str(i) + "|" 
    else:
      line = "  " + str(i) + "|" 
    graph.append(line)
    
    # drawing o by row
  count = 0
  chart = 110
  pline = ""
  for j in range(len(graph)):
    chart -= 10
    count = 0
    pline = ""
    for i in percentages:
      count += 1
      for key in i:
        if -i[key] >= chart:
          pline += " o "
        else:
          pline += "   "
      if count == len(percentages):
        pline += "\n"
    graph[j] = graph[j] + pline
    # drawing the line under the graph
  dotted_line = 5 * " " + width * "-" + "\n"
  graph.append(dotted_line)
    
    # writing the names of the category

    # making a list with the names
  names = []
  for i in percentages:
    for key, value in i.items():
      names.append(key)

    # writing the names of the categories
  linel = ""
  longest = 0
  for i in names:
    if len(i) > longest:
      longest = len(i)

  countn = 0
  
  for j in range(longest): # column
    linel = "    "
    countn = 0
    for i in names: # row
      countn += 1
      if j < len(i):
        linel += " " + i[j:j+1] + " "
      else:
        linel += "   "
      if countn == len(names) and j != longest-1:
        linel += "\n"      
                
    graph.append(linel)
        
  graph.insert(0,title)
  
  graphstr = ""
  for i in graph:
    graphstr +=  i
  print(graphstr)
  return graphstr
  



















