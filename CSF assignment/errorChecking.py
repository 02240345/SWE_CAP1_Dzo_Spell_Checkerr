import sys
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        result = chardet.detect(file.read())
        return result['encoding']

def load_dictionary(clean_dictionary):
    
    encoding = detect_encoding(clean_dictionary)
    print(f"Detected encoding for dictionary: {encoding}")

    
    with open(clean_dictionary, 'r', encoding=encoding) as f:
        dictionary = set(word.strip() for word in f.readlines())
    return dictionary

def spell_check(input_file, dictionary):
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    
    for line_num, line in enumerate(lines, start=1):
        words = line.strip().split()
        
        for word_pos, word in enumerate(words, star):
            if word not in dictionary:
                
                print(f"line {line_num}, {word_pos}th word '{word}' is incorrect.")

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python dzongkha_spell_checker.py dzo.txt")
        return

    input_file = sys.argv[1]
    dictionary_file = 'cleaned_dictionary.txt'  

    
    dictionary = load_dictionary(dictionary_file)
    spell_check(input_file, dictionary)

if __name__ == "__main__":
    main()
    