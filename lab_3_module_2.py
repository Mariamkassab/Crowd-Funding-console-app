import re
import datetime
import lab_3_module_1 as mod1

print("Hello dear, Welcome in Crowd-Funding projects ! ")

# function for getting a title for the new project
def project_title():
    global title
    title = input("Enter your project title: ")
    if title.strip() == "":
        print("Invalid: project title cannot be empty")
        project_title()
    else:
        print("perfect ..!")
        return title

# function for getting details for the new project
def project_details():
    global details
    details = input("Enter your project details: ")
    if details.strip() == "":
        print("Invalid: project details cannot be empty")
        project_details()
    else:
        print("perfect ..!")
        return details

# function for getting a total target for the new project
def project_target():
    global target
    target = input("Enter your project Total Target: ")
    if target.strip() == "":
        print("Invalid: project Total Target cannot be empty")
        project_target()
    else:
        print("perfect ..!")
        return target

# function for getting a start date for the new project
def project_startdate():
    global startdate
    startdate = input("Enter your project start date (in DD/MM/YYYY) : ")
    if startdate.strip() == "":
        print("Invalid: project start date cannot be empty")
        project_startdate()
    else:
        print("perfect ..!")
    if re.search(r'\d{1,2}[-/]\d{1,2}[-/]\d{4}', startdate):
        startdate = datetime.datetime.strptime(startdate, "%d/%m/%Y").date()
        return startdate
    else:
        print("Invalid: kindly input a valid start date")
        project_startdate()

# function for getting an end date for the new project
def project_enddate():
    global enddate
    enddate = input("Enter your project end date (in DD/MM/YYYY) : ")
    if enddate.strip() == "":
        print("Invalid: project end date cannot be empty")
        project_enddate()
    else:
        print("perfect ..!")
    if re.search(r'\d{1,2}[-/]\d{1,2}[-/]\d{4}', enddate):
        enddate = datetime.datetime.strptime(enddate, "%d/%m/%Y").date()
    else:
        print("Invalid: kindly input a valid end date")
        project_enddate()
    return enddate

# function for appending all data of the new project
def append_newproject():
    try:
        fileobject = open("projects.txt", 'a')
    except Exception as e:
        print(e)
    else:
        fileobject.write(title + ":" + details + ":" + target + ":" + startdate.strftime("%d/%m/%Y") + ":" + enddate.strftime("%d/%m/%Y") + ":" + mod1.email + "\n")
        fileobject.close()



# function to print all the projects on the screen
def view_projects():
    try:
        fileobject = open("projects.txt", 'r')
    except Exception as e:
        print(e)
    else:
        fileobject.seek(0)
        view = fileobject.readlines()
        fileobject.seek(0)
        print(view)

# function to create a new project
def create_new_project():
    mod1.logincheck()
    project_title()
    project_details()
    project_target()
    project_startdate()
    project_enddate()
    append_newproject()
    print("congratulations..! a new project had been created .. ")


# function to check before delete or edit
# def owner_checking():
#     global lines
#     global i
#     i = 0
#     try:
#         fileobject = open("projects.txt", 'r')
#     except Exception as e:
#         print(e)
#     else:
#         fileobject.seek(0)
#         linesnum = len(fileobject.readlines())
#         lines = fileobject.readlines()
#         fileobject.seek(0)
#         while i <= linesnum :
#             line = fileobject.readline()
#             fields = line.split(':')
#             project_creator = fields[5]
#             if project_creator == mod1.email :
#                 print("now you can use you project.. :) ")
#                 print(lines)
#                 lines.pop(i)
#                 fileobject.close()
#                 return
#             else:
#                 i += 1
#                 continue
#
#         else:
#             print("you can not use any project, you are not the owner of any project")
#             exit()


def owner_checking():
    global lines
    global i
    try:
        fileobject = open("projects.txt", 'r+')
    except Exception as e:
        print(e)
    else:
        fileobject.seek(0)
        lines = fileobject.readlines()
        fileobject.seek(0)
        for i, line in enumerate(lines):
            fields = line.split(':')
            project_creator = fields[5].strip()
            if project_creator == mod1.email:
                print("You are the owner of this project.")
                print(line)
                #lines.pop(i)
                # but it did not delete any thing
                fileobject.close()
                return
        else:
            print("You are not the owner of any project.")
            fileobject.close()
            exit()




# function of updating a project
def edit_project():
    mod1.logincheck()
    owner_checking()
    project_title()
    project_details()
    project_target()
    project_startdate()
    project_enddate()
    append_newproject()
    print("OK..!, The project had been UPDATED .. ")


# function of deleting a project
def delete_project():
    mod1.logincheck()
    owner_checking()
    print("OK..!, The project had been DELETED .. ")


# function of the first view that the user will see, a list of the options
def first_list_user():
    print("--------------------------------- THE LIST ----------------------------------------")
    options = ['View all projects', 'Create a new project', 'Edit your own project', 'Delete your own project']
    print("Please choose an one option from the list:")
    for i, option in enumerate(options):
        print(f"{i + 1}. {option}")

    chosen_option = int(input("Enter the number of the option you want to choose: "))
    if chosen_option > 0 and chosen_option <= 4:
        if chosen_option == 1:
            view_projects()
        elif chosen_option == 2:
            create_new_project()
        elif chosen_option == 3:
            edit_project()
        else:
            delete_project
    else:
        print("Invalid option number. Please try again.")
        first_list_user()

first_list_user()




