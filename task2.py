def get_count_char(str_):# TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = "".join(str_.lower())
    dict_ = {}
    for article in str_:
        if article not in dict_:
            if article.isalpha():
                dict_[article] = 1
        else:
            dict_[article] += 1
    return(dict_)
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
