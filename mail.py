import json
from maillist import MailList

def show_lists(lists):
    result = []
    for key in lists:
        result.append('[{0}] - {1}'.format(key, lists[key].get_name()))
    result = sorted(result)
    return '\n'.join(result) + '\n'

def show_list(lists, list_id):
    if not list_id in lists:
        print('List with unique identifier {} was not found!'.format(id))
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
