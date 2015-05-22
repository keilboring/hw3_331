import time
import os
import sys
import re
print os.getcwd()
import math
import operator
import functools
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
fw = open("output.csv","w")
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


sarcastic_answer = []

LabelCnt1 = 0
for l in reviews:
    sarcastic_answer.append(l[0])
    if l[0] == "1":
        LabelCnt1 = LabelCnt1 + 1
print "number of sarcastic 1's =" + str(LabelCnt1) 


LabelCnt0 = 0
for l in reviews:
    if l[0] == "0":
        LabelCnt0 = LabelCnt0 + 1
print "number of non-sarcastic 0's =" + str(LabelCnt0) 

P1 = float(LabelCnt1) / (float(LabelCnt1) + float(LabelCnt0))
P0 = float(LabelCnt0) / (float(LabelCnt0) + float(LabelCnt1))

#input_string = "just washed my sisters car, got totally soaked coz the actual hose thing came off, but i did a good job i guess."

sarcastic_guess = []
for input_string in reviews:
    print input_string
    #Check aP(when class = 1)
    PC1 = [float(P1)]
    for u in unqiueWords:
        probability = 0 
        cnt = 0
        #input contains keyword
        if(re.search(r'\b' + u + r'\b' ,input_string)):
            for l in reviews: 
                if l[0] == "1":
                    if(re.search(r'\b' + u + r'\b' ,l)):
                        cnt = cnt + 1
            #print "key found=" + u + "\t\t" + str(cnt)
            #probability = float(cnt) + 1) / (float(LabelCnt1) + float(len(unqiueWords))  
            probability = float(cnt)  / (float(LabelCnt1) )  
            #print "prob=" + str(probability)
       #input does not contain keyword so count # of reviews that dont have keyword
        else:
            for l in reviews: 
                if l[0] == "1":
                    if(not re.search(r'\b' + u + r'\b' ,l)):
                        cnt = cnt + 1
            #print "key not found=" + u + "\t\t" + str(cnt)
            #probability = float(cnt) + 1) / (float(LabelCnt1) + float(len(unqiueWords))  
            probability = float(cnt)  / (float(LabelCnt1) )  
            #print "prob=" + str(probability)
        PC1.append( probability)
        #print PC1

    #Check aP(when class = 0)
    PC0 = [float(P0)]
    for u in unqiueWords:
        cnt = 0
        probability = 0 
        #input contains keyword
        if(re.search(r'\b' + u + r'\b' ,input_string)):
            for l in reviews: 
                if l[0] == "0":
                    if(re.search(r'\b' + u + r'\b' ,l)):
                        cnt = cnt + 1
            #print "key found=" + u + "\t\t" + str(cnt)
            #probability = ((float(cnt) + 1) / (float(LabelCnt0) + float(len(unqiueWords))  ))
            probability = float(cnt)  / (float(LabelCnt0) )  
            #print "prob=" + str(probability)
       #input does not contain keyword so count # of reviews that dont have keyword
        else:
            for l in reviews: 
                if l[0] == "0":
                    if(not re.search(r'\b' + u + r'\b' ,l)):
                        cnt = cnt + 1
            #print "key not found=" + u + "\t\t" + str(cnt)
            #probability = ((float(cnt) + 1) / (float(LabelCnt0) + float(len(unqiueWords))  ))
            probability = float(cnt)  / (float(LabelCnt0) )  
            #print "prob=" + str(probability)
        PC0.append( probability)
        #print PC0


    print "PC0 = " + str(functools.reduce(operator.mul,PC0))
    print "PC1 = " + str(functools.reduce(operator.mul,PC1))
    if( functools.reduce(operator.mul,PC0) > functools.reduce(operator.mul,PC1)):
        sarcastic_guess.append("0")
        print "PC0 was bigger"
    else:
        sarcastic_guess.append("1")
        print "PC1 was bigger!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    #break

rightCnt = 0
wrongCnt = 0
for x in range(0, len(sarcastic_answer)):
    if(sarcastic_answer[x] == sarcastic_guess[x]):
        rightCnt = rightCnt + 1
        print "you guessed right"
    else:
        wrongCnt = wrongCnt + 1
        print "wrong"

print "right Cnt " + str(rightCnt)
print "wrong Cnt " + str(wrongCnt)
print "test"
