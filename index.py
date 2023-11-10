print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

# question no.1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
# question no.2
answer = input("What is OOPs? ")
if answer.lower() == "object oriented programming":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
# question no.3
answer = input("What is HTML? ")
if answer.lower() == "hyper text markup language":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
# question no.4
answer = input("What is CSS? ")
if answer.lower() == "cascading style sheets":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

# final result
print("You got " + str((score / 4) * 100) + "%.")