def thesaurus(*args, sort=False):
    name_dict = {}
    for name in args:
        if not name_dict.setdefault(name[0], [name]) == [name]:
            name_dict[name[0]].append(name)
    return name_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
