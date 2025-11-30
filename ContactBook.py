contact = {}
def add_contact(name, phone):
    key = name.lower()
    contact[key] = phone
    return f'{name} has been added to contact'

def search_contact(name):
    key = name.lower()
    if key in contact:
        return f"{name} contact is {contact[key]}"
    else:
        return "{name} not found in contact"

def delete_contact(name):
    key = name.lower()
    if key in contact:
        del contact[key]
        return f'{name} has been deleted from contact'
    else:
        return f"{name} not found in contact"

def list_contact():
    return [f'{name}: {phone}' for name, phone in contact.items() ]

add_contact("John", "12345678")
add_contact("Edu", "902344323")
print(search_contact("John"))
print(delete_contact("jOhn"))
print(list_contact())