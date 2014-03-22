import json
import os
from maillist import MailList
from maillist_factory import MailListFactory

def merge(lists, factory, list1_id, list2_id, name):
    listi = factory.create(name)
    for l in lists:
        if l.get_id() == list1_id or l.get_id() == list2_id:
            for item in l.users:
                if not listi.search_email(item.email):
                    listi.add_user(item.name, item.email)


    lists.append(listi)

    print('Merged lists <{0}> and <{1}> into <{2}>'\
        .format(lists[list1_id].get_name(), lists[list2_id].get_name(),
         name))


def show_lists(lists):
    result = []
    for l in lists:
        result.append('[{0}] - {1}'.format(l.get_id(), l.get_name()))
    result = sorted(result)
    return '\n'.join(result) + '\n'

def show_list(lists, list_id):
    for l in lists:
        if l.get_id() == list_id:
            return l.print_()

    return False

def create_list(lists, m_factory, new_list):
    lists.append(m_factory.create(new_list))
    print('New list <{0}> was created!'.format(new_list))

def add_new_user(lists, list_id, name, email):
    for i in range(len(lists)):
        if lists[i].get_id() == list_id:
            lists[i].add_user(name, email)
            return True
    print('List with unique identifier {} was not found!'.format(list_id))
    return False

def update_subscriber (lists, unique_list_id, unique_name_id):
    if not unique_list_id in lists:
        print('List with unique indentifier {} was not found!'.format(uniqie_list_id))
        return False
    if unique_name_id >= len(lists[unique_list_id].users):
        print('Subscriber with unique name indentifier {} was not found!'.format(unique_name_id))
        return False

    name = input('enter new name>')
    email = input('enter new email>')

    lists[unique_list_id].users[unique_name_id].update_subscriber(name, email)
    print("Subscriber updated: {0} - {1}".format(lists[unique_list_id].users[unique_name_id].take_name(), lists[unique_list_id].users[unique_name_id].take_email()))

#remove_subscriber <unique_list_identifier> <unique_name_identifier> - \Removes the given subscriber from the given list
def remove_subscriber(lists, unique_list_id, unique_name_id):
    for i in range(len(lists)):
        if lists[i].get_id() == unique_list_id:
            if not unique_name_id > len(lists[i].users):
                lists[i].users = lists[i].users[:unique_name_id - 1] +\
                    lists[i].users[unique_name_id:]
            else:
                print('Subscriber with unique name indentifier {} was not found!'\
                        .format(unique_name_id))
    print('List with unique indentifier {} was not found!'.format(unique_list_id))
    return False


def export(lists, list_id):
    for l in lists:
        if l.get_id() == list_id:
            json_data = json.dumps(l.__dict__)
            file_to_save = open('{}.json'.format(l.get_name()), 'w')
            file_to_save.write(json_data)
            file_to_save.close()
    print('List with unique identifier {} was not found!'.format(list_id))
    return False

def import_json(lists, factory, json_filename):
    if os.path.isfile(json_filename):
        json_f = open(json_filename, 'r')
        json_data = json_f.read()
        json_f.close()

        print('Creating maillist with name {}'.format(json_filename[:-5]))
        m_dict = json.loads(json_data)
        new_maillist = factory.create(m_dict['name'])
        for user in m_dict['users']:
            new_maillist.add_user(user['name'], user['email'])

        lists.append(new_maillist)

    else:
        print('{} doesn\'t exist'.format(json_filename))

def search_email(lists, email):
    result = ['<{}> was found in:'.format(email)]
    for l in lists:
        if l.search_email(email):
            result.append('[{0}] - {1}'.format(l.get_id(), l.get_name()))
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

def parse_command(command):
    return tuple(command.split(' '))

def is_command(command_tuple, command_string):
    return command_tuple[0] == command_string

def main():
    lists = []
    factory = MailListFactory()

    print(create_menu())

    while True:
        command_tuple = parse_command(input('Enter command>'))

        if is_command(command_tuple, 'help'):
            print(create_help())
        elif is_command(command_tuple, 'show_lists'):
            print(show_lists(lists))
        elif is_command(command_tuple, 'show_list'):
            print(show_list(lists, int(command_tuple[1])))
        elif is_command(command_tuple, 'add'):
            name = input('name>')
            email = input('email>')
            add_new_user(lists, int(command_tuple[1]), name, email)
        elif is_command(command_tuple, 'create'):
            create_list(lists, factory, command_tuple[1])
        elif is_command(command_tuple, 'search_email'):
            print(search_email(lists, command_tuple[1]))
        elif is_command(command_tuple, 'merge_lists'):
            list1, list2, new_list = command_tuple[1:]
            merge(lists, factory, int(list1), int(list2), new_list)
        elif is_command(command_tuple, 'export'):
            export(lists, int(command_tuple[1]))
        elif is_command(command_tuple, 'exit'):
            break
        else:
            print('Unknown command!')

if __name__ == '__main__':
    main()
