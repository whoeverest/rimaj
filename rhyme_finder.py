import sys
from os import path

vowels = ['а', 'е', 'и', 'о', 'у']

with open('zborovi.txt', 'r') as f:
    list_of_words = f.readlines()

list_of_words = [word.strip() for word in list_of_words]

def count_vowels(word):
    counter = 0
    for i, letter in enumerate(word):
        if letter in vowels:
            counter += 1
        elif i > 0 and i < len(word) - 2 and letter == 'р' and word[i-1] not in vowels and word[i+1] not in vowels:
            counter += 1
    return counter

# todo: rimuvaj so 'r'
# todo: rimuvaj ednoslozhni
# todo: metrika za kvalitet na rimite

def extract_part_beyond_samoglaska(word, koja):
    num_found_vowels = 0
    word_ending_reversed = ''
    for letter in word[::-1]:
        word_ending_reversed += letter
        if letter in vowels:
            num_found_vowels += 1
            if num_found_vowels == koja:
                return word_ending_reversed[::-1]
    return word_ending_reversed[::-1]

'''
Searches through the dictionary for words that rhyme. :D
'''
def find_rhymes(our_word):
    rhymes = []
    for dict_word in list_of_words:
        our_vowel_count = min(count_vowels(our_word), 3)
        dict_vowel_count = count_vowels(dict_word)
        
        dict_word_ending = extract_part_beyond_samoglaska(dict_word, our_vowel_count)
        our_word_ending = extract_part_beyond_samoglaska(our_word, our_vowel_count)

        if dict_word_ending == our_word_ending and dict_word != our_word:
            if our_vowel_count < 3 and dict_vowel_count > our_vowel_count:
                continue
            rhymes.append(dict_word)
    return rhymes

if sys.argv[1] == 'еренес':
    print('веренатеренот!')
    exit(0)

for rhyme in find_rhymes(sys.argv[1]):
    print(rhyme)