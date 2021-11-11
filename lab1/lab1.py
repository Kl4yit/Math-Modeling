import matplotlib.pyplot as plt
import json


DATA_FILE_PATH = 'data.json'


def parse_json_data(data_path):
    with open(data_path, 'r') as f:
        data = json.load(f)

    def parse_string_to_values(string):
        return list(map(float, string.split()))

    for label in data:
        data[label]["x"] = parse_string_to_values(data[label]["x"])
        data[label]["y"] = parse_string_to_values(data[label]["y"])
    return data


def plot(data, graph_list):
    fig, sub = plt.subplots()
    data_filtered = []
    for number in graph_list:
        data_filtered.append(list(data.items())[number - 1])
    for label, cords in data_filtered:
        sub.scatter(cords["x"], cords["y"], label=label)
        sub.set_xlabel('x label')
        sub.set_ylabel('y label')
        sub.set_title('New Plot')
        sub.legend()


def parse_graph_range():
    graph_count = list(set(map(int, input("Какие графики вывести?: ").split())))
    return graph_count


def main():
    graph_list = parse_graph_range()
    data = parse_json_data(DATA_FILE_PATH)

    if len(graph_list) > len(data.keys()):
        print("Неверно указан диапозон")
        return

    plot(data, graph_list)
    plt.show()


if __name__ == "__main__":
    main()
