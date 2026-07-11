from typing import List

def count_unique_words(words: List[str]) -> int:
    words_set = set(words)
    len_of_set = len(words_set)
    if len_of_set < 1:
        len_of_set = 0
    return len_of_set
    

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
