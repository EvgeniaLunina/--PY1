def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = str_.lower()
    count_dict = {}
    for char in str_:
        if char.isalpha():
            count_dict[char] = count_dict.get(char, 0) + 1
    return count_dict

def get_percentage_char(count_dict):
    total_count_char = sum(count_dict.values())
    for char, count in count_dict.items():
        count_dict[char] = count / total_count_char * 100
    return count_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
count_dict = get_count_char(main_str)
print(count_dict)
#count_dict = get_percentage_char(count_dict)
#print(count_dict)