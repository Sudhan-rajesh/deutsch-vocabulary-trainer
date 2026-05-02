import random
import csv

words = []

def pressed2():
    
    with open("vocabulary/vocabulary.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            words.append({"english":row["english"],"german":row["german"]})

    while True:
        question = random.choice(words)   
        english = question["english"]
        german = question["german"]
        print("Press 1 to exit")
        guess = input(f"{english} is german is: ").strip()
        if guess == german:
            print ("das ist richtig")
            continue
        elif guess == "1":
            break
        else:
            print(f"Try again, the right answer is {german}")
            continue
        
            
