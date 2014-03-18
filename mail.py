import json
from maillist import MailList

def merge(list1, list2, name):

    listi = MailList(name)
    for item in list1:
        listi.add_user(item.name, item.email)

    for item in list2:
        if not listi.search_email(item.email()):
            listi.add_user(item.name, item.emial)

    lists[len(lists) + 1] = listi

def show_lists(lists):
    result = []
    for key in lists:
        result.append('[{0}] - {1}'.format(key, lists[key].get_name()))
    result = sorted(result)
    return '\n'.join(result) + '\n'

def show_list(lists, list_id):
    if not list_id in lists:
        print('List with unique identifier {} was not found!'.format(list_id))
        return False
    return lists[list_id].print_()

def create_list(lists, new_list):
    lists[len(lists) + 1] = MailList(new_list)

def add_new_user(lists, list_id, name, email):
    if not list_id in lists:
        print('List with unique identifier {} was not found!'.format(list_id))
        return False
    lists[list_id].add_user(name, email)
    return True

def export(lists, list_id):
    if not list_id in lists:
        print('List with unique identifier {} was not found!'.format(list_id))
        return False
    peio = json.dumps(lists[list_id].__dict__)

def search_email(lists, email):
    result = ['<{}> was found in:'.format(email)]
    for key in lists:
        if lists[key].search_email(email):
            result.append('[{0}] - {1}'.format(key, lists[key].get_name()))
    return '\n'.join(result)

def create_menu():
    menu = ["Hello Stranger! This is a cutting-edge, console-based mail-list!",
"Type help, to see a list of commands."]

    return "\n".join(menu)

def create_help():
    helpi = ["Here is a full list of commands:",
"* show_lists - Prints all lists to the screen. Each list is assigned with a unique identifier",
"* show_list <unique_list_identifier> - Prints all people, one person at a line, that are subscribed for the list. The format is: <Name> - <Email>",
"* add <unique_list_identifier> - Starts the procedure for adding a person to a mail list. The program prompts for name and email.",
"* create <list_name> - Creates a new empty list, with the given name.",
"* search_email <email> - Performs a search into all lists to see if the given email is present. Shows all lists, where the email was found.",
"* merge_lists <list_identifier_1> <list_identifier_2> <new_list_name> - merges list1 and list2 into a new list, with the given name.",
"* export <unique_list_identifier> - Exports the given list into JSON file, named just like the list. All white spaces are replaced by underscores.",
"* exit - this will quit the program"]

    return "\n".join(helpi)
