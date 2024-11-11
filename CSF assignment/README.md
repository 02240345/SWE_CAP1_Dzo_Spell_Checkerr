## https://github.com/02240345/SWE_CAP1_Dzo_Spell_Checkerr.git


## karma Choing Zangmo
## A
## 02240345


# REFERENCES

## 


# SOLUTION

# Dzongkha Spell Checker

## Project Overview
The Dzongkha Spell Checker is a comprehensive project aimed at improving the accuracy and consistency of written Dzongkha. This project combines a robust dictionary cleaning tool with a spell-checking mechanism to support writers, educators, and language enthusiasts in producing high-quality Dzongkha text.



## Table of Contents

1.Usage   
2.Implementation   
3.Data Strucutures    
4.Algorithms   
5.Challenges and Solutions    
7.References



## 1.Usage

The Dzongkha Spell Checker project consists of two main components: 

1.input.txt: The text file to be checked for misspelled words.

2.filtered_dictionary.txt: A file containing correct Dzongkha terms, one word per line, which serves as the 
dictionary for spell-checking.




## 2. Implementation

The Dzongkha Spell Checker project is implemented in Python and consists of two main components:  

1.load_dictionary(): Loads words from a dictionary file into a set for efficient searching.

2.check_dzongkha_spelling(): Reads through each word in the input file and checks if it exists in the dictionary
set. If a word is not found in the dictionary, the program outputs the line number and word position.





## Data Structures

The Dzongkha Spell Checker project utilizes several data structures to efficiently store and process the dictionary 
and perform spell checking. 

Each line of the input file is split into a list of words for word-by-word verification.



### Set for Dictionary Storage

The cleaned Dzongkha dictionary is stored in memory using a Python `set` data structure.


### List for Suggestion Storage
When generating spelling suggestions, a Python list is used to store potential corrections.





## Algorithms

The Dzongkha Spell Checker employs several algorithms to perform its core functionalities. 

1.Loading the Dictionary: Each word from the dictionary file is stripped of extra spaces and stored in a set, 
ensuring that there are no duplicates and allowing for fast lookup.

2.Spell Checking: The script reads through the input file line by line, checking each word. If a word is not in the 
dictionary, it outputs its line and position.


## Challenges and Solutions

1.Challenge: Handling large dictionary files efficiently.

Solution: Using a set for the dictionary allows for fast lookups and efficient memory usage.

2.Challenge: Ensuring Unicode support for Dzongkha.

Solution: The script opens files with UTF-8 encoding, which supports Dzongkha characters.







## References
### Chat gpt
### Tabnine ai
### Cloudcovert
### codeacademy