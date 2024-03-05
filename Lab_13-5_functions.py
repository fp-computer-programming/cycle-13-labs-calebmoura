# Author: Caleb A. Moura

# series of functions defined & created to correspond with Lab 13-5.
def sum_of_list(numbers):
    total = sum(numbers)
    return total

def count_words(sentence):
    words = sentence.split()
    num_words = len(words)
    return num_words

def find_max(numbers):
    max_num = max(numbers)
    return max_num

def create_dict(keys, values):
    result_dict = dict(zip(keys, values))
    return result_dict

def even_numbers(numbers):
    even_nums = [num for num in numbers if num % 2 == 0]
    return even_nums

def vowel_count(sentence):
    vowels = "aeiou"
    count = 0
    for char in sentence.lower():
        if char in vowels:
            count += 1
    return count

def capitalize_words(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

def reverse_string(sentence):
    return sentence[::-1]

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def find_index_of_element(lst, element):
    for index, value in enumerate(lst):
        if value == element:
            return index
    return -1