class Account:

  def deposit(self, depositamount):
    self.currentBalance += depositamount 
  def withrdraw(self, withdrawAmount):
    if withdrawAmount > self.currentBalance:
      print("thats too much")
    else: 
      self.currentBalance -= withdrawAmount
  def checkBalance(self):
    return self.currentBalance
  def __init__(self,name,city, isChecking):
    self.name = name  
    self.city = city 
    self.isChecking = isChecking
    self.currentBalance = 0

