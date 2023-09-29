#=====importing libraries===========

def user_profiles():
    """Opens 'user.txt' and creates a list of all usernames and associated
    passwords.

    Returns:
        list: usernames and passwords stored in 'user.txt'
    """
    while True:
        try:
            with open('user.txt', 'r+') as f:
                data = f.read()
                data_list = data.replace('\n', ', ').split(', ')
            return data_list
        except FileNotFoundError:
            print('''
        ***************************************************************
        Uh OH! Something went wrong!
        
        The file "user.txt" does not exist. Please contact your System
        Administrator or the Task Manager App helpdesk for assistance.
        ***************************************************************
                  
                  ''')
            break

def user_name_lst(list):
    """Creates a new list from another list, but only stores every other 
    element from the original list. Iteration starts from index 0.

    Args:
        list: as defined. 

    Returns:
        list: from index 0, returning every other element from defined list.
    """
    user_names = list[0::2]
    return user_names

def user_dict(list):
    """
    Converts a list into a dictionary
    Args:
        list (for loop): iterate through list from first to list item based on 
        list length. 

    Returns:
        Dictionary: key-value pair based on
    the current element as the key and the next element as the value.
    """
    user_data_dict = {}
    for i in range(0, len(list), 2):
        user_data_dict[list[i]] = list[i + 1]
    return user_data_dict


# USER NAME LIST
user_list = user_name_lst(user_profiles())

# PASSWORD DISCTIONARY
password_dict = user_dict(user_profiles())

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password
'''

def enter_user(list):
    """Requests user input for username and checks whether user exists in 
    user.txt file.

    Args:
        list (str): usernames stored in user.txt file.
    """
    user_name = input('''
----------------------
Welome to Task Manager
----------------------
                        
Please login below (usernames & passwords are case sensitive)
Username:  ''')
    while user_name not in list:
        print('''
Username not recognised. Please retry...
Forgetten your username?  Please contact the System Administrator.
''')
        user_name = input("Enter Username:  ")
    return(user_name)

def user_login(lst, dict):
    """request user input for password and checks credentials are correct for 
    stated user. Re-entry of password will be requested until matching
    credentials in user.txt file.

    Args:
        lst (str): usernames sotred in user.txt file
        dict (key, value): key: username, value: password
    """
    username = enter_user(lst)
    correct_password = (dict[username])
    user_password = input('Enter Password:  ')
    while user_password != correct_password:
        print('''
Incorrect password entered. please retry...
Forgetten your password?  Please contact the System Administrator.''')
        user_password = input('Enter Password:  ')
    print("Login details verified.  Please wait...")
    return(username)

# USER LOGIN PROGRAM CODE
user_id = user_login(user_list, password_dict)
print(f'\nWelcome, {user_id}!')


#====App Functionality Section====

# FUNCTIONS | ADD NEW USER
def new_user():
    """
    Allow user to create a new username as part of the login credentials.
    The new username will be check against the pre-existing usernames in 
    user.txt file.  
    If the username exists an error message will be shown and the user will be
    asked to enter an alternative username.
    """
    print('''
          
--------------------------------
Task Manager | Register New User
--------------------------------
          
New login details (username & password) can be created on this page.
On successful creation of new login details they will be added to 'user.txt'.
      
''')
    user_name = input("Enter Username:  ")
    
    while user_name in user_name_lst(user_profiles()):
        print('''
Username already exists. Please enter an alternative...
''')
        user_name = input("Enter Username:  ")
    return(user_name)

def new_password():
    """
    Allows user to add a password to a new user name.  
    The user will have to enter the new password identically twice before 
    the password being accepted.
    """
    print('''You are about to setup a new password.  This is a 2 step process,
