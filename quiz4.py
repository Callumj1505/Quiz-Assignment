import random

from colorama import Fore, Style

def questions():
    global score
    score = 0
    questions_and_answers = [
        ("How many dots appear on a pair of dice?\nA: 45\nB: 42\nC: 39", "b"),
        ("What is the tallest type?\nA: Oakwoods\nB: Sprucewood\nC: Redwoods","c"),
        ("What is acrophobia a fear of?\nA: Speeds\nB: Heights\nC: Spiders", "heights"),
        ("Which year did the Titanic sink in the Atlantic Ocean?\nA: 1912\nB: 1909\nC: 1920", "a"),
        ("Which was Disney's first movie?\nA: Cinderella\nB: Tangled\nC: Snow White", "c"),
        ("Which alien creature in film has acid for blood?\nA: E.T\nB: Xenomorph\nC: Predator","b"),
        ("What is the chemical element with the symbol Fe?\nA: Zinc\nB: Copper\nC: Iron","c"),
        ("What is the national sport of Japan?\nA: Karate\nB: Sumo Wrestling\nC: Samurai","a"),
        ("What animal had the most powerful bite in the world?\nA: Nile Crocodile\nB: Freshwater Crocodile\nC: Salwater Crocodile","a"),
        ("Which State in America is the biggest?\nA: Alaska\nB: New York\nC: Texas","a")
        ]
    random.shuffle(questions_and_answers)
    for q, correct_answers in questions_and_answers:
        while True:
            print (q)
            answer = input("Choose A, B or C: ").lower()
            if answer not in ["a", "b", "c"]:
                print ("-- PLEASE ANSWER A, B OR C! --")
            else:
                break

        if answer == correct_answers:
            score += 5
            print (Fore.GREEN + f"-- CONGRATUALTIONS YOUR SCORE IS NOW {score}! --" + Style.RESET_ALL)
        else:
            score -= 2
            print(Fore.RED + f"-- INCORRECT YOUR SCORE IS NOW {score} --" + Style.RESET_ALL)
    
    while True:
        print(Fore.BLUE + f"Your final score is {score}" + Style.RESET_ALL)
        retry = input("Would you like to try again? Y/N\n").lower()
        if retry == "y":
            questions()
        elif retry == "n":
            print("Thank you for playing!")
            break
        else:
            print("Please pick an option.")

questions()