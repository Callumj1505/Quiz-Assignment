import time

def questions():
    global score
    score = 0
    questions_and_answers = [
        ("Question 1: How many dots appear on a pair of dice?\nA: 45\nB: 42\nC: 39", "b"),
        ("Question 2: What is the tallest type?\nA: Oakwoods\nB: Sprucewood\nC: Redwoods","c"),
        ("Question 3: What is acrophobia a fear of?\nA: Speeds\nB: Heights\nC: Spiders", "heights"),
        ("Question 4: Which year did the Titanic sink in the Atlantic Ocean?\nA: 1912\nB: 1909\nC: 1920", "a"),
        ("Question 5: Which was Disney's first movie?\nA: Cinderella\nB: Tangled\nC: Snow White", "c"),
        ("Question 6: Which alien creature in film has acid for blood?\nA: E.T\nB: Xenomorph\nC: Preditor","b"),
        ("Question 7: What is the chemical element with the symbol Fe?\nA: Zinc\nB: Copper\nC: Iron","c"),
        ("Question 8: What is the national sport of Japan?\nA: Karate\nB: Sumo Wrestling\nC: Samurai","a"),
        ("Question 9: What animal had the most powerful bite in the world?\nA: Nile Crocodile\nB: Freshwater Crocodile\nC: Salwater Crocodile","a"),
        ("Question 10: Which State in America is the biggest?\nA: Alaska\nB: New York\nC: Texas","a")
        ]
    for q, correct_answers in questions_and_answers:
        print (q)
        answer = input("Choose A, B or C: ").lower()
        if answer != "a" or "b" or "c":
            print ("-- PLEASE ANSWER A, B OR C! --")
            answer = input("Choose A, B or C: ").lower()
            if answer == correct_answers:
                score += 5
                print (f"-- CONGRATUALTIONS YOUR SCORE IS NOW {score}! --")
        else:
            score -= 2
            print (f"-- INCORRECT YOUR SCORE IS NOW {score}")

questions()
    
# print ("Question 1: How many dots appear on a pair of dice?")
# print ("A: 45\nB: 42\nC: 39")

# print ("Question 2: What is the tallest type?")
# print ("A: Oakwoods\nB: Sprucewood\nC: Redwoods")

# print ("Question 3: What is acrophobia a fear of?")
# print ("A: Speeds\nB: Heights\nC: Spiders")

# print ("Question 4: Which year did the Titanic sink in the Atlantic Ocean?")
# print ("A: 1912\nB: 1909\nC: 1920")

# print ("Question 5: Which was Disney's first movie?")
# print ("A: Cinderella\nB: Tangled\nC: Snow White")

# print ("Question 6: Which alien creature in film has acid for blood?")
# print ("A: E.T\nB: Xenomorph\nC: Preditor")

# print ("Question 7: What is the chemical element with the symbol Fe?")
# print ("A: Zinc\nB: Copper\nC: Iron")

# print ("Question 8: What is the national sport of Japan?")
# print ("A: Karate\nB: Sumo Wrestling\nC: Samurai")

# print ("Question 9: What animal had the most powerful bite in the world?")
# print ("A: Nile Crocodile\nB: Freshwater Crocodile\n C: Salwater Crocodile")

# print ("Question 10: Which State in America is the biggest?")
# print ("A: Alaska\nB: New York\nC: Texas")