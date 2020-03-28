from random import choices

def select_names(list_names, new_len_list_names_N):
    return choices(list_names, k=new_len_list_names_N)

def Name_repead_max(list_names):
    # инициализация пустого словаря
    name_max = {}
    # перебор имён в списке
    for name in list_names:
        # наполнение словаря уникальными именами (key)
        # и одновременным подсчётом и сопоставлением количества их повторов (value)
        name_max[name] = name_max.get(name, 0) + 1
    # преобразование типа словарь в тип список
    name_max = list(name_max.items())
    # сортировка по value - x[1], с одновременным указанием от большего к меньшему
    name_max.sort(key=lambda x: x[1], reverse=True)
    return name_max[0][0]

def find_sort_symbol(list_names):
    """
    :param list_names: список имен
    :return: первый символ имени, реже всего встречающийся в списке
    """
    # инициализация пустого словаря dict_First_sym_of_names
    dict_First_sym_of_names = {}
    #print(type(dict_First_sym_of_names),dict_First_sym_of_names)
    # огранизация цикла для перебора имён из списка list_names
    for name in list_names:
        # присвоение переменной First_sym_of_name первого символа имени [0]
        First_sym_of_name = name[0]
        # наполнение славоря dict_First_sym_of_names с key = First_sym_of_name и value = количество повторов символа
        dict_First_sym_of_names[First_sym_of_name] = dict_First_sym_of_names.get(First_sym_of_name, 0) + 1
    # преобразование типа словаря в тип листа и сортировка по второму элементу листа, т.е. по количествам повторов символа
    # x[0] - key (str), а x[1] - value (integer)
    dict_First_sym_of_names = sorted(list(dict_First_sym_of_names.items()), key=lambda x: x[1])
    #print(type(dict_First_sym_of_names),dict_First_sym_of_names)
    return dict_First_sym_of_names[0][0]

New_list_gen = select_names(['Ильфат', 'Ильдар', 'Ильгиз', 'Ильдус', 'Ильнур', 'Ильшат', 'Ильхам','Салих', 'Ирек',
                      'Марат', 'Айрат', 'Айдар', 'Ахмат', 'Ринат', 'Руслан', 'Рустам', 'Шамиль'], new_len_list_names_N=100)
print(New_list_gen)
print(Name_repead_max(New_list_gen))
print(find_sort_symbol(New_list_gen), '- здесь вероятнее всего, самыми редкими первыми символами имён должны быть "С","М","Ш"')