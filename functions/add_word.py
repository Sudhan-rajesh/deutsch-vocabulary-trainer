import csv

def pressed1():

    english = input("Enter english word: ")
    german = input("Enter the german translation: ")
    with open("vocabulary/vocabulary.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["english","german"])
        writer.writerow({"english":english,"german":german})
        print("vocabulary list updated successfully!")
        print(f"Last added word is {english} which means {german}")
    
        
            