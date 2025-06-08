def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Array implementation
    
    while True:
        display_menu()  # Function call
        
        choice = input("Enter your choice: ")  # Choice input
        
        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"Item added: {item}")
            
        elif choice == '2':
            if not shopping_list:
                print("The list is empty!")
                continue
                
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Item removed: {item}")
            else:
                print("Item not found!")
                
        elif choice == '3':
            if not shopping_list:
                print("The list is empty!")
            else:
                print("Current Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
                    
        elif choice == '4':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
