#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
name_user = input("Enter your name")
print("Good luck",name_user,"in your word guessing game")
words = ['science','speaking','round', 'warm', 'soft', 'small', 'size','animal','reminds','human','babies','cats','cute','pie']
selected_word = random.choice(words)
#finds the word that has maximum length for to give a chance to the user
max_length=max(words,key=len)
#splits the word into the chars and counts how many chars in this list, in this list "speaking"!
guess_chance = len([*max_length])

turns = 2*guess_chance #Giving them this times of chances
print("Guess the characters")
guesses = ''

while turns>0:
    #taking the input from user
    guess = input("Enter a character: ")
    #storing it in the guesses
    guesses += guess
    failed = 0
    for char in selected_word:
        #comparing guess with the chars in guesses
        if char in guesses:
            print(char,end=" ") #ending with only space not \n
        else:
            #looking every char one by one, and if its not equal; writes "_"
            print("_")
            failed += 1
    if failed == 0:
        print("You Win! The word was",selected_word)
        break
    
    if guess not in selected_word:
        #decrement the turns
        turns-=1
        print("WRONG!")
        print("You have",turns,"turns left.")
        
    if turns == 0:
        print("You lost!")
        

        
            
            
            


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




