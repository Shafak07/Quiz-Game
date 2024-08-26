print("Welcome to the Quiz: ")

play = input("Do you want to play? ")

if play.lower() != "yes":
    quit()

print("Okay! Let's play ;)")
score = 0

answer = input("What does CPU stand for?")
if answer.lower() == "central processing unit":
    print('Correct!')
    score +=1
else:
    print('Incorrect!')

answer = input("What is capital of India?")
if answer.lower() == "delhi":
    print('Correct!')
    score +=1
else:
    print('Incorrect!')

answer = input("Who is Prime Minister of India?")
if answer.lower() == "Narendra Modi":
    print('Correct!')
    score +=1
else:
    print('Incorrect!')

answer = input("What does Ram Stand for?")
if answer.lower() == "Random Access Memory":
    print('Correct!')
    score +=1
else:
    print('Incorrect!')

answer = input("What is Object in OOP?")
if answer.lower() == "instance of a class ":
    print('Correct!')
    score +=1
else:
    print('Incorrect!')

    print("You got " + str(score)+ "questions correct!")
    print("You got " +str((score/5)*100) + "%.")