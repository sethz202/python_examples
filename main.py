import DB_Controller

def main_menu(user_type):
    if user_type == 'researcher':
        print('1. View Information')
        print('2. Add Information')
        print('3. Remove Information')
        print('4. Add User')
        print('5. Remove User')
        print('6. Quit')
        choice = int(input('What would you like to do? (Enter a corresponding number): '))
        if choice == 1:
            view_information(user_type)
        elif choice == 2:
            add_information(user_type)
        elif choice == 3:
            remove_information(user_type)
        elif choice == 4:
            add_user(user_type)
        elif choice == 5:
            remove_user(user_type)
        elif choice == 6:
            print('Quitting program...')
            exit()
    elif user_type == 'customer support':
        print('1. Log an issue')
        print('2. View open support cases')
        print('3. Cancel order')
        print('4. Quit')
        choice = int(input('What would you like to do? (Enter a corresponding number): '))
        if choice == 1:
            log_issue(user_type)
        elif choice == 2:
            view_open_support_cases(user_type)
        elif choice == 3:
            cancel_order(user_type)
        elif choice == 4:
            print('Quitting program...')
            exit()
    elif user_type == 'user':
        print('1. View Information')
        print('2. Log an issue')
        print('3. Quit')
        choice = int(input('What would you like to do? (Enter a corresponding number): '))
        if choice == 1:
            view_information(user_type)
        elif choice == 2:
            log_issue(user_type)
        elif choice == 3:
            print('Quitting program...')
            exit()

def view_information(user_type):
    print('---View Information---')
    print('1. Meso-structure microbialites')
    print('2. Macro-structure microbialites')
    print('3. Return to main menu')
    choice = int(input('What would you like to view? (Enter a corresponding number): '))
    if choice == 1 or choice==2:
        m_type = ''
        if choice == 1:
            m_type = 'Meso'
        else:
            m_type = 'Macro'
        m_structure = DB.get_mstructure(m_type)
        if len(m_structure) == 0:
            print('No information available.')
            return
        m_list = []
        for m in m_structure:
            print(m)
            if m_type == 'Meso':
                if m[5] == None and m[6] == None:
                    m_list.append([f"Mesostructure Microbialite ID: {m[0]}", 'No description available.', m])
                elif m[5] == None:
                    m_list.append([f"Mesostructure Microbialite ID: {m[0]}", m[6].strip(), m])
                else:
                    m_list.append([f"Mesostructure Microbialite ID: {m[0]}", m[5].strip(), m])
            else:
                if m[7] == None:
                    m_list.append([f"Macrostructure Microbialite ID: {m[0]}", 'No description available.', m])
                else:
                    m_list.append([f"Macrostructure Microbialite ID: {m[0]}", m[7].strip(),m])
        print(m_list)
        for i in range(len(m_list)):
            print(f'{i+1}. {m_list[i][0]} \nDescription: {m_list[i][1]}\n')
        choice = int(input('Select a meso-structure to view (Enter a corresponding number): '))
        try:
            print(f'{m_list[choice-1][0]}\nDescription: {m_list[choice-1][1]}\nImageID: {m_list[choice-1][2][3]}\nSampleID: {m_list[choice-1][2][4]}\nType: {m_list[choice-1][2][7]}\nLamina Properties: \nLamina Thickness: {m_list[choice-1][2][9]}\nTexture 1: {m_list[choice-1][2][10]}\nAmplitude: {m_list[choice-1][2][11]}\nTexture 2: {m_list[choice-1][2][12]}\nGrains: {m_list[choice-1][2][13]}\nSynoptic Relief: {m_list[choice-1][2][14]}\nWavelength: {m_list[choice-1][2][15]}')
        except Exception as e:
            print(f'{m_list[choice-1][0]}\nDescription: {m_list[choice-1][1]}\nImageID: {m_list[choice-1][2][4]}')
        input('Press enter to return to main menu...')
        main_menu(user_type)
    elif choice == 3:
        main_menu(user_type)
    else:
        print('Invalid option selected. Please try again.')
        view_information(user_type)

