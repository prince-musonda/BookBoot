import sys
from stats import get_num_words
from stats import get_num_individual_chars

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content


def sort_by_value(dictionary:dict):
    # create a new list of distionaries
    items = []
    for key,value in dictionary.items():
        items.append({'name':key, 'count':value})
    # sort the list of dictionaries based on the count
    def sort_on(item):
        return item["count"]
    items.sort(reverse=True,key=sort_on)
    return items

def main(file_path):
    bookContent = get_book_text(file_path)
    number_of_words = get_num_words(bookContent)
    characters_count = get_num_individual_chars(bookContent)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print(f"--------- Character Count -------")
    # sort_dictionary(characters_count)
    sorted_characters_list = sort_by_value(characters_count)
    for character in sorted_characters_list:
        print(f"{character['name']}: {character['count']}")


# get system arguments 
command_line_arguments = sys.argv
if(len(command_line_arguments) < 2):
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
else:
    # get the second CLI argument (which is the book path )
    book_path = command_line_arguments[1]
    main(book_path)