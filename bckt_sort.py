import json

def rank_key(anime):
    return anime['popularity']

def bckt_sort(animes, num_buckets, key_func):
    key_val = [key_func(item) for item in animes]
    min_val, max_val = min(key_val), max(key_val)

    bucket_size = (max_val - min_val + 1) / num_buckets

    buckets = [[] for _ in range(num_buckets)]

    for item in animes:
        val = key_func(item)
        bucket_index = int((val - min_val) / bucket_size)
        buckets[bucket_index].append(item)

    for i in range(num_buckets):
        buckets[i] = sorted(buckets[i], key=key_func)

    sorted_database = []

    for bucket in buckets:
        sorted_database += bucket
    return sorted_database

def load_animes(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)
    
def save_sorted_animes(file_name, sorted_animes):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(sorted_animes, file, indent=2)    

animes = load_animes('animes.json')
num_buckets = 10
sorted_animes = bckt_sort(animes, num_buckets, rank_key)
save_sorted_animes('animes_ordered_bucket.json', sorted_animes)
