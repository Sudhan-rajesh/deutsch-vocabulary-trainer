from .add_word import pressed1

def show_menu():
    while True:
        print("Vocabulary Trainer")
        print("Press 1 to add new word")
        print("Press 2 to practice vocabulary")
        print("Press 3 to show your vocabulary list")
        print("Press 4 to exit")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            pressed1()
        elif choice == 2:
            ...
        elif choice == 3:
            ...
        elif choice == 4:
            print("Auf Wiedersehen")
            break
        else:
            print("Invalid choice, Please try again")
            
        