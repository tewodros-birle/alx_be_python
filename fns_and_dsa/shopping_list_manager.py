def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # This is the array implementation
    
    while True:
        display_menu()  # Calling the display_menu function
        
        try:
            choice = int(input("Enter your choice (1-4): "))  # Ensuring input is a number
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
            
        if choice == 1:
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' added to your shopping list.")
            
        elif choice == 2:
            if len(shopping_list) == 0:
                print("Your shopping list is empty!")
                continue
                
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from your shopping list.")
            else:
                print(f"'{item}' not found in your shopping list.")
                
        elif choice == 3:
            if len(shopping_list) == 0:
                print("Your shopping list is empty!")
            else:
                print("\nCurrent Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
                    
        elif choice == 4:
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
