import json
def csv_to_list_dict(file, delim = ',', newline = '\n') -> list[dict]:
# TODO реализовать конвертер из csv в json
    with open(file, 'r') as f:
       data = [line.replace(newline, '').split(delim) for line in f]
# прочитаем первую строку как заголоки
       headers = data[0]
       lendata = len(data)
# оставшиеся в цикле засунем в словарь, добавим в список словарей
    result_list = []
    for i in range(1,lendata):
        result = dict(zip(headers,data[i]))
        result_list.append(result)
    return result_list

# инпут поправлен (в чатике писали про съехавшее содержимое https://github.com/aeksei/DD-PY-1-issue/issues/17#issuecomment-1308691761
INPUT_FILE = "input.csv"

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
