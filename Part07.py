# Part 7

# The Bells
# Edgar Allen Poe
theBells = '''HEAR the sledges with the bells,
Silver bells!
What a world of merriment their melody foretells!
How they tinkle, tinkle, tinkle,
In the icy air of night!
While the stars, that oversprinkle
All the heavens, seem to twinkle
With a crystalline delight;
Keeping time, time, time,
In a sort of Runic rhyme,
To the tintinnabulation that so musically wells
From the bells, bells, bells, bells,
Bells, bells, bells--
From the jingling and the tinkling of the bells.
'''

# Canto XII from The Heights of Macchu Picchu
# Pablo Neruda
cantoXII = '''Arise to birth with me, my brother.
Give me your hand out of the depths
sown by your sorrows.
You will not return from these stone fastnesses.
You will not emerge from subterranean time.
Your rasping voice will not come back,
nor your pierced eyes rise from their sockets.
'''

import string

def litCricFriend(wordList, text):
    ''' The Literary Critic's Friend helps the humanities scholar
    by computing and returning the frequency with which specified words
    (wordList) appear in a body of text (text). Frequency is
    the sum of the number of times that each word in wordList
    occurs, divided by the number of words in the text. A word
    occurrence is the whole word, regardless of case, and
    excluding punctuation.'''
    
    # Problem 1: Lowercasign the text
    text = text.lower()
    
    # Problem 2: Replacing m-dash ('--') with a space (' ')
    text = text.replace('--', ' ')
    
    # Problem 3: Spliting text into a list of words
    words = text.split()
    
    # Problem 4: Striping punctuation from each word
    
    stripped_words = [word.strip(string.punctuation) for word in words]
    
    '''
    stripped_words = []
    for word in words:
        cleaned_word = word.strip(string.punctuation)
        stripped_words.append(cleaned_word)
    '''
    
    # Problem 5: Counting occurrences of words in wordList
    word_count = sum(stripped_words.count(word.lower()) for word in wordList)
    
    '''
    word_count = 0
    for word in wordList:
        word_count += stripped_words.count(word.lower())
    '''
    
    # Problem 6: Calculating the ratio of word occurrences to total words
    frequency = word_count / len(stripped_words) if len(stripped_words) > 0 else 0

    return frequency

# Problem 7: Testing frequencies in both poems
bells_a_an_frequency = litCricFriend(['a', 'an'], theBells)
bells_the_frequency = litCricFriend(['the'], theBells)
canto_a_an_frequency = litCricFriend(['a', 'an'], cantoXII)
canto_the_frequency = litCricFriend(['the'], cantoXII)

# results getting print
print("bells_a_an_frequency:", bells_a_an_frequency)
print("bells_the_frequency:", bells_the_frequency)
print("canto_a_an_frequency:", canto_a_an_frequency)
print("canto_the_frequency:", canto_the_frequency)

'''
PROBLEM 8 Analysis:
The results suggest that Poe's usage of "the" in "The Bells" is significantly higher than Neruda's in "Canto XII,"
indicating a more frequent emphasis on specific, definite objects or ideas. Poe also uses "a" and "an" to a small degree,
while Neruda's usage of indefinite articles is absent, possibly reflecting his broader, more universal tone.
'''
