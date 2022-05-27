import string
alphabet_string_u = string.ascii_uppercase
alphabet_string_u = list(alphabet_string_u)
alphabet_string_l = string.ascii_lowercase
alphabet_string_l = list(alphabet_string_l)
all_letters = alphabet_string_l + alphabet_string_u


def read_file_content(filename):
    """To read files and take care of punctuations at the end of words"""
    with open(filename) as fhandle:
        file = fhandle.readlines()
        words_only = []
        for sentences in file:
            sentence = sentences.split()
            for words in sentence:
                if words[len(words)- 1] in all_letters:
                    words_only.append(words)
                else:
                    nice_letter = words.replace(words[len(words)-1] , '')
                    words_only.append(nice_letter)

    return words_only


def count_words():
    """To count words and assign them to dict"""
    my_dict = {}
    text = read_file_content('story.txt')
    for words in text:
        if words in my_dict:
            my_dict[words] += 1
        else:
            my_dict[words] = 0
            my_dict[words] += 1
    return my_dict

print(count_words())
