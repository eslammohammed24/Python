contacts = {
    1 : {
        "name" : "Eslam",
        "number" : 1234,
        "address" : "Giza"
    },
    2 : {
        "name" : "Mohamed",
        "number" : 56789,
        "address" : "cairo"
    },
    3 : {
        "name" : "Ahmed",
        "number" : 56854,
        "address" : "Alex"
    }
}

# Creating a menu display
def showMenu():
    print("Welcome to Contact Books. What do you want to do?")
    print("1. View contact")
    print("2. Change contact")
    print("3. Add contact")
    print("4. Delete contact")
    print("5. Exit")

    selectMenu()

def selectMenu():
    repeat = True
    while repeat == True:
        try:
            option = int(input("Choose[1-5]: "))
        except ValueError:
            print("Please input number.")
            # fill the option with value so the program won't error
            option = 0
        if option > 0 and option < 6: repeat = False
        if option == 1:
            showContacts()
            showMenu()
        elif option == 2:
            print("\n==============")
            print("Change Contact")
            print("==============")
            #updateContact()
            #showMenu()
        elif option == 3:
            print("\n===========")
            print("Add Contact")
            print("===========")
            #addContact()
            #showMenu()
        elif option == 4:
            #deleteContact()
            #showMenu()
            print("4 selected")
        elif option == 5:
            print("Good bye!")
            break
        else: 
            print("Option unavailable.")

def showContacts():
    # manual numbering 
    num = 1
    print("================================================================================")
    print("|No.| Name            | Number           | Address:                            |")
    print("================================================================================")
    for contact in contacts.values():
        # format to left-align and give some spacing
        print("|{no} .| {name:<15} | {number:<15}  | {address:<35} |"
        .format(no = num, name = contact["name"], 
                number = contact["number"], address = contact["address"]))
        num += 1
    print("================================================================================")

showMenu()
