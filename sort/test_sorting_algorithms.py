from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from heap_sort import heap_sort
import random
import matplotlib.pyplot as plt

sizes = {
    '1000': 1000,
    '2000': 2000,
    '4000': 4000,
    '8000': 8000,
    '16000': 16000,
    '32000': 32000
}

algorithms = {
        'Heap_sort': heap_sort,
        'Merge_sort': merge_sort,
        'Quick_sort': quick_sort,
        'Insertion_sort': insertion_sort
    }

def generate_test_cases(sizes): 
    test_cases = {}
    for size_name, size in sizes.items():
        sorted_array = sorted([random.randint(-10*6, 10*6) for _ in range(size)])
        reversed_array = sorted_array[::-1]
        duplicates_array = [random.randint(0, size//10) for _ in range(size)]  # יותר כפילויות
        mixed_signs_array = [random.randint(-10*6, 10*6) for _ in range(size)]
        mixed_types_array = [random.uniform(-10*6, 10*6) for _ in range(size)]
        test_cases[size_name] = {
            "sorted": sorted_array,
            "reversed": reversed_array,
            "duplicates": duplicates_array,
            "mixed_signs": mixed_signs_array,
            "mixed_types": mixed_types_array
        }

    return test_cases

def test_algorithm(algo, arr):
    copy_arr = arr[:]
    comparisons_count, initializations_count = algo(copy_arr)
    python_sorted = sorted(arr)
    return copy_arr == python_sorted, comparisons_count, initializations_count

def evaluate_algorithm(sizes, algorithms):
    test_cases = generate_test_cases(sizes)
    
    result = {}
     
    for algo_name, algo in algorithms.items():
        for size_name, cases in test_cases.items():
            for case_name, case in cases.items():

                is_correct, comparisons_count, initializations_count = test_algorithm(algo, case)
                
                if not is_correct:
                    raise Exception(f"Algorithm {algo_name} failed on test case {case_name}.")

                this_test = [size_name, comparisons_count, initializations_count, comparisons_count + initializations_count]
                result.setdefault(algo_name, {}).setdefault(case_name, []).append(this_test)
    
    return result

def plot_algorithm_results(results):
    plt.figure(figsize=(15, 8))
    
    first_algo = list(results.keys())[0] 
    first_algo_data = results[first_algo]
    case_types = list(first_algo_data.keys())

    rows = 2  
    cols = 3  
    for idx, case_type in enumerate(case_types, 1):
        plt.subplot(rows, cols, idx)
        
        for algo, cases in results.items():
            case_data = cases[case_type]
            sizes = [test[0] for test in case_data]
            operations = [test[-1] for test in case_data]
            
            plt.loglog(sizes, operations, marker='o', label=algo, linewidth=2)
        
        plt.title(f"{case_type}", fontsize=10)
        plt.xlabel("Input Size (log)", fontsize=8)
        plt.ylabel("Operations (log)", fontsize=8)
        plt.grid(True, which="both", ls="-", alpha=0.2)
        plt.legend(fontsize=7)
        plt.tick_params(labelsize=8)
    
    plt.tight_layout(pad=1.5)
    plt.show()
    
    plt.tight_layout()
    plt.show()
    
test_res = evaluate_algorithm(sizes, algorithms)

print(test_res)
plot_algorithm_results(test_res)