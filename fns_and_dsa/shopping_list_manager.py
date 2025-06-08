# this script use lists to create a simple shopping list manager,
# that allows users to add items, view the current list, and remove items.

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item you want to add: ").strip()
            # add user item to shopping list
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.\n")
        
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item you want to remove: ").strip()
            # remove user item from shopping list
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from your shopping list\n")
            else:
                print(f"'{item}' was not found in your shopping list\n")
        
        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}\n")
            else:
                print("The shopping list is empty.\n")

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