with both password entered needing to match for process to be successful\n''')
    
    password = input("Enter new password:  ")
    conf_password = input("Re-enter passowrd:  ")
    
    while conf_password != password:
        print("The re-entered password does not match.  Please retry...")
        while True:
            view_password = input("Would you like to view the oringinal password? (Y/N):  ").upper()
            if view_password == "Y":
                print(f"Original Password:  {password}")
                break
            elif view_password == "N":
                break
            else:
                print('Invalid entry. Please enter "Y" or "N"...')
        conf_password = input("Re-enter passowrd:  ")
    return(conf_password)

def add_user(user, password):
    """Creates a new user profile with unique username and associated password.
    User profile is appended to user.txt file.

    Args:
        user (input): called function output
        password (input): called function output
    """
    with open('user.txt', 'a') as f:
        f.write(f"\n{user}, {password}")
        print('''The new user details have been added to "user.txt".
You will now return to homepage option menu.
              ''')

# FUNCTIONS | ADD TASK
def task_user():
    """
    Allow user to assign task to specific user listed in 'user.txt' file
    """
    assign_user = input('Assign task to:  ')
    while assign_user not in user_list:
        print(''''User name does not exist.  Please make a selection from the
following list:''')
        print(*user_list, sep = '\n')
        assign_user = input('Assign task to:  ')
    return(assign_user)

def task_title():
    """
    Allow user to assign title to new task.
    """
    title = input("Enter Task title:  ")
    return(title)

def task_desc():
    """
    Allow user to assign description to new task.
    """
    desc = input("Enter task details:  ")
    return(desc)

def today_date():
    """
    Generates today's date in DD-MM-YYYY format.
    """
    from datetime import date
    today = date.today()
    today = (today.strftime("%d-%m-%y"))

    return(today)

def task_due():
    """
    Allows user to assign due date based on number of days entered.
    The enter number of days will be added to todays date.
    a due date will be returned in DD-MM-YYYY format.
    """
    from datetime import timedelta
    from datetime import date

    start_date  = date.today()

    while True:
        try:
            day_num = int(input(f'''Today's date is {start_date.strftime("%d-%m-%y")}.
How many caldendar days until this task is due?  '''))
            break
        except ValueError:
            print("\nInvalid entry, only whole numbers can be entered.  Please retry...\n")
        

    end_date = start_date + timedelta(days=day_num)
    due_date = (end_date.strftime("%d-%m-%y"))

    return(due_date)

def task_details():
    """
    Calls on associated functions to allow user to generate new task and include
    all required information.  
    User will be able to review task details before confirming whether to add
    details to 'tasks.txt' file.

    """
    user_resp = (task_user())
    title = (task_title())
    description = (task_desc())
    start_date = (today_date())
    due_date = (task_due())
    task_data = (f'\n{user_resp}, {title}, {description}, {start_date}, {due_date}, No')
    print(f'''\nThe task details entered are as follows:
Assigned to:    {user_resp}
Title:          {title}
Description:    {description}
Start Date:     {start_date}
Due Date:       {due_date}
''')
    return(task_data)

def y_n_valid(x):
    """
    Validates user input base on Y/N criteria.  User will be requested to retry
    entry if parameters not met.

    Args:
        x (input): user input with Y/N answer options only
    """
    while x not in ['Y', 'N']:
            print('Invalid entry.  Please enter "Y" or "N".')
            x = input('Would you like to added this to the tasks.txt file (Y/N)?  ').upper()
    return(x)

def add_task():
    """
    Provides with the option to add another task without having to return to the
    main menu and re-enter menu option.
    """
    add = "N"
    while add != "Y":
        task_data = task_details()
        add = input('Would you like to added this to the tasks.txt file (Y/N)?  ').upper()
        while add not in ['Y', 'N']:
            print('Invalid entry.  Please enter "Y" or "N".')
            add = input('Would you like to added this to the tasks.txt file (Y/N)?  ').upper()
                  
    with open('tasks.txt', 'a') as f:
        f.write(task_data)

    print('\nTasks details successfully added to tasks.txt file.\n')

def menu_return():
    """
    User input required to confrim that they are ready to return to main menu
    option page.

    Returns:
        input: "Y" - confirmation to return to main menu.
    """
    ready = "N"
    while ready != "Y":
        ready = input('''\nReady to return to main menu?
