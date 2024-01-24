'error handling'
contact_book = {}
while True:
    print()
    print()
    print("1 Add Contact\n2 View Contact\n3 Edit Contact\n4 Delete Contact\n5 Exit")
    print()
    print()
    try:
        user = int(input("***************** Enter a choice : *****************************\n"))
    except:
         print("Sorry you have typed wrong input\ntype integer")
    else:
        if user == 1:
            print("      *******ADD Contact*******       ")
            print()
            print()
    
            name = input("Enter your name :----->  ")
            try:
                number = int(input("Enter your number :---->  "))
            except:
                print("Sorry you have typed wrong input\ntype integer")
            else:
                contact_book.update({name:number})
    

    
        elif user == 2:
            print("      *******View Contact*******       ")
            print()
            print()
            print()
            if contact_book == {}:
                print('Nothing here!!!\nadd some contact')
            else:
                print()
                print()
                for x,y in contact_book.items():
                    print(f"{x} - {y}")
            
                print()
                print()
    

        elif user == 3:
            print("      *******Edit Contact*******       ")
            print()
            print()
            print()
            print("*****1 Change Name*****\n******2 Change Phone Number*******")
            while True:

                try:
                    choice = int(input("Enter a choice :------>  "))
                except:
                    print('wrong input type an integer')
                else:
                    if choice == 1:
                        for x,y in contact_book.items():
                            print(f"{x} - {y}")
                        old_name = input("Enter a Existing Name :------> ")
                        if old_name in contact_book:
                            number = contact_book[old_name] 
                            contact_book.pop(old_name)
                            new_name = input("Enter a new name :-------> ")
                            contact_book.update({new_name:number})
                            break
                        else:
                            print("This name doesn't Exist")
                    elif choice == 2:
                        for x,y in contact_book.items():
                            print(f"{x} - {y}")
                        person = input("Whose number you want to change :------>  ")
                        if person in contact_book:
                            name = person
                            contact_book.pop(person)
                            while True:
                                try:
                                    new_number = int(input("Enter a new number :----->  "))

                                except:
                                    print("Sorry you have typed wrong input\ntype integer")
                        
                                else:
                                    contact_book.update({name:new_number})
                                    break
                            print('Succesfully added')
                            break   
                        
                        else:
                            print("********This name doesn't Exist**********")
                    else:
                        print("*************Invalid Input***********")


        elif user == 4:
            print("      *******Delete Contact*******       ")
            print()
            print()
            print()
            for x,y in contact_book.items():
                print(f"{x} - {y}")
            ask = input("Whose contact you want to delete :------->  ")
            if ask in contact_book:
                del contact_book[ask]
                print("Successfully removed from your contact book")
            else:
                print("*************This name doesn't Exist**********")


        elif user == 5:
            
            ask_1 = input("*********Do you want to exit from the Contact book*********\ntype yes to exit or no to continue : ")
            if ask_1 == str():
                print('Invalid input')
                continue
                
            elif ask_1 == 'no':
                continue
            elif ask_1 == "yes":
                break
    