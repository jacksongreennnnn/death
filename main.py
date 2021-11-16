numberOfCopies = 20
price = 9.99
name = "DOOM"
profit = 0
copiesSold = 0
sold5Copies = False
customers = []

def sellACopy(copies, customer="bob"):
  global numberOfCopies, profit, copiesSold, customers
  numberOfCopies -= copies
  profit += (price * copies)
  copiesSold += 1
  customers.append(customer)

def checkCopies():
  if numberOfCopies <= 0:
    print("NOOOOOOOOOOOOOOOOOO")
  else:
    print("We have %d copies of doom" % numberOfCopies)
    print("Our profit is £%.2f" % profit)
  if copiesSold >= 5:
    sold5Copies = True
    print("We sold more than 5 copies")
  
numberOfCopies -= 1
profit += price

checkCopies()

for i in range(0, 5):
  sellACopy(1)

checkCopies()
print(customers)