def add_information(user_type):
    '''
    add_information options
    '''
    print('---Add Information---')
    print('1. Meso-structure microbialites')
    print('2. Macro-structure microbialites')
    print('3. Return to main menu')
    choice = int(input('What would you like to add? (Enter a corresponding number): '))

    '''
    1.Meso-structure microbialites is selected.
    '''
    if (choice == 1):
        q1 = input('Enter StromatoliticID (enter integer or press Enter if null): ')
        q2 = input('Enter ThromboliticID (enter integer or press Enter if null): ')
        q3 = input('Enter ImageID (enter integer or press Enter if null): ')
        q4 = input('Enter SampleIDKey (enter string or press Enter if null): ')
        q5 = input('Enter Field Description (enter string or press Enter if null): ')
        q6 = input('Enter Rock Description (enter string or press Enter if null): ')
        q7 = input('Enter General Type (enter string or press Enter if null): ')
        q8 = input('Enter Lamina Properties (enter string or press Enter if null): ')
        q9 = input('Enter Lamina Thickness (enter integer or press Enter if null): ')
        q10 = input('Enter Texture 1 (enter string or press Enter if null): ')
        q11 = input('Enter Amplitude (enter integer or press Enter if null): ')
        q12 = input('Enter Texture 2 (enter string or press Enter if null): ')
        q13 = input('Enter Grains (enter string or press Enter if null): ')
        q14 = input('Enter Synoptic Relief (enter integer or press Enter if null): ')
        q15 = input('Enter Wavelength (enter integer or press Enter if null): ')

        if (not q1 == "" and not q1.isdigit()):
            print('Invalid input for StromatoliticID. Please try again.')
            add_information(user_type)
        elif (not q1 == ""):
            q1 = int(q1)
        else:
            q1 = None
        if (not q2 == "" and not q2.isdigit()):
            print('Invalid input for ThromboliticID. Please try again.')
            add_information(user_type)
        elif (not q2 == ""):
            q2 = int(q2)
        else:
            q2 = None
        if (not q3 == "" and not q3.isdigit()):
            print('Invalid input for ImageID. Please try again.')
            add_information(user_type)
        elif (not q3 == ""):
            q3 = int(q3)
        else:
            q3 = None
        if (not q4 == "" and not isinstance(q4, str)):
            print('Invalid input for SampleIDKey. Please try again.')
            add_information(user_type)
        if (not q5 == "" and not isinstance(q5, str)):
            print('Invalid input for Field Description. Please try again.')
            add_information(user_type)
        if (not q6 == "" and not isinstance(q6, str)):
            print('Invalid input for Rock Description. Please try again.')
            add_information(user_type)
        if (not q7 == "" and not isinstance(q7, str)):
            print('Invalid input for General Type. Please try again.')
            add_information(user_type)
        if (not q8 == "" and not isinstance(q8, str)):
            print('Invalid input for Lamina Properties. Please try again.')
            add_information(user_type)
        else:
            q8 = None
        if (not q9 == "" and not q9.isdigit()):
            print('Invalid input for Lamina Thickness. Please try again.')
            add_information(user_type)
        elif (not q9 == ""):
            q9 = int(q9)
        else:
            q9 = None
        if (not q10 == "" and not isinstance(q10, str)):
            print('Invalid input for Texture 1. Please try again.')
            add_information(user_type)
        if (not q11 == "" and not q11.isdigit()):
            print('Invalid input for Amplitude. Please try again.')
            add_information(user_type)
        elif (not q11 == ""):
            q11 = int(q11)
        else:
            q11 = None
        if (not q12 == "" and not isinstance(q12, str)):
            print('Invalid input for Texture 2. Please try again.')
            add_information(user_type)
        else:
            q12 = None
        if (not q13 == "" and not isinstance(q13, str)):
            print('Invalid input for Grains. Please try again.')
            add_information(user_type)
        else:
            q13 = None
        if (not q14 == "" and not q14.isdigit()):
            print('Invalid input for Synoptic Relief. Please try again.')
            add_information(user_type)
        elif (not q14 == ""):
            q14 = int(q14)
        else:
            q14 = None
        if (not q15 == "" and not q15.isdigit()):
            print('Invalid input for Wavelength. Please try again.')
            add_information(user_type)
        elif (not q15 == ""):
            q15 = int(q15)
        else:
            q15 = None

        DB.add_information_meso(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15)
        main_menu(user_type)
        
    '''
    2.Macro-structure microbialites is selected.
    '''
    if (choice == 2):
        q1 = input('Enter WaypointID (enter integer or press Enter if null): ')
        q2 = input('Enter MesostructureID (enter integer or press Enter if null): ')
        q3 = input('Enter MegaStructureID (enter integer or press Enter if null): ')
        q4 = input('Enter ImageID (enter integer or press Enter if null): ')
        q5 = input('Enter MacroinfoID (enter integer or press Enter if null): ')
        q6 = input('Enter SectionHeight (enter decimal with a total of 5 digits and 1 digit after the decimal point or press Enter if null): ')
        q7 = input('Enter Comments (enter string or press Enter if null): ')

        if (not q1 == "" and not q1.isdigit()):
            print('Invalid input for WaypointID. Please try again.')
            add_information(user_type)
        elif (not q1 == ""):
            q1 = int(q1)
        else:
            q1 = None
        if (not q2 == "" and not q2.isdigit()):
            print('Invalid input for MesostructureID. Please try again.')
            add_information(user_type)
        elif (not q2 == ""):
            q2 = int(q2)
        else:
            q2 = None
        if (not q3 == "" and not q3.isdigit()):
            print('Invalid input for MegaStructureID. Please try again.')
            add_information(user_type)
        elif (not q3 == ""):
            q3 = int(q3)
        else:
            q3 = None
        if (not q4 == "" and not q4.isdigit()):
            print('Invalid input for ImageID. Please try again.')
            add_information(user_type)
        elif (not q4 == ""):
            q4 = int(q4)
        else:
            q4 = None
        if (not q5 == "" and not q5.isdigit()):
            print('Invalid input for MacroinfoID. Please try again.')
            add_information(user_type)
        elif (not q5 == ""):
            q5 = int(q5)
        else:
            q5 = None
        if (not q6 == "" and not is_double_5_1(q6)):
            print('Invalid input for SectionHeight. Please try again.')
            add_information(user_type)
        elif (not q6 == ""):
            q6 = float(q6)
        else:
            q6 = None
        if (not q7 == "" and not isinstance(q7, str)):
            print('Invalid input for Comments. Please try again.')
            add_information(user_type)

        DB.add_information_macro(q1,q2,q3,q4,q5,q6,q7)
        main_menu(user_type)

    '''
    3.Return to main menu is selected.
    '''
    if (choice == 3):
        main_menu(user_type)

    '''
    None of the valid options is selected.
    '''
    if (choice != 1 and choice != 2 and choice != 3):
        print('Invalid option selected. Please try again.')
        add_information(user_type)

