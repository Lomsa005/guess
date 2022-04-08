import random

print("Good Luck ! ")
guesses_left=10
def get_guess():
    while True:
        guess=input("Guess: ")
        if len(guess)!=1:
            print("Your guess must have exactly one character!")
        elif guess.islower()==False:
            print("Your guess must be a lowercase letter!")
        else:
            return guess
def update_dashes(word,dashes,guess):
    for i in range(len(word)):
        if word[i]==guess:
            dashes=dashes[:i]+guess+dashes[i+1:]
    return dashes
words=["hello","python","facebook","school","book","except"]
secret_word = random.choice(words)
dashes=len(secret_word)*"-"
while guesses_left>0 and secret_word!=dashes:
    print(dashes)
    guess=get_guess()
    dashes=update_dashes(secret_word,dashes,guess)
    if guess in secret_word:
        print("That letter is in the word!")
        print(str(guesses_left)+" incorrect guesses left.")
    else:
        print("That letter is not in the word.")
        guesses_left-=1
        print(str(guesses_left)+" incorrect guesses left.")
        
        
if guesses_left==0:
    print("You lose. The word was: "+ secret_word )
else:      
    print("Congrats! You win. The word was: "+ secret_word)