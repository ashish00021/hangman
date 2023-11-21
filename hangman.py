import random
import time
import word

# getting random word from wordlist 
secret_word = list(random.choice(word.words))
i = 0

# return a list display_word for guessing .
def randoms(secret_word):
    display_word=[]
    for letter in range(len(secret_word)):
        display_word += '_'
    return display_word




display_word = randoms(secret_word) # calling the function and get back a list for gussing 
num = len(secret_word)
        
print("[+] Welcome Hangman ....!")
time.sleep(2)

print("[+] you have 10 guess's for Guessing the word !")
time.sleep(3)

for x in range(0,10): # main for loop 
    
    if num == 0:
        break
    else:
        print(display_word)

        guess = input("Guess a letter: ").lower()

        for x in range(len(secret_word)):
           if guess == secret_word[x]:
               display_word[x] = secret_word[x]
               num -= 1 
               i += 1
               

score = 10 - i
if num != 0:
    print(secret_word)
    print("!! SORRY BETTER LUCK NEXT TIME !!")
else:
    print("!! YOU WIN THE GAME !!")
    print(f"AND YOUR SCORE IS {score}")
    
        