from typing import Literal

expenses = []


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


def add_new_expense(new_expense_type: str, new_expense_amount: int, new_expense_description: str):
    new_expense = {"type": new_expense_type, "amount": new_expense_amount, "description": new_expense_description}
    expenses.append(new_expense)
    print(
        f"New expense with type {new_expense_type}, amount {new_expense_amount} and description "
        f"{new_expense_description} is added to the expenses dictionary.")


def remove_expense(existing_type: Literal['food', 'rent', 'pussy']):
    print(
        f"Would you like to remove all expenses with type {existing_type}, or one specific expense?\n 1. All expenses "
        f"with type {existing_type}\n 2. One specific expense")
    user_choice = input("Please enter your choice:")
    if user_choice == "1":
        for expense in expenses:
            if expense["type"] == existing_type.lower():
                expenses.remove(expense)
        print(f"All expenses with type {existing_type} are removed.")
    elif user_choice == "2":
        for all_expenses in expenses:
            if all_expenses["type"] == existing_type.lower():
                print(all_expenses["description"])
        existing_description = input("Based on a description, what would you like to remove?")
        for get_expense_description in expenses:
            if get_expense_description["description"].lower() == existing_description.lower():
                expenses.remove(get_expense_description)
            else:
                raise Exception("Invalid expense description. Restart the program and try again")
        print(f"All expenses with type {existing_type} and description {existing_description} are removed.")
        print(expenses)
    else:
        raise Exception("Input not valid.")


def calculate_total_expenses_by_type(expense_type: Literal['food', 'rent', 'pussy']):
    total = 0
    for item in expenses:
        if item["type"] == expense_type.lower():
            total += item['amount']
    print(f"Your total expenses for {expense_type} are: {total}")


def main():
    _create_mock_expenses()
    program_run = True
    print("Welcome to your expenses tracker")

    while program_run:
        print("1. Calculate total expenses")
        print("2. Calculate total expenses by type")
        print("3. Add new expense")
        print("4. Remove existing expense")
        print("5. Exit program")
        user_input = input("Please enter your choice: ")
        if user_input == "1":
            calculate_total_expenses()
        elif user_input == "2":
            expense_type = input("Please chose type of the expense:")
            calculate_total_expenses_by_type(expense_type)
        elif user_input == "3":
            new_expense_type = input("What is the type of the expense?")
            new_expense_amount = int(input("What is the expense amount?"))
            new_expense_description = input("Fill in the description of new expense:")
            add_new_expense(new_expense_type, new_expense_amount, new_expense_description)
        elif user_input == "4":
            existing_type = input("What type of an expense you would like to remove?")
            remove_expense(existing_type)
        elif user_input == "5":
            print("Goodbye.")
            program_run = False
        else:
            raise Exception("Please restart the program and choose one number from the list above.")


main()

