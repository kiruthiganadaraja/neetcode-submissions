from typing import List

def contains_duplicate(words: List[str]) -> bool:
    len_of_list = len(words)
    words_set = set(words)
    len_of_set = len(words_set)
    if len_of_list > len_of_set:
        output = True
    else:
        output = False
    return output
        
    


# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
