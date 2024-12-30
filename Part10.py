# Part 10

# Problem 1

def initialLetterCount(wordList):

    initial_count = {}

    for word in wordList:
        
        initial = word[0]
        
        if initial in initial_count:
            initial_count[initial] += 1
        else:
            initial_count[initial] = 1
    
    return initial_count


horton1 = ['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']
print(initialLetterCount(horton1), "\n")

# Problem 2

def initialLetters(wordList):

    result = {}
    

    for word in wordList:

        initial = word[0].lower()

        if initial not in result:
            result[initial] = []
        
        if word not in result[initial]:
            result[initial].append(word)
    
    return result


horton2 = ['I', 'say', 'what', 'I', 'mean', 'and', 'mean']
print(initialLetters(horton2), "\n")

# Problem 3

def shareOneLetter(wordList):
    result = {}

    for word in wordList:

        shared_words = []

        for other_word in wordList:

            has_common_letter = False
            for letter in word:
                if letter in other_word:
                    has_common_letter = True
                    break

            if has_common_letter and other_word not in shared_words:
                shared_words.append(other_word)

        result[word] = shared_words

    return result


horton3 = ['I', 'say', 'what', 'mean', 'and']
print(shareOneLetter(horton3), "\n")
