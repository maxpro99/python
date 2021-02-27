def thesaurus_adv(*args):
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
    for current_name in args:
        a, b = current_name.split()[1][0], current_name.split()[0][0]
        if not name_dict.setdefault(a, {b: [current_name]}) == {b: [current_name]}:
            if name_dict[a].get(b) is None:
                name_dict[a].setdefault(b, [current_name])
            else:
                name_dict[a][b].append(current_name)
    return name_dict


my_dict = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Алик Алексеев")
print(my_dict)
