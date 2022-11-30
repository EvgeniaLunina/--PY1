import csv
import json

INPUT_FILE = "input.csv"
delimiter = ","
new_line = "\n"


def csv_to_list_dict(INPUT_FILE) -> list[dict]:
    ...  # TODO реализовать конвертер из csv в json
    with open(INPUT_FILE) as f:
        list_ = []
        list_of_dict_ = []
        for line in f:
            list_.append(line.replace(new_line, '').split(delimiter))

        headline = list_[0]

        for line_ in list_[1:]:
            dict_ = {headline[number]: line_[number] for number in range(len(headline))}
            list_of_dict_.append(dict_)

        return list_of_dict_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
