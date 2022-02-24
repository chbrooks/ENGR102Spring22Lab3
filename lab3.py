## Lab 3: Word counting.

## In this lab, we'll build a tool to construct a Frequency Distribution.
## This is a dictionary that maps words to the number of times they occur in a file.

## Task 1. To begin, let's make a function called countWords. It should take as input the name of
## a file, use with to open the file, and read in easch line and print them out.


### Task 2. Modify this to only print the lines that contain text. (Hint: they have len > 1)

## But what we really need are words.
## To count words, we need to divide the string into substrings. We can do this with split()
line1 = "May the Force be with you"
line1.split()

## by default, split uses whitespace. To split on another character, provide that character as an argument.
jedi="anakin,obi-wan,yoda,mace windu,qui-gon jinn"
jedi.split(',')

### Task 3. Modify your countWords function so that it splits lines on spaces and prints each word.


### What we really  want is to know how many times *each* word occurs. To do this, we need
## a way to count each word separately.
#
# To do this, we'll use a dictionary. A dictionary is a data structure that maps keys to values. It's one of the most
# common and versatile structures in Python.

# We declare an empty dictionary with {} or with dict()

wordCount = {}

# We then store things in the dictionary by referencing the key:
wordCount['dagobah'] = 1

# We can look them up the same way.

print(wordCount['dagobah'])

## We can then do something like this to count words.
wordCount = {}
SWString = "Fear is the path to the dark side. Fear leads to anger; anger leads to hate; hate leads to suffering. I sense much fear in you."
SWwords = SWString.split()

for word in SWwords :
    if word in wordCount :
        wordCount[word] = wordCount[word] + 1
    else :
        wordCount[word] = 1

### Task 5. Modify your countWords function to generate a count of all the words in the input file.

### ------------------------

## If you look carefully at the code above, you'll see a problem. It counts 'Fear' and 'fear' differently - the first
## one is capitalized. We'd like to treat them all the same. Luckily, we can convert strings with lower() and upper()

dv = "Darth Vader"
print(dv.lower())
print(dv.upper())

### Task 6. Modify your countWords function to convert all the words to lower case before counting them.


### -------------------------

## But wait - there's another problem! some words have punctuation attached to them.
## We could write code to consider every possible punctuation mark and strip those off, but that sounds like a lot
## of work. Luckily, Python is here to help us.
## Built into the string module is a variable containing all the punctuation characters. We can use that with strip()
## to strip any of the punctuation characters. (note that this will only remove leading and trailing characters.)

import string
print string.punctuation

message="Use the Force, Luke!"
messageWords = message.split()
for word in messageWords :
    print(word.strip(string.punctuation))

### Task 7. Modify your countWords again to first strip punctuation, then convert to lower case before counting.

##--------------

### finally, if we look at our word counts, we can see that the most common words are 'the' and 'of'.
### These are examples of stopwords. Stopwords are words that don't contain any content that helps us
### identify what a document is about. In some tasks, such as classification, it's helpful to skip them.

## let's make a list called stopwords.

stopwords = ['a','an','the','in','of','he','she']

## We can test whether a word is in this list with the in keyword

print('of' in stopwords)
print('jedi' in stopwords)

### 8. Modify your countWords function one last time to skip over words that are in our list of stopwords.

