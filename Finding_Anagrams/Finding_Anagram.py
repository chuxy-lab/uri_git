# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    # rm excess space
    replace_word = word.replace(" ", "")
    replace_anagram = anagram.replace(" ", "")
    # sort letters
    sort_word = sorted(replace_word)
    sort_anagram = sorted(replace_anagram)


    # tracker
    track_letters = dict()
    
    # first check: length
    if len(sort_word) != len(sort_anagram):
        return "This is not anagram"
   
    # second check: add
    for loop_over_word in sort_word:
        if loop_over_word in track_letters:
            track_letters[loop_over_word] += 1
        else:
            track_letters[loop_over_word] = 1
    # third check: remove
    for loop_over_word in sort_anagram:
        if loop_over_word in track_letters:
            track_letters[loop_over_word] -= 1
        else:
            track_letters[loop_over_word] = 1 
    # fouth check: net = 0
    for loop_over_word in track_letters:
        if track_letters[loop_over_word] != 0:
            return "This is not anagram"
    return "This is anagram"

print(find_anagram('below', 'elbow'))