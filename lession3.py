def url_parse1(url):
    """
    Parses url address in tuple of items

    """
    _t_protocol, _, domain, *resource_address = url.strip('/').split('/')
    t_protocol = _t_protocol[:-1]
    return t_protocol, domain, resource_address


def url_parse2(url):
    _t_protocol, _, domain, *resource_address = url.split('/')
    t_protocol = _t_protocol[:-1]
    return t_protocol, domain, resource_address


print(url_parse1('https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/'))
print(url_parse2('https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/'))


nums = ['1578.4', '892.4', '354.1', '871.5']
print(sum(map(float, nums)))  # 3696.4


vector_list = [[1, 2, 3]]
for i, vector in enumerate(vector_list * 3):
    print(f"{i + 1} scalar product of vector: {[(i + 1) * e for e in vector]}")
# 1 scalar product of vector: [1, 2, 3]
# 2 scalar product of vector: [2, 4, 6]
# 3 scalar product of vector: [3, 6, 9]

print([1, 2, 3] * 3)

print('--------------------------')
print('01234'[:-1])
print('01234'[-1])

print('--------------------------')
prices = ['15,78.4', '892.4', '354.1 rub', '871.5', '47,1']
prices_float = map(float, filter(lambda x: x.replace('.', '', 1).isdigit(), prices))
print(*prices_float)

# Неправильно
# prices = ['15,78.4', '892.4', '354.1 rub', '871.5', '47,1']
# prices_float = map(float, filter(lambda x: x.replace(',', '.', 1).replace('.', '', 1).isdigit(), prices))
# print(*prices_float)

my_dict = {'key': 'value'}
my_dict.update({'another_key': 'another_value'})  # Дополняем.
my_dict.update({'another_key': 'yet_another_value'})  # Обновляем.
print(my_dict)

my_dict = {'A':{'B':['fvfdsr']}}

my_dict['A']['B'].append('dsw dfwsdf')
print(my_dict['A']['B'])



