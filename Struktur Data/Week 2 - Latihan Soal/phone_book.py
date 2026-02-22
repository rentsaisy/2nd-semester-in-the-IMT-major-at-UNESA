def phone_book():
    contacts = {}
    
    while True:
        print("\n=== PHONE BOOK MENU ===")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display All Contacts")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            contacts[name] = number
            print(f"Contact '{name}' added successfully.")
        
        elif choice == "2":
            name = input("Enter name to search: ")
            if name in contacts:
                print(f"{name} -> {contacts[name]}")
            else:
                print("Contact not found.")
        
        elif choice == "3":
            if contacts:
                print("\n--- Contact List ---")
                for name, number in contacts.items():
                    print(f"{name} -> {number}")
            else:
                print("No contacts available.")
        
        elif choice == "4":
            print("Exiting Phone Book. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select 1-4.")

# Run the program
phone_book()