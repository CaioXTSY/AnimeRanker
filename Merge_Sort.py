import json

def popularity_key(anime):
    return anime['popularity']

def merge_sort(animes, key_func):
    if len(animes) <= 1:
        return animes

    mid = len(animes) // 2
    left = merge_sort(animes[:mid], key_func)
    right = merge_sort(animes[mid:], key_func)

    return merge(left, right, key_func)

def merge(left, right, key_func):
    merged = []
    left_idx = right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if key_func(left[left_idx]) < key_func(right[right_idx]):
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1

    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])

    return merged

def load_animes(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_sorted_animes(file_name, sorted_animes):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(sorted_animes, file, indent=2)

animes = load_animes('animes.json')
sorted_animes = merge_sort(animes, popularity_key)
save_sorted_animes('animes_ordered_merge.json', sorted_animes)
