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

    
