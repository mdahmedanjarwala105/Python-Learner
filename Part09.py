# Part 9

# Problem 1

def file_copy(in_file, out_file):
    """
    Copies the content of in_file to out_file.
    """
    # Opening the input file in read mode
    source_file = open(in_file, 'r')
    content = source_file.read()
    source_file.close()

    # Opening the output file in write mode
    destination_file = open(out_file, 'w')
    destination_file.write(content)
    destination_file.close()


file_copy('created_equal.txt', 'copy.txt')

# Opening the copied file to verify the result
copy_f = open('copy.txt')
print(copy_f.read())
copy_f.close()

# Problem 2:

def file_stats(in_file):
    """
    Calculates and prints the number of lines, words, and characters in a text file.
    """
    # Opening the input file in read mode
    file = open(in_file, 'r')
    lines = file.readlines()
    file.close()

    # Calculating statistics
    num_lines = len(lines)
    num_words = 0
    num_characters = 0

    # Iterate through each line to calculate word and character counts
    for line in lines:
        num_words += len(line.split())
        num_characters += len(line)

    # Printing the statistics
    print("lines", num_lines)
    print("words", num_words)
    print("characters", num_characters)


file_stats('created_equal.txt')

# Problem 3

import string

def repeat_words(in_file, out_file):
    """
    Identifies words that appear more than once on each line of the input file and writes them to the output file.
    Words are converted to lowercase and stripped of punctuation before comparison.
    """
    # Opening the input file for reading
    input_file = open(in_file, 'r')
    lines = input_file.readlines()
    input_file.close()

    # Opening the output file for writing
    output_file = open(out_file, 'w')

    # Processing each line of the input file
    for line in lines:
        words = line.split()

        cleaned_words = []
        for word in words:
            cleaned_word = word.strip(string.punctuation).lower()
            cleaned_words.append(cleaned_word)

        seen = []
        repeated = []
        for word in cleaned_words:
            if word in seen and word not in repeated:
                repeated.append(word)
            elif word not in seen:
                seen.append(word)

        repeated.sort()

        output_string = ''
        for word in repeated:
            output_string += word + ' '
        
        output_file.write(output_string.strip() + '\n')

    # Closing the output file after writing
    output_file.close()


inF = 'catInTheHat.txt'
outF = 'catRepWords.txt'
repeat_words(inF, outF)

output_file = open(outF, 'r')
print(output_file.read())
output_file.close()
