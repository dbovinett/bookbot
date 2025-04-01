def word_count(text):
    word_list = text.split()
    word_count_length = len(word_list)
    return word_count_length

def letter_count(text):
    text = text.lower()
    letter_counts = {}

    for c in text:
        if c.isalpha():
            try:
                letter_counts[c] = letter_counts[c] + 1
            except Exception as e:
                letter_counts[c] = 0
                letter_counts[c] = letter_counts[c] + 1
    return letter_counts

def dict_sort(letter_counts):
    x = dict(sorted(letter_counts.items(), key=lambda item: item[1],reverse=True))
    return x