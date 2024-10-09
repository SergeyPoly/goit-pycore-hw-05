from functools import wraps

def parse_command_error(func):
    @wraps(func)
    def inner(arg):
        try:
            return func(arg)
        except ValueError:
            return ['error']

    return inner


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter name and phone please."
        except IndexError:
            return "Enter name please."
        except KeyError as e:
            return f"No such name: {e} in contacts"

    return inner


def show_all_error(func):
    @wraps(func)
    def inner(arg):
        try:
            return func(arg)
        except ValueError:
            return "No contacts available."

    return inner