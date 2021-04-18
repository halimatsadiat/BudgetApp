class Budget():
    'Budget Class'
    
    def __init__(self):
        self.categories = {
                'food' : 0,
                'clothing' : 0,
                'entertainment' : 0
            }

    def deposit(self, category, amount):
        if amount > 0:
            self.categories[category] += amount
            return True
        else:
            print('You entered an invalid amount')
            return False

    def withdraw(self, category, amount):
        if amount < 1:
            print ('You entered an invalid amount')
            return False
        if self.categories[category] < amount:
            print('You do not have enough funds in', category, 'category')
            return False
        
        self.categories[category] -= amount
        return True

    def balance(self, category):
        balance = self.categories[category]
        return balance

    def transfer(self, source_cat, dest_cat, amount):
        if self.withdraw(source_cat, amount):
            self.deposit(dest_cat, amount)
            return True
        return False


def get_input(msg):
    try:
        input_value = int(input(msg))
    except:
        print('Invalid selection')
        return False
    return input_value

valid_inputs = [1,2,3,4,5]
categories = {1:'food', 2:'clothing', 3:'entertainment'}
budget = Budget()

def operation():
    global budget
    user_input = get_input('\nPlease select an operation: ')
    
    if user_input == False:
        return 
    
    if not user_input in valid_inputs:
        print('Invalid selection')
        return
        
    if user_input == 1:
        amount = get_input('Please enter an amount: ')
        if amount == False:
            return
        
        print('\nPress 1 to deposit to food category')
        print('Press 2 to deposit to clothing category')
        print('Press 3 to deposit to entertainment category\n')
        
        category = get_input('Please select a category: ')
        if category == False:
            return
        
        if not category in categories:
            print('Invalid selection')
        else:
            if budget.deposit(categories[category], amount) == True:
                print('Deposit successful')

        return
        
    if user_input == 2:
        amount = get_input('Please enter an amount: ')
        if amount == False:
            return
        
        print('\nPress 1 to withdraw from food category')
        print('Press 2 to withdraw from clothing category')
        print('Press 3 to withdraw from entertainment category\n')
        
        category = get_input('Please select a category: ')
        if category == False:
            return
        
        if not category in categories:
            print('Invalid selection')
        else:
            if budget.withdraw(categories[category], amount) == True:
                print('Withdrawal successful')

        return

    if user_input == 3:
        print('\nPress 1 to check the balance of food category')
        print('Press 2 to check the balance of clothing category')
        print('Press 3 to check the balance of entertainment category\n')
        
        category = get_input('Please select a category: ')
        if category == False:
            return
        
        if not category in categories:
            print('Invalid selection')
        else:
            print('Balance in', categories[category], 'category: ',budget.balance(categories[category]))

        return
        
    if user_input == 4:
        amount = get_input('Please enter an amount: ')
        if amount == False:
            return
        
        print('\nPress 1 to select food category')
        print('Press 2 to select of clothing category')
        print('Press 3 to select of entertainment category\n')
        
        source_cat = get_input('Please select the category to transfer from: ')
        if source_cat == False:
            return
        
        if not source_cat in categories:
            print('Invalid selection')
        else:
            dest_cat = get_input('Please select the category to transfer to: ')
            if dest_cat == False:
                return
            
            if not dest_cat in categories:
                print('Invalid selection')
            else:
                if budget.transfer(categories[source_cat], categories[dest_cat], amount) == True:
                    print('Transfer successful')
        return
                
    if user_input == 5:
        return


def actions():
    print('Welcome to Budget app')
    print('Below is the list of available operations')
    print('press 1 for deposit')
    print('press 2 for withdrawal')
    print('press 3 for balance')
    print('press 4 for transfer')
    print('press 5 to exit')
actions()     
operation()

while(True):
    print('\nDo you want to perform another operation?')
    response = input('Enter Y for YES or N for No: ')
    if response.lower() != 'y' and response.lower() != 'n':
        print('Invalid response')
    if response.lower() == 'y':
        actions()
        operation()
    if response.lower() == 'n':
        print('\nBye!')
        break
    
