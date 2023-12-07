class Atm:    
    #constructor
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()
        
    def menu(self):
        user_input = input("""
        Hi. How can I help You?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check Balance
        4. Press 4 to withdraw    
        5. Anything else to exit      
        """)
        if user_input == '1':
            return self.create_pin()
        elif user_input == '2':
            return self.change_pin()
        elif user_input == '3':
            return self.check_balance()
        elif user_input == '4':
            return self.withdraw()
        else:
            exit()
            
    def create_pin(self):
        user_pin = input('enter your pin')
        confirm_pin = input('enter your pin again')
        if user_pin == confirm_pin:
            print("Pin created successfully")
            self.pin = user_pin
            self.enter_balance()
            self.menu()
        else:
            print("Pin and confirm pin doesn't match Try again")
            self.create_pin()
            
    def enter_balance(self):
        user_balance = int(input("Enter Your Balance"))
        self.balance = user_balance
        
    def change_pin(self):
        user_pin_verification = input("Enter your pin")
        if user_pin_verification == self.pin:
            self.create_pin()
        else:
            print('Wrong pin')
            self.change_pin()
    
    def check_balance(self):
        user_pin = input("Enter your pin")
        if user_pin == self.pin:
            print('Your available balance Rs',self.balance)
            self.menu()
        else:
            print('Wrong pin Try again!')
            self.check_balance()
        
    def withdraw(self):
        user_pin = input('Enter your pin')
        if user_pin == self.pin:
            amount_withdraw = int(input('Enter the amount you want to withdraw'))
            if amount_withdraw < self.balance:
                self.balance -= amount_withdraw
                print('sucessfully withdraw')
                print('Available balance Rs',self.balance)
            else:
                print('Your account have insufficient fund')
                self.withdraw()
        else:
            print('Wrong pin')
            self.withdraw()
            
obj = Atm()
