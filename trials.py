"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)

list_of_items = [1, 'hello', True]
output_all_items(list_of_items)


def get_all_evens(nums):
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums

numbers_list =[7, 8, 10, 1, 2, 2]
print(get_all_evens(numbers_list))

def get_odd_indices(items):
    result = []
    for idx in range(len(items)):
        if idx % 2 != 0:
            result.append(items[idx])
    
    return result

odd_list = [1, 'hello', True, 500]
print(get_odd_indices(odd_list))


def print_as_numbered_list(items):
    i = 1
    for item in items:
        print(f"{i}. {item}")
        i  += 1

list_items = [1, 'hello', True]
print_as_numbered_list(list_items)


def get_range(start, stop):
    nums = []
    for num in range(start, stop):
        nums.append(num)
    
    return nums

print(get_range(0, 5))
print(get_range(1, 3))


def censor_vowels(word):
    chars = []
    for letter in word:
        if letter in "aeiou":
            chars.append("*")
        else:
            chars.append(letter)

    return "".join(chars)

phrase = 'hello world'
print(censor_vowels(phrase))


def snake_to_camel(string):
    camel_case = []
    for word in string.split("_"):
        camel_case.append(word.capitalize())
    
    return "".join(camel_case)

print(snake_to_camel('hello_world'))


def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if len(word) > longest:
            longest = len(word)

    return longest

word_list = ['jellyfish', 'zebra']
print(longest_word_length(word_list))


def truncate(string):
    result = []

    for char in string:
        if len(result) == 0 or char != result[range(len(result[-1]))]:
            result.append(char)

    return result

function truncate(string) {
  const result = [];

  for (const char of string) {
    if (result.length === 0 || char !== result[result.length - 1]) {
      result.push(char);
    }
  }

  return result.join('');
}


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
