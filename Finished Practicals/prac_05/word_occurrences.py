word_counting = {}
user_text = input("Text: ")
words = user_text.split()
for word in words:
    word_frequency = word_counting.get(word, 0)
    word_counting[word] = word_frequency + 1
words = list(word_counting.keys())
words.sort()
max_word_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_word_length, word_counting[word]))
