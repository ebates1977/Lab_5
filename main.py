import random

range = int(input("enter the range you would like to play in (starts at 1): "))

def play_again():
  answer = input("do you want to play again? ")
  if answer == "y" or answer == "Y" or answer == "Yes":
    r = int(input("enter the range you would like to play in (starts at 1): "))
    random_number(r)
  else:
    print("okay have a good day!")
    exit()
    
def random_number(range):
  random_number = random.randint(1, range)
  guess = int(input("Enter an integer from 1 to " + str(range) + ": "))
  while random_number != "guess":
      print
      if guess < random_number:
          print( "guess is low")
          guess = int(input("Enter an integer from 1 to " + str(range) + ": "))
      elif guess > random_number:
          print ("guess is high")
          guess = int(input("Enter an integer from 1 to " + str(range) + ": "))
      else:
          print ("you guessed it!")
          play_again()
          
      print

random_number(range)