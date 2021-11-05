from account import Account
class ATM:

  def homeScreen(self):
    print("Welcome to the ATM!")
    user_choice =input("A == Open Account, B == Load Account, C == Deposit, D == Withdraw, E == Exit, F == Check Balance")
    if user_choice == "A":
      name_input = input("What is your name?")
      city_input = input("What city do you live in?")
      type_input = input("What type of account do you want?")
      self.accountList.append(Account(name_input.upper(), city_input, type_input))
      print("Account succesfully created")
      return self.homeScreen()    
    if user_choice == "B":
      name_input = input("What is your name?")
      for account in self.accountList:
        if account.name == name_input.upper():
          self.currentaccount = account
          break
      if self.currentaccount == None:
        print("Account doesn't exist")
      else:     
        print("Account succesfully loaded")
      return self.homeScreen()  
    if user_choice == "C":
      user_input = int (input("How much do you want to deposit?"))
      self.currentaccount.deposit(user_input)
      return self.homeScreen()
    if user_choice == "D":
      user_input = int (input("How much do you want to withdraw?"))
      self.currentaccount.withdraw(user_input)
      return self.homeScreen()
    #if user_choice == "E"
    if user_choice == "F":
      print(self.currentaccount.checkBalance())
      return self.homeScreen()

  def __init__(self, nameOfBank, cityofthebank):
    self.accountList = []
    self.name = nameOfBank
    self.city = cityofthebank
    self.currentaccount = None
