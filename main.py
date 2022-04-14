import random

range = int(input("enter the range you would like to play in (starts at 1): "))
ran = random.randint(1, range)


def random_number(range, ran):
  guess = int(input("Enter an integer from 1 to " + str(range) + ": "))
  
  if guess > ran:
    print( "guess is high")
    random_number(range, ran)
    
  elif guess < ran:
    print ("guess is low")
    random_number(range, ran)
    
  else:
    print ("you guessed it!")
    play_again()

def play_again():
  answer = input("do you want to play again? ")
  if answer == "y" or answer == "Y" or answer == "Yes" or answer == "yes":
    r = int(input("enter the range you would like to play in (starts at 1): "))
    rand = random.randint(1, range)
    random_number(r, rand)
  else:
    print("okay have a good day!")
    exit()
    
random_number(range, ran)