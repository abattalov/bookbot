def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.lower()

    def get_unique_letters(text):
        unique_letter_count = {}

        for letter in text:
            if letter in unique_letter_count:
                unique_letter_count[letter] += 1
            else:
                unique_letter_count[letter] = 1
      
        
        return unique_letter_count

    
    count = get_unique_letters(words)

    print(count)

   

main()

