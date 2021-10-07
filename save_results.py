from generate_nums import get_123_nums, get_random_nums, get_sorted_ascending_nums, get_sorted_descending_nums
from sorting import insertionsort, selectionsort, mergesort, shellsort
import time
import json
import copy

EXPERIMENTS = {
    "Randomized list": get_random_nums,
    "Sorted list (ascending)": get_sorted_ascending_nums,
    "Sorted list (descending)": get_sorted_descending_nums,
    "List with elements {1, 2, 3}": get_123_nums,
}

SORTING_ALGORITHMS = {
    "Insertion Sort": insertionsort,
    "Selection Sort": selectionsort,
    "Merge Sort": mergesort,
    "Shellsort": shellsort
}

results = {}

for experiment_title, generate_list in EXPERIMENTS.items():
    for power in range(7, 16):
        if power not in results:
            results[power] = {
                experiment_title: {}
            }

        nums = generate_list(2 ** power)

        for algorithm_name, sort_nums in SORTING_ALGORITHMS.items():
            start = time.time()
            num_comparisons = sort_nums(copy.copy(nums))
            execution_time = time.time() - start

            if experiment_title not in results[power]:
                results[power][experiment_title] = {}
            results[power][experiment_title][algorithm_name] = (
                execution_time, num_comparisons)
            print((execution_time, num_comparisons))

with open("results.json", "w") as f:
    json.dump(results, f)
