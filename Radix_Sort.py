import json

def popularity_key(anime):
    # Retorna o valor de "popularity" do dicionário do anime
    return anime['popularity']

def get_digit(item, key_func, digit_position):
    # Retorna o dígito na posição especificada usando a função-chave
    return int(key_func(item) / (10 ** digit_position)) % 10

def radix_sort(arr, key_func):
    # Classifica o array usando o algoritmo radix sort com base na função-chave
    max_val = max(arr, key=key_func)
    max_digits = len(str(key_func(max_val)))

    for digit_position in range(max_digits):
        buckets = [[] for i in range(10)]

        for item in arr:
            digit = get_digit(item, key_func, digit_position)
            buckets[digit].append(item)

        arr = [item for bucket in buckets for item in bucket]

    return arr

def load_animes(file_name):
    # Carrega os dados do anime de um arquivo JSON e os retorna
    with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_sorted_animes(file_name, sorted_animes):
    # Salva os dados dos animes ordenados em um arquivo JSON
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(sorted_animes, file, indent=2)

animes = load_animes('animes.json')
sorted_animes = radix_sort(animes, popularity_key)
save_sorted_animes('animes_ordered_radix.json', sorted_animes)