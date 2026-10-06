from datetime import datetime
dt = datetime.now()


class Journal():

    def __init__(self):
        try:
            file = open("journal.txt","x")
            file.close()
        except:
            print("File already exists! ")

    def add_entry(self):
        try:
            file = open("journal.txt","a")
            data_entry = input("Enter your journal entry: ")
            file.write(data_entry + " " + str(dt) + "\n")
            file.close()
            print("\nEntry Added Successfully!")
        except:
            print("Something went wrong!")

    def view_entries(self):
        try:
            file = open("journal.txt","r")
            data = file.read()
            file.close()
            print("\nYour Journal Entries: ")
            if data == "":
                print("No Entries are found!")
            else:
                print(data)
                print("All Details")
        except:
            print("Something went wrong! ")

    def search_entry(self):
        try:
            file = open("journal.txt","r")
            data = file.readlines()
            file.close()
            entry = input("Enter a keyword: ")
            for i in data:
                if entry.lower() in i.lower():
                    print(i)
        except:
            print("Something went wrong! ")

    def delete_entries(self):
        try:
            confirm = input("\nAre you sure you want to delete all entries? (yes/no): ")
            if confirm.lower() == "yes":
                file = open("journal.txt", "w")
                file.write("")
                file.close()
                print("\nAll journal entries have been deleted.")
            else:
                print("\nDelete operation cancelled.")
        except:
            print("Something went wrong!")


obj = Journal()

while True:
    print("\nWelcome to Personal Journal Manager!")
    print("Select an option:")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        obj.add_entry()

    elif choice == 2:
        obj.view_entries()

    elif choice == 3:
        obj.search_entry()

    elif choice == 4:
        obj.delete_entries()

    elif choice == 5:
        print("Thank You for using Personal Journal Manager. Goodbye!")
        break
    
    else:
        print("Invalid Choice!")
