import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("budget_tracker.log"),
        logging.StreamHandler()
    ]
)

def get_budget_input() -> float:
    """
    Prompts the user to input their budget for the month.

    Returns:
        float: The monthly budget amount entered by the user.
    
    Raises:
        ValueError: If the input is not a valid float or a negative value.
    """
    while True:
        try:
            budget = float(input("Please enter your amount budgeted for the month: $"))
            if budget < 0:
                raise ValueError("Budget cannot be negative.")
            return budget
        except ValueError as e:
            logging.error(f"Invalid budget input: {e}")
            print(f"Invalid input. Please enter a valid positive number for the budget.")

def get_expense_input() -> float:
    """
    Prompts the user to input an expense amount.

    Returns:
        float: The expense amount entered by the user.
    
    Raises:
        ValueError: If the input is not a valid float or a negative value.
    """
    while True:
        try:
            expense = float(input("Enter your expenses or enter 0 to quit: $"))
            if expense < 0:
                raise ValueError("Expense cannot be negative.")
            return expense
        except ValueError as e:
            logging.error(f"Invalid expense input: {e}")
            print(f"Invalid input. Please enter a valid positive number for the expense.")

def calculate_budget_status(budget: float, total_expenses: float) -> str:
    """
    Determines the budget status based on the comparison between budget and total expenses.

    Args:
        budget (float): The amount budgeted for the month.
        total_expenses (float): The total expenses entered by the user.
    
    Returns:
        str: A message indicating whether the user is under budget, over budget, or matches the budget.
    """
    if budget > total_expenses:
        return f"You are ${budget - total_expenses:,.2f} under budget. WELL DONE!"
    elif budget < total_expenses:
        return f"You are ${total_expenses - budget:,.2f} over budget. PLAN BETTER NEXT TIME!"
    else:
        return "Spending matches your budget. GOOD PLANNING!"

def main():
    """
    Main function to track the user's expenses and compare them with their budget.
    """
    try:
        # Get the budget and track expenses
        budget = get_budget_input()
        total_expenses = 0

        while True:
            expense = get_expense_input()
            if expense == 0:
                break
            total_expenses += expense

        # Display results
        print(f"Budgeted: ${budget:,.2f}")
        print(f"Expenses: ${total_expenses:,.2f}")
        print(calculate_budget_status(budget, total_expenses))

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
