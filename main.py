def get_dictionary():
    words = []
    with open('all_dict.txt', encoding='utf-8') as f:
        for line in f:
            line = line.strip().lower()
            x = line.split(',')
            if len(x) == 2:
                pair = x[0], x[1]
                words.append(pair)
    return words


words = get_dictionary()

w = 'sleep'

for pair in words:
    if w == pair[0]:
        print(pair[1])
