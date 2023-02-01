lives = 5 # Attempts
word = "HELLO" # The word that needs to be guessed
guess_word = "*" * len(word) # The word is encrypted with stars

print("***** WORD GUESS *****") # Shows the name of the game

# The main algorithm
while not (lives == 0 or word == guess_word):
  print("")
  print("Word to guess:", guess_word)
  print("You have", lives, "lives left.")
  letter = ""
  while not (len(letter) == 1 and letter.isdigit() == False): 
    letter = input("Letter? ")
    letter = letter.upper()
  if letter in word:
    index_letter = [x[0] for x in enumerate(word) if x[1] == letter]
    for index in index_letter:
      guess_word = guess_word[:index] + letter + guess_word[index + 1:]
  else:
    lives -= 1

# Shows the result
print("")
if lives == 0:
  print("You lose!")
else:
  print("You win!")
  print("Word:", word)
