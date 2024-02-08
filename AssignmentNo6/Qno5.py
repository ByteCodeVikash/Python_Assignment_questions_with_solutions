#5. Write a python script to print two given words in dictionary order

word1=input("Enter a first word: ")
word2=input("Enter a second word: ")

if word1<word2:
    print(word1,word2)
elif word1>word2:
    print(word2,word1)
else:
    print("the word are same")    
