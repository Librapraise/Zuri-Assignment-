import string
common_punctuations = list(string.punctuation)
def find_anagram(word, anagram):
    #Covert to list with spaces as delimiters
    word_list , anagram_list= word.lower().split(), anagram.lower().split()

    #add all members of list so there'd be no more space if there is in the original string
    good_word = ''
    for each_word in word_list:
        for char in each_word:
            if char in common_punctuations:
                continue
            else:
                good_word += char

    good_anagram = ''
    for each_word in anagram_list:
        for char in each_word:
            if char in common_punctuations:
                continue
            else:
                good_anagram += char

    #Rearrange them and check if they are the same
    if sorted(good_word) == sorted(good_anagram):
        return True
    else:
        return False

print(find_anagram('Big man','nab-mig'))
print(find_anagram('Church of Scientology','rich-chosen goofy cult'))
