
import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Starting with $100 balance
    
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)
    
    try:
        # Parse command and amount
        command, *params = sys.argv[1].split(':')
        amount = float(params[0]) if params else None
        
        # Execute commands
        if command == "deposit" and amount is not None:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        elif command == "withdraw" and amount is not None:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        elif command == "display":
            account.display_balance()
        else:
            print("Invalid command or missing amount.")
            
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")

if __name__ == "__main__":
    main()
