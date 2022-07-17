import random
from movies import movie_list

def get_word():
    movie = random.choice(movie_list)
    return movie.upper()


def play(movie):
    movie_completion="_"*len(movie)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(movie_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            
                if guess in guessed_letters:
                    {
                        print("You already guessed the letter ",guess)
                    }
                elif guess not in movie:
                    
                        print(guess,"is not in the word ")
                        
                        tries -=1
                        guessed_letters.append(guess)
                else:
                    
                        print("Good job, ",guess," is in the word!")
                        guessed_letters.append(guess)
                        movie_as_list = list(movie_completion)
                        indices = [i for i, letter in enumerate(movie) if letter == guess]
                        for index in indices:
                            movie_as_list[index] = guess
                        movie_completion="".join(movie_as_list)
                        if "_" not in movie_completion:
                            guessed = True
                    
        elif len(guess) == len(movie) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word ",guess)
            elif guess != movie:
                print(guess, " is not the word.")
                tries -=1
                guessed_words.append(guess)
            else:
                guessed = True
                movie_completion = movie
            
        else:

            print("Not a valid guess.")
        print(display_hangman(tries))
        print(movie_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the Movie! You win!")
    else:
        print("Sorry, you ran out of tries. The word was" + movie + ". Maybe next time!")
        






def display_hangman(tries):
    stages = ["""  
                     _______________
                     |             |
                     |             0
                     |           \ | /
                     |             |
                     |            / \ 
                     |           /   \ 
                     |
                     |                      
                     __                      
                                           
                     """
                     ,
                     """
                     _______________
                     |             |
                     |             0
                     |           \ | /
                     |             |
                     |            / 
                     |           /   
                     |
                     |                      
                     __                      
                          
                     """
                     ,
                     """
                     _______________
                     |             |
                     |             0
                     |           \ | /
                     |             |
                     |            
                     |           
                     |
                     |                      
                     __                      
                          
                     """
                     ,
                     """
                     _______________
                     |             |
                     |             0
                     |           \ | 
                     |             |
                     |            
                     |           
                     |
                     |                      
                     __
                     """
                     ,
                     """
                     _______________
                     |             |
                     |             0
                     |             | 
                     |             |
                     |            
                     |           
                     |
                     |                      
                     __
                     """
                     ,
                      """
                     _______________
                     |             |
                     |             0
                     |              
                     |             
                     |            
                     |           
                     |
                     |                      
                     __
                     """
                     ,
                      """
                     _______________
                     |             |
                     |             
                     |             
                     |             
                     |            
                     |           
                     |
                     |                      
                     __
                     """
            ]
    return stages[tries]

def main():
    movie=get_word()
    play(movie)
    while input("Play Again? (Y/N)").upper()=="Y":
        movie = get_word()
        play(movie)

if __name__=="__main__":
    main()


