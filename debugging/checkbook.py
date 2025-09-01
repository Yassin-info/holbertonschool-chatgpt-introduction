class Checkbook:
    def __init__(self):
        """Initialize the checkbook with a zero balance."""
        self.balance = 0.0

    def deposit(self, amount):
        """Deposit the given amount to the balance."""
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """Withdraw the given amount from the balance if funds are sufficient."""
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Print the current balance."""
        print("Current Balance: ${:.2f}".format(self.balance))

def get_valid_amount(prompt):
    """
    Prompt the user for a monetary amount and validate the input.
    Returns a float if valid, or None if invalid.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive amount.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            amount = get_valid_amount("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = get_valid_amount("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
