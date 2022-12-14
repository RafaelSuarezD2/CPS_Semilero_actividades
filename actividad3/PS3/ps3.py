# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Rafael Santiago Suárez Gil
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*':0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    word=word.lower()
    score=0
    puntosletras=0
    parte2=0
    wordlen=len(word)
    diferencia=n-wordlen
    for i in word:
        puntosletras=puntosletras+SCRABBLE_LETTER_VALUES[i]
    parte2=7*wordlen-3*diferencia
    if parte2<1:
        parte2=1
    score=puntosletras*parte2
    return score   
  # TO DO... Remove this line when you implement this function

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    hand["*"]=1
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    word=word.lower()
    available=hand.copy()
    for E in word:
        for F in available.keys():
            if F==E:
                if available[F]!=0:
                    available[F]=available[F]-1
    return(available)
  # TO DO... Remove this line when you implement this function

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    word=word.lower()
    def match_with_gaps(my_word, other_word):
         largo_palabra_mia=len(my_word)
         largo_otra_palabra=len(other_word)
         coincide=False
         if largo_palabra_mia==largo_otra_palabra:
             for A in range(largo_palabra_mia):
                 if my_word[A]!='*':
                     if my_word[A]==other_word[A]:
                         coincide=True
                     else:
                        coincide=False
                        break
                 else:
                     if VOWELS.find(other_word[A])!=-1:
                         coincide=True
                     else:
                         coincide=False
                         break
    
         return(coincide)
     
    def verificar_lista_palabras(word, wordlist):
        Verif=False
        cantidad_palabras=len(wordlist)
        for A in range(cantidad_palabras):
            if match_with_gaps(word, wordlist[A]):
                Verif=True
                break
        return Verif
    
    def verificar_mano(word, hand):
        Veriftot=True
        palabradiccion=get_frequency_dict(word)
        for A in palabradiccion.keys():
            Verifciclo=False
            for B in hand.keys():
                if A==B:
                    if hand[B]>=palabradiccion[A]:
                        Verifciclo=True
                        break
                    else:
                        Veriftot=False
                        break
                        break
            Veriftot=Veriftot and Verifciclo
            if not Veriftot:
                break
        return Veriftot        
    return verificar_lista_palabras(word, word_list) and verificar_mano(word, hand)       
            

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    suma=0
    for A in hand.keys():
        suma=suma+hand[A]
    return suma
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    

def play_hand(hand, word_list):
    terminar=False
    puntos=0
    while not terminar:
        print("Current hand: ")
        display_hand(hand)
        palabra=input("Enter word, or !! to indicate that you are finished: ")
        if palabra == "!!":
            terminar=True
        else:
            if is_valid_word(palabra, hand, word_list):
                puntos=puntos+get_word_score(palabra, calculate_handlen(hand))
                print(palabra,"earned:",get_word_score(palabra, calculate_handlen(hand)),"points. Total:",puntos,"points \n")
                hand=update_hand(hand, palabra)
            else:
                print("Please enter a valid word\n")
        if calculate_handlen(hand)==0:
            print("Ran out of letters.")
            terminar=True
    print("Total score:",puntos,"Points.\n")
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is two exclamation points:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not two exclamation points):

            # If the word is valid:

                # Tell the user how many points the word earned,
                # and the updated total score

            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
                
            # update the user's hand by removing the letters of their inputted word
            

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function



#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    letter=letter.lower()
    nueva_mano=hand.copy()
    if letter in hand:
        conjunto="".join(map(str,string.ascii_lowercase-nueva_mano.keys()))
        nueva_letra=random.choice(conjunto)
        nueva_mano[nueva_letra]=nueva_mano[letter]
        del(nueva_mano[letter])
    return nueva_mano    
        
        
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    

    
def play_game(word_list):
    numero_manos=input("Enter total number of hands: ")
    numero_manos=int(numero_manos)
    while numero_manos>0: 
        hand=deal_hand(HAND_SIZE)
        arrancar=False
        cambiar_mano=False
        while not arrancar:
          print("Current hand:")
          display_hand(hand)
          confirm_cambio_letra=input("Would you like to substitute a letter?: ")
          if confirm_cambio_letra!='no':
              if confirm_cambio_letra!='yes':
                  print("I don't understand, try again")
              else:
                  letra_para_cambiar=input("Which letter would you like to replace: ")
                  hand=substitute_hand(hand, letra_para_cambiar)
                  arrancar=True
          else:
              arrancar=True
        while not cambiar_mano:
          play_hand(hand, word_list)
          print("_______________")
          confirm_misma_mano=input("Would you like to replay the hand? ")
          if confirm_misma_mano=="yes":
              cambiar_mano=False
          elif confirm_misma_mano=="no":
              cambiar_mano=True
          else:
              print("I didn't understand your answer, I think it's no")
              cambiar_mano=True
        numero_manos=numero_manos-1      
        
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
   


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)