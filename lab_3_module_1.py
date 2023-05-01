""""crowd-funding app"""
import re
import os   
print("Hello dear, Welcome in Crowd-Funding App ! ")

# function to check firstname
def fname_check():
    global fname
    fname = input("Enter your firstname: ")
    if fname.strip() == "":
        print("Invalid: firstname cannot be empty")
        fname_check()
    else:
        print("perfect ..!")
        return fname

# function to check lastname
def lname_check():
    global lname
    lname = input("Enter your lastname: ")
    if lname.strip() == "":
        print("Invalid: lastname cannot be empty")
        lname_check()
    else:
        print("perfect ..!")
        return lname

# function to check valid email
def emailcheck():
    global email
    email = input("Enter your e-mail: ")
    emailregex =  r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(emailregex, email):
        print("perfect..! ")
        return email
    else:
        print("Invalid Email")
        emailcheck()

# function to input the password
def password_check():
    global password
    password = input("Enter your password: ")
    if password.strip() == "":
        print("Invalid: Password cannot be empty")
        password_check()
    else:
        print("perfect ..!")
        return password


# function to check password confirmation
def confirm_password():
    global password
    confirmpassword = input("Confirm your password confirmation:  ")
    if confirmpassword == password:
        print("perfect..! ")
    else:
        print("""wrong password confirmation..!""")
        reinputpass = input("if you want to re inptut the password type 'try' if you want confirm password again type 'no' ..! ")
        if reinputpass == "try":
            print("kindly input the new password ...!")
            password_check()
        else:
            confirm_password()

# function to check mobile number
def phone_number_check():
    global phone_number
    phone_number = input("Enter your phone number:  ")
    phoneregex = r'^01[0125][0-9]{8}$'
    if re.match(phoneregex, phone_number):
        print("perfect...!")
        return phone_number
    else:
        print("This phone number is not egyptian number, kindly input an egyptian phone number ...!")
        phone_number_check()



def append_data():
    try:
        fileobject = open("database.txt", 'a')
    except Exception as e:
        print(e)
    else:
        fileobject.write(fname + ":" + lname + ":" + email + ":" + password + ":" + phone_number + "\n")
        fileobject.close()


 # function to check password
def password_login():
    i = 0
    try:
        fileobject = open("database.txt", 'r')
    except Exception as e:
        print(e)
    else:
        fileobject.seek(0)
        linesnum = len(fileobject.readlines())
        fileobject.seek(0)
        while i <= linesnum :
            line = fileobject.readline()
            fields = line.split(':')
            data_pass = fields[3]
            if password == data_pass:
                print("correct password..!, Welcome back :):) ")
                break
               # can do some actions like create funding
            else:
                i+=1
                continue
        else:  # this part of code issued
            print("error: you entered invalid password .., Try again!")
            password_check()
            password_login()





# function to check the login email and if it is right will check login password
def logincheck():
    global i
    print("Welcome in Crowd-Funding App !, let's login ... :)  ")
    i = 0
    emailcheck()
    try:
        fileobject = open("database.txt", 'r')
    except Exception as e:
        print(e)
    else:
        fileobject.seek(0)
        linesnum = len(fileobject.readlines())
        fileobject.seek(0)
        while i <= linesnum :
            line = fileobject.readline()
            fields = line.split(':')
            #print(fields)
            data_email = fields[2]
            if email == data_email:
                print("correct email.. :) ")
                fileobject.close()
                password_check()
                password_login()
                break
            else:
                i+=1
                continue
                return i
        if i > linesnum: # this part of code issued
            print("error: you entered invalid E-mail ..!")
            logincheck()




def create_account():
    fname_check()
    lname_check()
    emailcheck()
    password_check()
    confirm_password()
    phone_number_check()
    append_data()
    logincheck()




# function to check if the user want to login or signup
def choose():
    want = input("if you want to login type 'login' or to create accout type 'signup' :  ")
    if want == "login" :
        logincheck()
    elif want == "signup" :
        create_account()
    else:
        print("error: kindly enter a valid input ..! ")
        choose()




