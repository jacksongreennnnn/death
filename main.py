numberOfCopies = 20
price = 9.99
name = "DOOM"
profit = 0

def sellACopy(copies):
  global numberOfCopies, profit
  numberOfCopies -= copies
  profit += (price * copies)

def checkCopies():
  if numberOfCopies <= 0:
    print("NOOOOOOOOOOOOOOOOOO")
  else:
    print("We have %d copies of doom" % numberOfCopies)
    print("Our profit is £%r" % profit) 
  
numberOfCopies -= 1
profit += price

checkCopies()

for i in range(0, 19):
  sellACopy(1)

checkCopies()
