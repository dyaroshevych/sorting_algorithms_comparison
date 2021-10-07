import matplotlib.pyplot as plt
import json
import sys


def draw_experment(results_filename: str, experiment_title: str):
    data = json.load(open(results_filename))
    powers = list(range(7, 16))
    y_insertion = []
    y_selection = []
    y_merge = []
    y_shell = []

    for power in powers:
        power_str = str(power)
        y_insertion.append(
            data[power_str][experiment_title]["Insertion Sort"][1])
        y_selection.append(
            data[power_str][experiment_title]["Selection Sort"][1])
        y_merge.append(data[power_str][experiment_title]["Merge Sort"][1])
        y_shell.append(data[power_str][experiment_title]["Shellsort"][1])

    plt.plot(powers, y_insertion)
    plt.plot(powers, y_selection)
    plt.plot(powers, y_merge)
    plt.plot(powers, y_shell)
    plt.yscale('log')

    plt.title(experiment_title)
    plt.xlabel('List Size (2^x)')
    plt.ylabel("Number of comparisons")
    plt.legend(["Insertion Sort", "Selection Sort",
                "Merge Sort", "Shellsort"])
    plt.show()


if __name__ == '__main__':
    results_filename = sys.argv[1]
    experiment_title = sys.argv[2]
    draw_experment(results_filename, experiment_title)
