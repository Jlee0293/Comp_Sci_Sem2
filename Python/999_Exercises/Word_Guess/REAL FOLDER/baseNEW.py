
with open('wordle.txt') as f:
    for line in f:
        l = line.strip()
        list_words.append(1)

num = random.randrange(12972)
answer = list_word[num]
print (answer)
for i in range (0,6):
    guess = input("Give me a word! ")
    if guesss == answer:
        print("You guessed it! ")
        break
    else: 
        for words in list_words:
            if guess == words :
                a= 1
                if a == 1:
                     print("wrong word! ")
                     w = w + 1
                else: 
                    print("Invalid entry, guess again!")
                    a=0
        print ("You lost! The word was " + answer)
        
    print(c3)

f.close()
