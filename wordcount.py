# put your code here.


# def get_words_count(words):
#     """ """

#     words_count = {}

#     for word in words:
#         words_count[word] = words_count.get(word, 0) + 1

#     return words_count


# def get_count_for_words(words_count, word):
#     """ """

#     return word_counts.get(word, 0)


# log_file = open("test.txt")

# for line in log_file:
#     line = line.rstrip()
#     words = line.split(" ") #give collections plural names to indicate they are collections


# counts = get_words_count()

# log_file.close()

# 1) Open file
log_file = open("test.txt")
# 2) Look at file line by line. Also remove white space
# 3) From line to word by word . Also remove spaces. Set = to variable
for line in log_file:
    line = line.rstrip()
    words = line.split(" ")
# 4) Create a blank dictionary
words_count = {}
# 5) Look at first word. If not in, add word, add +1 to value of key.
# 6) If word is in dictionary, return current value and +1

for word in words:
    words_count[word] = words_count.get(word, 0) + 1
print words_count
# 7) print the dictionary.
