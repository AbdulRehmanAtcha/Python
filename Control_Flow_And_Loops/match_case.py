a = int(input("Enter Number: "))

match a:
    case 122:
        print("Not matched")
    case 12:
        print("Not matched")
    case 34:
        print("Ohahoohahah! It matches....")
    case _:
        print("Not matches")