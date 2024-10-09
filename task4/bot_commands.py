from decorators import input_error, show_all_error

@input_error
def add_contact(args: list, contacts: dict) -> str:
    name, phone = args

    if name in contacts:
        return change_contact(args, contacts)
    
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: list, contacts: dict) -> str:
    name, phone = args

    if name not in contacts:
        raise KeyError(name)
    
    contacts[name] = phone
    return "Contact updated."
    

@input_error
def show_phone(args: list, contacts: dict) -> str: 
    name = args[0]
    if name not in contacts:
        raise KeyError(name)
    
    return contacts[name]


@show_all_error
def show_all(contacts: dict) -> str:
    if not contacts:
        raise ValueError
    
    return "\n".join(f"{name:<10}: {phone}" for name, phone in contacts.items())
