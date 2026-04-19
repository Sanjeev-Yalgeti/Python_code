import threading
def sort_sublist(sublist, index, results):
    results[index] = sorted(sublist)
def merge_lists(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

if __name__ == "__main__":
    user_input = input("Enter a list of numbers separated by spaces: ")
    numbers = [int(x) for x in user_input.split()]
    mid = len(numbers) // 2
    left_half = numbers[:mid]
    right_half = numbers[mid:]
    results = [None, None]
    t1 = threading.Thread(target=sort_sublist, args=(left_half, 0, results))
    t2 = threading.Thread(target=sort_sublist, args=(right_half, 1, results))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    final_sorted_list = merge_lists(results[0], results[1])
    print(" ".join(map(str, final_sorted_list)))
