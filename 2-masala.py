def is_vowel_in_there(s):
    return any(char in 'aeiou' for char in s)
print(is_vowel_in_there("hello"))