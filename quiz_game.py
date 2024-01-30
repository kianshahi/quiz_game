# ---------------------
def new_game():
  guesses = []
  correct_guesses = 0
  # counter
  question_num = 1
  # display all questios in our dictionary of questions
  for key in questions:
    print("-------------------------")
    print(key)
    # display all of the different options for each question
    for i in options[question_num-1]:
      print(i)
    guess = input("Enter (A, B, C, or D): ")
    guess = guess.upper()
    guesses.append(guess)

    correct_guesses += check_answer(questions.get(key), guess)
    question_num += 1

  # after iterating through questions display final score
  display_score(correct_guesses, guesses)
# ---------------------
def check_answer(answer, guess):
  # see if answer is equal to out guess
  if answer == guess:
    print("Correct!")
    return 1
  else:
    print("Wrong!")
    return 0
# ---------------------
def display_score(correct_guesses, guesses):
  print("-------------------------")
  print("Results")
  print("-------------------------")
  # Display answers
  print("Answers: ", end="")
  for i in questions:
    print(questions.get(i), end=" ")
  print()
  # Display guesses
  print("Guesses: ", end="")
  for i in guesses:
    print(i, end=" ")
  print()
  # calculate score
  score = int((correct_guesses/len(questions))*100)
  print("Your score is: "+str(score)+"%")
# ---------------------
def play_again():
  response = input("Do you want to play again? (yes or no)?: ")
  response = response.upper()
  if response == "YES":
    return True
  else:
    return False
# ---------------------

# a collection to hold the answers and questions
# questions and answers are in the same order
questions = {
  "Who created Python?: ": "A",
  "What year was Python created?: ": "B",
  "Python is tributed to which comedy group?: ": "C",
  "Is the Earth round?: ": "A"
}

# a collection to hold every possible answer
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

new_game()

while play_again():
  new_game()

print("Thanks for playing!")