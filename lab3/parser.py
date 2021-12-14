from text_interface import print_graph_options

def parse_json_data(data):

    def parse_string_to_values(string):
        return list(map(float, string.split()))

    for label in data:
        data[label]["x"] = parse_string_to_values(data[label]["x"])
        data[label]["y"] = parse_string_to_values(data[label]["y"])

    for label in data:
        cords = list(zip(data[label]["x"], data[label]["y"]))
        sorted_cords = sorted(cords, key=lambda values: values[0])
        sorted_x = [cord[0] for cord in sorted_cords]
        sorted_y = [cord[1] for cord in sorted_cords]
        data[label]["x"] = sorted_x
        data[label]["y"] = sorted_y

    return filter_data(data)


def filter_data(data):
    print_graph_options()
    option = input('>>> ')

    if option not in ['all', 'one', 'range', 'group']:
        print("Введён неверный аргумент")
        exit(1)

    if option == 'all':
        return data

    if option == "one":
        index = int(input("Введите индекс графика: ")) - 1
        label, cords = list(data.items())[index]
        return {label: cords}

    if option == "range":
        start, end = [value - 1 for value in
                      list(map(int, input("Введите диапазон (2 целых числа через пробел): ").split(' ')))]
        return {label: cords for (label, cords) in list(data.items())[start: end + 1]}

    if option == "group":
        index_array = [value - 1 for value in list(
            map(int, input("Введите последовательность цифр - индексы графиков через пробел: ").split(' ')))]
        group = [list(data.items())[index] for index in index_array]
        return {label: cords for (label, cords) in group}

