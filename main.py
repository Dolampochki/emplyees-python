import menu

menu_list = menu.menu_list


def print_menu():
    print('\nPlease enter the action from the list:')
    for action in menu_list.keys():
        print(menu_list[action]['name'] + ' - ' + action)


def select_action():
    print_menu()
    while True:
        try:
            user_choice = input('Select the action: ')
            menu_list[user_choice]['func']()
        except:
            print('Something went wrong, try again')
        else:
            break
        finally:
            select_action()


select_action()
