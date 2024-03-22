stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()

# Type your code below
count = 0
numbers = stdform.replace(".","").replace("x","").replace("^","").replace("-","")
for i in range(len(str(stdform))):
  if stdform[i] in (".", "x", "^"):
      count = count + 1
if count != 3 or numbers.isdigit() == False:
  print('Error converting to scientific E notation.')
else:
    enotation = stdform.replace('x10^', 'E')
    print('This number in E notation is ' + enotation + '.')