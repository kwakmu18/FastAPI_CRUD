def get_full_name(first_name:str, last_name:str): # type hints
    full_name = first_name.title() + " " + last_name.title()
    return full_name

def get_name_with_age(name:str, age:int):
    name_with_age = name + " is this old: " + age
    return name_with_age

print(get_full_name("john", "doe"))
print(get_name_with_age("john", 12))