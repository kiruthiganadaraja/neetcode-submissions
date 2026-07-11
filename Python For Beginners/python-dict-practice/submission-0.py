from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    my_dict = {}
    for char in word:
        # Correctly add/update the character count in the dictionary
        my_dict[char] = word.count(char)
    # Return the populated dictionary, not the built-in 'dict' type
    return my_dict




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
