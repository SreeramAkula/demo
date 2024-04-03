while 1 :
    print("create your account")
    user = input("Enter username")
    pasw = input("Enter password")
    cpasw = input("Enter confirm password")
    if(pasw==cpasw):
        print("your account is created")
        print("login here")
        cuser = input("enter username")
        cpas = input("enter password")
        if(user== cuser and pasw == cpas ):
            print("you are loggedin")
        else:
            print("invalid details")
    else:
        print("password and conform password must be same")