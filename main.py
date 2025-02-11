def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.lower()

    def get_unique_letters(text):
        unique_letter_count = {}

        for letter in text:
            if letter.isalpha():
                if letter in unique_letter_count:
                    unique_letter_count[letter] += 1
                else:
                    unique_letter_count[letter] = 1
      
        
        return unique_letter_count

    
    count = get_unique_letters(words)

    list_of_dicts = []

    for key in count:
        dict = {key: count[key]}
        list_of_dicts.append(dict)
    
    sorted_list = sorted(list_of_dicts, key=lambda x: list(x.values())[0], reverse=True)

    # print(sorted_list)

    for item in sorted_list:
        key = list(item.keys())[0]
        value = list(item.values())[0]
        print(f"The '{key}' character was found {value} times")

main()

