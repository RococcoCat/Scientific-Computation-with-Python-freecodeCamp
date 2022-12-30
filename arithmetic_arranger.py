def arithmetic_arranger(problems, display = False):
  import re
  prob = []
  numbers = []
  answers = []
  a_prob = ""
    # extracts #s and operators from problems
    # prob is a list of strings (#s and operators)
  for i in problems:
    prob.append(re.findall(r'[0-9]*\S',i))
 # Error 1: no more than 5 problems:
  if len(prob) > 5:
    error_message1 = 'Error: Too many problems.'
    return error_message1       
    
    # extracts #s from prob
    # numbers is a list of strs of the #s 
  for i in prob:
    x = []
    x.append(i[0])
    x.append(i[2])
    numbers.append(x)

  # Error 3: no digits in the number
  # Error 4: number can't be more than 4 digits    
  error_message3 = 'Error: Numbers must only contain digits.'
  error_message4 = 'Error: Numbers cannot be more than four digits.'
    
  for i in numbers:
    for j in i:
      if not j.isdigit():
        return error_message3
      if len(j) > 4:
        return error_message4
        
  # extracts operators from prob
  operators = []
  for i in prob:
    operators.append(i[1])
  # Error 2: wrong operators
  wrong_op = ['*','/']
  error_message = "Error: Operator must be '+' or '-'."
  for i in wrong_op:
    if i in operators:
      return error_message
# if display is True, displays answers
    # calculate answers
  x = 0
  if display:
    for i in range(len(numbers)):
      if operators[i] == '+':
        x = int(numbers[i][0]) + int(numbers[i][1])
      elif operators[i] == '-':
        x = int(numbers[i][0]) - int(numbers[i][1])
      answers.append(x) 
    
    
    # gets the longest # in numbers
    # longest_nums is a list of the #s (int)
  longest = 0
  longest_nums = []
  for i in range(len(numbers)):
    longest = int(numbers[i][0])
    for j in range(len(numbers[i])):
      if abs(int(numbers[i][j])) > longest:
        longest = int(numbers[i][j])
    longest_nums.append(longest)

    # still need to arrange prob w/ apropriate # of spaces and /n and bottom dashes
        # single space btw operator and the longest of the 2
        # same order: 1st on top, 2nd on botton
        # right aligned
        # 4 spaces btw each prob

    # finds the max length that each prob. is going to be (longest + 2)
    # lengths is a list of ints. of the max lengths
  lengths = []
  for i in  range(len(longest_nums)):
    lengths.append(len(str(longest_nums[i])) + 2)

    # arrange problems
    # top = (length - 1st #) x spaces + 1st #
    # bottom = operator + (length - (2nd # + 1)) x spaces + 2nd #
    # line = length x - 
  top = ""
  bottom = ""
  line = ""
  answer_line = ""
  for i in range(len(prob)):
    top = top + ((lengths[i] - len(prob[i][0])) * " ") + prob[i][0]
    bottom = bottom + operators[i] + ((lengths[i] - (len(prob[i][2]) + 1)) * " ") + prob[i][2] 
    line = line  + lengths[i] * "-"
    if i == (len(prob) - 1):
      top = top + "\n"
      bottom = bottom + "\n"
      if display:
        line = line + "\n"
    else:
      top = top + (4 * " ")
      bottom = bottom + (4 * " ")
      line = line + (4 * " ")
  if display:            
    for i in range(len(answers)):
      answer_line = answer_line + (lengths[i] - len(str(answers[i]))) * " " + str(answers[i])
      if not i == (len(answers) - 1):                       answer_line = answer_line + (4 * " ")
                
  arranged_problems = top + bottom + line + answer_line 
  return arranged_problems