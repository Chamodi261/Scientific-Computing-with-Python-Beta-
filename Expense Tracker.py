def add_expense(expenses, amount, category):
    """
    Adds a new expense to the list of expenses.

    Parameters:
        expenses (list): List of expenses.
        amount (float): The amount of the expense.
        category (str): The category of the expense.
    """
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):
    """
    Prints all expenses in a formatted manner.

    Parameters:
        expenses (list): List of expenses.
    """
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    """
    Calculates the total amount of all expenses.

    Parameters:
        expenses (list): List of expenses.

    Returns:
        float: Total amount of expenses.
    """
    return sum(map(lambda expense: expense['amount'], expenses))
    
def filter_expenses_by_category(expenses, category):
    """
    Filters expenses based on a given category.

    Parameters:
        expenses (list): List of expenses.
        category (str): The category to filter.

    Returns:
        filter: Filtered expenses.
    """
    return filter(lambda expense: expense['category'] == category, expenses)

def main():
    """
    Main function to manage the expense tracker program.
    """
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)

        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))

        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)

        elif choice == '5':
            print('Exiting the program.')
            break

# Run the main function
main()
