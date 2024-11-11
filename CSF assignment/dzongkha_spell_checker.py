import sys

def load_dictionary(dictionary_file):
    # Put dictionary into a set to make through out easier and quick
    with open(dictionary_file, 'r', encoding='utf-8') as file:
        # Open the dictionary file, read line by line. Make sure to remove any leading or trailing spaces before inserting into a set.
        return set(word.strip() for word in file if word.strip())

def check_dzongkha_spelling(input_file, dictionary):
    # Verify all the Dzongkha terms contained in the input document with the respective dictionary.
    with open(input_file, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            words = line.strip().split()
            for position, word in enumerate(words, start=1):
                # Check if the word is in the dictionary
                if word not in dictionary:
                    print(f"Line {line_number}, Position {position}: {word}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python dzongkha_spell_checker.py <input.txt> <filtered_dictionary.txt>")
        sys.exit(1)

    input_file = sys.argv[1]
    dictionary_file = sys.argv[2]

    # Load the dictionary
    dictionary = load_dictionary(dictionary_file)

    # Check spelling of dzongkha words in the input file
    check_dzongkha_spelling(input_file, dictionary)

if __name__ == "__main__":
    main()