def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    count_dict = get_count_dict(text)
    num_words = get_num_words(text)
    
    count_list = [i for i in count_dict.items() if i[0].isalpha()]
    count_list.sort(key= lambda a: a[1], reverse=True)

    print(f"--- Report for {book_path} ---\n")
    print(f"{num_words} words were found\n")
    for val in count_list:
        print(f"The {val[0]} character was found {val[1]} times")
    print("\n--- End of Report ---")


def get_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(content):
    return len(content.split())

def get_count_dict(content):
    count_dict = {}
    for i in content:
        lowercase_char = i.lower()
        if lowercase_char in count_dict:
            count_dict[lowercase_char] += 1
        else:
            count_dict[lowercase_char] = 1
    return count_dict


main()