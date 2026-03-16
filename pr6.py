from datetime import datetime


class Manager:
    def __init__(self):
        pass

    def add_entry(self):
        self.now = datetime.now().strftime("%d-%m-%y %H:%M:%S")
        self.entry = input("enter your journal entry: ")
        with open("journal.txt", "a") as f:
            f.write(f"date: {self.now}\n")
            f.write(f"entry: {self.entry}\n")
            f.write(f"-------------------------------\n")
        print("journal entry added successfully")

    def view_all_entry(self):
        try:
            with open("journal.txt", "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("no (journal.txt) file found ")

    def search_entry(self):
        keyword = input(" Enter keyword to search: ")
        found = False
        with open("journal.txt", "r") as f:
            entries = f.read().split("--------------------------------")
            for entry in entries:
                if keyword.lower() in entry.lower():
                    print(entry.strip())
                    print("------------------------------")
                    found = True
        if not found:
            print(" No entry found with that keyword.")

    def delete_all_entries(self):
        self.confirm = input("are you sure to delete all entries (yes/no): ").lower()
        if self.confirm == "yes":
            with open("journal.txt", "w") as f:
                pass
                print("delete all entries successfully ")
        else:
            print("plase enter correct confirmation ")


m1 = Manager()


while True:
    print(" Welcome to Personal Journal Manager!")
    print("1. Add a new entry")
    print("2. View all entries")
    print("3. Search for an entry")
    print("4. Delete all entries")
    print("5. Exit")

    try:
        option = int(input(" Please select an option (1-5): "))
        match option:
            case 1:
                m1.add_entry()
            case 2:
                m1.view_all_entry()
            case 3:
                m1.search_entry()
            case 4:
                m1.delete_all_entries()
            case 5:
                print(" Exiting... Goodbye!")
                break
    except ValueError:
        print(" Please enter a valid number.")