(Press "Y" to continue):  ''').upper()
        while ready not in ['Y']:
            print('\nInvalid entry.  Please enter "Y" to return to main menu.\n')
            ready = input('''\nReady to return to main menu?
(Press "Y" to continue):  ''').upper()
        else:
            return

while True:
    print('''
------------------------
Task Manager | Home Page
------------------------
          ''')
    print(f'Logged in as: {user_id}\n')

    if user_id == 'admin': # admin user specific menu
        menu = input('''Select one of the following options:
r - register new user
a - add task
va - view all tasks
vm - view my tasks
ds - display statistics
e - exit
: ''').lower()
    else:
        menu = input('''Select one of the following options:
r - register new user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    if menu == 'r':
        if user_id == 'admin': # admin user access only
            add_user(new_user(), new_password())
        else:
            print('Access Denied.  Only admin are able to add new users.')
            pass

    elif menu == 'a':
        print('''
---------------------------
Task Manager | Add New Task
---------------------------
          ''')

        add_task()
        add_more = "Y"
        while add_more != "N":
            add_more = input('\nWould you like to add another task (Y/N)?  ').upper()
            while add_more not in ['Y', 'N']:
                print('\nInvalid entry.  Please enter "Y" or "N".\n')
                add_more = input('Would you like to added another task (Y/N)?  ').upper()
            if add_more == "Y":
                add_task()
            else:
                pass

    elif menu == 'va':
        print('''
-----------------------------
Task Manager | View All Tasks
-----------------------------
              ''')
        with open('tasks.txt', 'r+') as f:
            lines = f.readlines()
            total_lines = len(lines)
            line_count = 0
            while line_count < total_lines:
                line = (lines[line_count]).strip().split(', ')
                line_count += 1
                print(f'\nTASK # {line_count} OF {total_lines}')
                print(f'Assigned to:   {line[0]}')
                print(f'Title:         {line[1]}')
                print(f'Description:   {line[2]}')
                print(f'Start Date:    {line[3]}')
                print(f'Due Date:      {line[4]}')
                print(f'Complete:      {line[5]}')
        
        menu_return()
        pass

    elif menu == 'vm':
        print('''
-----------------------------
Task Manager | View My Tasks
-----------------------------
              ''')
        with open('tasks.txt', 'r+') as f:
            lines = f.readlines()
            total_lines = len(lines)
            line_count = 0
            task_count = 0
            while line_count < total_lines:
                line = (lines[line_count]).strip().split(', ')
                line_count += 1
                if line[0] == user_id:
                    print(f'Assigned to:  {line[0]}')
                    print(f'Title:        {line[1]}')
                    print(f'Description:  {line[2]}')
                    print(f'Start Date:   {line[3]}')
                    print(f'Due Date:     {line[4]}')
                    print(f'Complete:     {line[5]}\n')
                    task_count += 1
            if task_count == 0:
                print(f'No tasks are currently assigned to {user_id}.')
        
        menu_return()
        pass

    elif menu == 'ds':
        print('''
-------------------------
Task Manager | Statistics
-------------------------
              ''')
        while True:
            try:
                with open('user.txt', 'r') as f:
                    lines = f.readlines()
                    total_lines = len(lines)
                    print(f'Total Number of Users = {total_lines}')
                    break
            except FileNotFoundError:
                print('user.txt file does not exist.  Please retry.')
        
        while True:
            try:
                with open('tasks.txt', 'r') as f:
                    lines = f.readlines()
                    total_lines = len(lines)
                    print(f'Total Number of Tasks = {total_lines}')
                    break
            except FileNotFoundError:
                print('tasks.txt file does not exist.  Please retry.')

        menu_return()
        pass

    elif menu == 'e':
        print(f'{user_id} has successfully logged out.  Bye for now!')
        exit()

    else:
        print("You have made entered an invalid input. Please try again")
