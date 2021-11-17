import random
import names as namegen

numberOfCopies = 20
price = 9.99
name = "DOOM"
profit = 0
copiesSold = 0
sold5Copies = False
customers = []
names = []

for i in range(0, 50):
  names.append(namegen.get_first_name())

def sellACopy(copies, customer="Bob"):
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
  randomName = random.choice(names)
  sellACopy(1, customer=randomName)

checkCopies()
print(customers)

print(random.randint(1, 2))