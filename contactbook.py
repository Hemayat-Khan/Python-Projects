# Save contact in file
def save_contact(name, phone, email, address):
    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone},{email},{address}\n")
    print("Contact saved successfully!\n")

# View contacts from file
def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("Contact book is empty!\n")
                return
            print("\n--- Contact Book ---")
            for contact in contacts:
                name, phone, email, address = contact.strip().split(',')
                print(f"Name: {name}")
                print(f"Phone: {phone}")
                print(f"Email: {email}")
                print(f"Address: {address}")
                print("-" * 20)
    except FileNotFoundError:
        print("No contacts found. File not created yet.\n")

# Main menu
def main():
    while True:
        print("\n📒 Contact Book Menu (.txt version)")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            save_contact(name, phone, email, address)

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

main()

    