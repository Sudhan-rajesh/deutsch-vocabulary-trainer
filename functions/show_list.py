import csv

def pressed3():
    words = []
    
    with open("vocabulary/vocabulary.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            words.append({"english":row[0],"german":row[1]})
    for word in sorted(words, key= lambda word:word["english"]):
        print(f"{word['english']} = {word['german']}")
