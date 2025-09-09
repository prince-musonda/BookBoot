def get_num_words(text):
    word_list = text.split()
    return len(word_list)


def get_num_individual_chars(text:str):
    text = text.lower()
    characters = {}
    for i in range(0,len(text)):
        #check if character already exists in characters dictionary
        item = characters.get(text[i])
        # if it doesn't exist
        if(not item):
            count = text.count(text[i])
            characters[text[i]] = count
        
    return characters
