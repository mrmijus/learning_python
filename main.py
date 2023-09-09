from typing import Literal
expenses = []


# TODO: Create function that will add a new expense to the list of expenses
# TODO: Create a function that will remove an expense from the list of expenses
# TODO: Add user input in the main function that will choose which function to call

def _create_mock_expenses():
    random_expense_1 = {"type": 'food', "amount": 100, "description": 'sastojsci za mazalicu'}
    random_expense_2 = {"type": 'food', "amount": 2130, "description": 'pivo za vikend'}
    random_expense_3 = {"type": 'food', "amount": 12410, "description": 'meso za rostilj'}
    random_expense_4 = {"type": 'rent', "amount": 1000, "description": 'racun za avgust'}
    random_expense_5 = {"type": 'pussy', "amount": 300, "description": 'kondomi i lubrikanti'}

    expenses.append(random_expense_1)
    expenses.append(random_expense_2)
    expenses.append(random_expense_3)
    expenses.append(random_expense_4)
    expenses.append(random_expense_5)


def calculate_total_expenses():
    total = 0
    for item in expenses:
        total += item['amount']
    print(f"You total expenses are: {total}")


def calculate_total_expenses_by_type(expense_type: Literal['food', 'rent', 'pussy']):
    total = 0
    for item in expenses:
        if item["type"] == expense_type.lower():
            total += item['amount']
    print(f"Your total expenses for {expense_type} are: {total}")


def main():
    _create_mock_expenses()
    print("Welcome to your expenses tracker")
    print("1. Calculate total expenses")
    print("2. Calculate total expenses by type")
    print("3. Add new expense")

    user_input = input("Please enter your choice: ")
    
    
main()
