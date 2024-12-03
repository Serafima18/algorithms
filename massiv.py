def find_min_pairs(arr):
    new_arr = []
    for i in range(0, len(arr), 2):
        if i + 1 < len(arr):  # Если есть пара
            min_value = min(arr[i], arr[i + 1])
            new_arr.append(min_value)
        else:  # Если нечетное количество
            new_arr.append(arr[i])
    return new_arr

def create_tree_array(original_array):
    current_array = original_array[:]
    history = []

    while len(current_array) > 1:
        current_array = find_min_pairs(current_array)
        history.append(current_array)

    final_value = current_array[0]  # Это будет единственный элемент
    result_array = [final_value] * len(history) + [item for sublist in history for item in sublist] + original_array

    result_array = [final_value] + [item for sublist in history for item in sublist] + original_array

    return result_array

original_array = [5, 1, -2, 3, 7, 0, 10, 8]
final_result = create_tree_array(original_array)
print(final_result)
