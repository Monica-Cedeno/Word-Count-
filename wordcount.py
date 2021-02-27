"""Count the words in a file"""

space_count = open('./test.txt')
#open the text

#empy dict
word_counter= {}    

for line in space_count:
    line = line.rstrip()
    words = line.split()

    for word in words:
        word_counter[word] = word_counter.get(word, 0)+1

for word, count in word_counter.items():
   print (word, count)