def is_double_5_1(str_value):
    """
    This function checks if value is double(5,1) in mySQL.
    """
    try:
        if (len(str_value) == 0):
            return True
        if (len(str_value) > 6):
            return False
        dot_index = str_value.find('.')
        if (len(str_value)-1-dot_index != 1):
            return False
        else:
            return True
    except ValueError:
        return False

def remove_information(user_type):
    """
    remove_information options
    """
    print('---Remove Information---')
    print('1. Meso-structure microbialites')
    print('2. Macro-structure microbialites')
    print('3. Return to main menu')
    choice = int(input('What would you like to remove? (Enter a corresponding number): '))

    """
    1.Meso-structure microbialites is selected.
    """
    if (choice == 1):
        MesostructureID = int(input("Enter MesostructureID to remove: "))
        DB.remove_information_meso(MesostructureID)
        main_menu(user_type)

    """
    2.Macro-structure microbialites is selected.
    """
    if (choice == 2):
        MacrostructureID = int(input("Enter MacrostructureID to remove: "))
        DB.remove_information_macro(MacrostructureID)
        main_menu(user_type)

    """
    3.Return to main menu is selected.
    """
    if (choice == 3):
        main_menu(user_type)

    """
    None of the valid options is selected.
    """
    if (choice != 1 and choice != 2 and choice != 3):
        print('Invalid option selected. Please try again.')
        add_information(user_type)

