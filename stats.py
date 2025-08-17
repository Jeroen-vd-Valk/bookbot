def count_number_words(text):
    words = text.split()
    return len(words)

def count_number_characters(text):
    letters = {}
    
    for character in text:
        character = character.lower()
        if(character in letters):
            letters[character] += 1
        else:
            letters[character] = 1

    return letters

def sort_on(items):
    return items["num"]

def sort_dictionary(dictionary_to_sort):
    sorting_dictionary = []
    
    for item in dictionary_to_sort:
        sorting_dictionary.append({"char": item, "num": dictionary_to_sort[item]})

    
    sorting_dictionary.sort(reverse=True, key=sort_on)

    return sorting_dictionary
