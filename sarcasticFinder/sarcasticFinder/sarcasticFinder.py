import time
import os
import sys
import re
print os.getcwd()

fo = open("training_text.txt", "r")
x = 0

wordList = []
unqiueWords = []
reviews = []


#parse line by line removing unneeded chacters
for line in fo.readlines():
    x = x + 1
    p = re.compile( '"|\(|\)|\.|\'|-')
    line = p.sub(' ',line.lower())


    temp = line.split(",")[:-1]
    temp2 = line.split(",")[-1]   # 0 or 1 
    temp = ''.join(temp)

    if temp != "":
        reviews.append(temp2 + ' ' + temp)
        for words in p.sub('',line.lower().split(",")[0]).split(" "):
            wordList.append(words)

    
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
fw.write("\n")
#check if review contains unique word
for l in reviews:
    #print "~" + l + "~"

    for u in unqiueWords:

        #print u
        #re.search(pattern,string)

        if(re.search(r'\b' + u + r'\b' ,l)):
            #print "!!!!!!!!!!!!!!!!!!FOUND!!!!!!!!!!"
            fw.write("1,")
        else:
            fw.write("0,")
            #print "not found"
    fw.write(l[0] + "\n")
    #time.sleep(3)



##
cnt = 0
for l in reviews:
    key = "about"
    label = "0"
    if l[0] == label:
        if(re.search(r'\b' + key + r'\b' ,l)):
            cnt = cnt + 1
print "number of 1's =" + str(cnt) 


input_string = "This IPOD has a lot of problems and in my opinion is NOT worth the inflated cost."

for u in unqiueWords:
    cnt = 0
    #input contains keyword
    if(re.search(r'\b' + u + r'\b' ,input_string)):
        for l in reviews: 
            if l[0] == "1":
                if(re.search(r'\b' + u + r'\b' ,l)):
                    cnt = cnt + 1
        print "key found=" + u + "\t\t" + str(cnt)
   #input does not contain keyword so count # of reviews that dont have keyword
    else:
        for l in reviews: 
            if l[0] == "1":
                if(not re.search(r'\b' + u + r'\b' ,l)):
                    cnt = cnt + 1
        print "key not found=" + u + "\t\t" + str(cnt)