def add_user(user_type):
    user_types = {1: 'researcher', 2: 'customer support', 3: 'user'}
    print('---Add User---')
    print('1. Researcher')
    print('2. Customer Support')
    print('3. User')
    print('4. Return to main menu')
    choice = int(input('What type of user would you like to add? (Enter a corresponding number): '))
    if choice == 1 or choice == 2 or choice == 3:
        extra_info = []
        f_name = input(f'Enter the {user_types[choice]}\'s first name: ')
        l_name = input(f'Enter the {user_types[choice]}\'s last name: ')
        if l_name.endswith('s'):
            email = input(f'Enter {f_name} {l_name}\' email: ')
        else:
            email = input(f'Enter {f_name} {l_name}\'s email: ')
        if choice == 1:
            extra_info.append(input(f'Enter {f_name} {l_name}\'s salary: '))
            extra_info.append(input(f'Enter {f_name} {l_name}\'s work hours: '))
            extra_info.append(input(f'Enter {f_name} {l_name}\'s job description: '))
        elif choice == 2:
            extra_info.append(input(f'Enter {f_name} {l_name}\'s department name: '))
            extra_info.append(input(f'Enter {f_name} {l_name}\'s phone number: '))
        DB.add_user(f_name, l_name, email, extra_info)
        print(f'{user_types[choice].capitalize()} {f_name} {l_name} added successfully.')
        add_user(user_type)
    elif choice == 4:
        main_menu(user_type)
    else:
        print('Invalid option selected. Please try again.')
        add_user(user_type)

def remove_user(user_type):
    print('---Remove User---')
    users = DB.get_users()
    if len(users) == 0:
        print('No users to remove.')
        return
    for i in range(len(users)):
        print(f'{i+1}. {users[i][1]} {users[i][2]}')
    print(f'{len(users)+1}. Return to main menu')
    choice = int(input('Select a user to remove (Enter a corresponding number): '))
    if choice <= len(users):
        print(f'{users[choice-1][1]} {users[choice-1][2]} removed successfully.')
        DB.remove_user(users[choice-1][0])
        remove_user(user_type)
    elif choice == len(users)+1:
        main_menu(user_type)
    else:
        print('Invalid option selected. Please try again.')
        remove_user(user_type)

def log_issue(user_type):
    print('---Log an issue---')
    print('Valid issue types: 1. Viewing issue 2. Payment issue 3. Issue adding/editing information, 4. Other')
    issues_dict = {1: 'Viewing', 2: 'Payment', 3: 'Adding/editing information', 4: 'Other'}
    issue_type = int(input('What type of issue would you like to log? (Enter a corresponding number): '))
    issue_description = input('Please describe the issue: ')
    user_id = input('Enter your user ID: ')
    if user_type == 'customer support':
        support_id = user_id
        support_id = input('Enter the customer support\'s ID: ')
    else:
        support_id = None
    DB.add_issue([user_id, support_id, issue_description, issues_dict[issue_type]])
    print('Issue logged successfully.')
    main_menu(user_type)

def cancel_order(user_type):
    print('---Cancel order---')
    order_number = input('Enter the order number to cancel: ')
    cancel_reason = input('Enter cancelation reasoning (optional):')
    #We do not have an order table so we cannot implement this function with SQL
    print(f'Successfully canceled order {order_number}.')
    main_menu(user_type)

def view_open_support_cases(user_type):
    print('---Open support cases---')
    cases = DB.get_open_support_cases()
    case_list = []
    for case in cases:
        case_list.append([case[0],case[3], case[4],case[5]])
    if len(case_list) != 0:
        for i in range(len(case_list)):
            print(f'{i+1}. {case_list[i][3]} Issue: {case_list[i][1]}')
        print(f'{len(case_list)+1}. Return to main menu')
    else:
        print('No open support cases.')
    
    choice = int(input('Select a case to view (Enter a corresponding number): '))
    if choice == len(case_list)+1:
        main_menu(user_type)
    else:
        print(f'Case ID: {case_list[choice-1][0]} \nDescription: {case_list[choice-1][1]} \nIssue Type: {case_list[choice-1][3]} \nDate Reported: {case_list[choice-1][2]}')
        input('Press enter to return to main menu...')
        main_menu(user_type)


DB = DB_Controller.DB_Controller()

while True:
    user_type = input('Enter your user type (researcher, customer support, user): ')
    main_menu(user_type.lower())