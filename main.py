numberOfCopies = 20
price = 9.99
name = "DOOM"
profit = 0

def sellACopy(copies):
  global numberOfCopies, profit
  numberOfCopies -= copies
  profit += (price * copies)

numberOfCopies -= 1
profit += 9.99

print("We have %d copies of doom" % numberOfCopies)
print("Our profit is £%r" % profit)

sellACopy(3)
print("We have %d copies of doom" % numberOfCopies)
print("Our profit is £%r" % profit)