Names = []
Phone_numbers = []
Address = []
print("-----CONTACT_BOOK-----")
num = 3
for i in range(num):
    name = input("Enter Name: ")
    phone_number = input("Enter Phone Number: ")
    address = input("Enter your Address: ")
    Names.append(name)
    Phone_numbers.append(phone_number)
    Address.append(address)
print(f"\tNames\t\t\tPhone_numbers\t\t\t\tAddress")
for i in range(num):
        print(f"\t{Names[i]}\t\t\t{Phone_numbers[i]}\t\t\t\t{Address[i]}")

while True:
    print("1. Add")
    print("2. search")
    print("3. Update")
    print("4. Delete")
    print("5. View")
    print("6. exit/stop")

    choice = input("Enter your choice: ")
    
    if choice == "1":
       name = input("Enter name: ")
       phone_number = input("Enter phone number: ")
       address = input("Enter your address: ")
       Names.append(name)
       Phone_numbers.append(phone_number)
       Address.append(address)
       print(f"Name:{name}, Phone Number:{phone_number}, Address:{address}")

    elif choice == "2":
        search = input("Enter the name to search: ")
        if search in Names:
            index = Names.index(search)
            name = Names[index]
            phone_number = Phone_numbers[index]
            address = Address[index]
            print(f"Name:{name},Phone Number:{phone_number},Address:{address}")
        else:
            print("Name not found!")

    elif choice == "3":
        update = input("Enter name  you want to update: ")
        if update in Names:
            index = Names.index(update)
            Names[index] = input("enter new name: ")
            Phone_numbers[index] = input("enter new phone no.: ")
            Address[index]= input("enter new address: ")
            print(f"Updated Name:{Names[index]},Updated Phone Number:{Phone_numbers[index]},Updated Address:{Address[index]}")
        else:
            print(" Name not found!")

    elif choice == "4":
        delete = input("which name/phone_no/address you want to delete = ")
        if delete in Names:
            index = Names.index(delete)
            del Names[index]
            del Phone_numbers[index]
            del Address[index]
            print(f"Contact has been deleted..")
        else:
            print("Contact not found!")
    elif choice == "5":
        for i in range(len(Names)):
            print(f"Name:{Names[i]}, Phone Number:{Phone_numbers[i]}, Address:{Address[i]}")

    elif choice == "6":
        print("closing the contact_book..")
        break
    else:
        print("not found!")



