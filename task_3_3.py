def thesaurus(*args, sort=False):
    """
    Return dict with key first char form Last_Name
    and value is dict with key first char from First_Name
    and value is list of "First_Name Second_Name"

    :param args: tuple of strings "First_Name Second_Name" 
    :param sort: sort by alphabet
    :return: dictionary with key first char Second Name 
             and value is dictionary with key first char First Name 
             and value is "First_Name Second_Name"
    """
    name_dict = {}
    for name in args:
        if not name_dict.setdefault(name[0], [name]) == [name]:
            name_dict[name[0]].append(name)
    return name_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
