def percent_str(in_number):
    out_str = ' процентов'

    # Тут Берем из условия целые числа, иначе надо переписывать
    if 1 < in_number % 10 < 5:
        out_str = ' процента'
    elif in_number % 10 == 1:
        out_str = ' процент'
    if 10 < in_number < 15:
        out_str = ' процентов'

    return out_str

#Берем чуть больше 20, поскольку именно окончания внутри второго десятка отличны от других
for num in range(31):
    print(num, percent_str(num))