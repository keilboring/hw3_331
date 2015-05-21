import time
import os
import sys
import re
print os.getcwd()

fo = open("test_text.txt", "r")
x = 0

wordList = []
unqiueWords = []
reviews = []

#parse line by line removing unneeded chacters
for line in fo.readlines():
    x = x + 1
    p = re.compile( '"|\(|\)|\.|\'')
    #print p.sub('',line.split(",")[0])
    reviews.append(p.sub('',line.split(",")[0]))
    for words in p.sub('',line.split(",")[0]).split(" "):
        wordList.append(words)

    #if x == 4:
    #    break
 
    
#get only unique words from list of words   
wordList.sort()
print "\n", "\n"
for words in wordList:
    if wordList.count(words) > 5 :
        #print words , wordList.count(words)
        if unqiueWords.count(words) == 0:
            unqiueWords.append(words)
            print  words, wordList.count(words)





#create file and create header using unique words
if unqiueWords.count('') > 0:
    unqiueWords.remove('')
fw = open("output.txt","w")
for w in unqiueWords:
    fw.write(w + ",")
fw.write("classlabel")

if reviews.count("\n") > 0:
    reviews.remove("\n")
print("\n")
fw.write("n")
#check if review contains unique word
for l in reviews:
    print "~" + l + "~"

    for u in unqiueWords:

        print u
        #re.search(pattern,string)
        if(re.search(u,l)):
            print "!!!!!!!!!!!!!!!!!!FOUND!!!!!!!!!!"
            fw.write("1,")
        else:
            fw.write("0,")
            print "not found"
    fw.write("\n")
    #time.sleep(3)