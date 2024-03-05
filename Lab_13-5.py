# Author: Caleb A. Moura

def sum_of_list(numbers):
    total = sum(numbers)
    return total

# 4 functions from lab_13-5_functions.py called and used.
numbers = [1, 2, 3, 4, 5]
print("Sum of numbers:", sum_of_list(numbers))

def count_words(sentence):
    words = sentence.split()
    num_words = len(words)
    return num_words

sentence = "Hello, good morning to you."
print("Number of words:", count_words(sentence))

def find_max(numbers):
    max_num = max(numbers)
    return max_num

print("Maximum number:", find_max(numbers))

def create_dict(keys, values):
    result_dict = dict(zip(keys, values))
    return result_dict

keys = ["a", "b", "c"]
values = [1, 2, 3]
print("Created dictionary:", create_dict(keys, values))