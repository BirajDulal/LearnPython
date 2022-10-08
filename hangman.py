import random
import hangman_words
import hangman_art
stages = hangman_art.stages
words = hangman_words.word_list
life = 6 
selectedWord = random.choice(words)
print (selectedWord)
spaces = len(selectedWord)
print(hangman_art.logo)

hman = []
for i in range(spaces):
    hman.append("_")
print(hman)
gameover = False
while gameover == False:
    guess = input("Please guess the letter: ").lower()
    i = 0
    if guess in hman:
        print(f"You have alredy selected {guess}, Please select any other letters")
    for letter in selectedWord:      
        if letter == guess:
            hman[i] = letter
            # else:
            #     life = life - 1
            #     print(f"One life is gone. Remaning life = {life}")
        i += 1
    
    if guess not in selectedWord:
        life = life -1
        print(f"The letter {guess} is not in the world. Hence, you loose a life")
        print(stages[life])
            
    print(hman)
    if "_" not in hman:
        gameover = True
        print("Game over you Won!")
    elif life == 0:
        gameover = True
        print("Game over")    