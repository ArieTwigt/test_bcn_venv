# function to remove all vowels from a name


def remove_vowels(name):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        name = name.replace(vowel, '')
    return name