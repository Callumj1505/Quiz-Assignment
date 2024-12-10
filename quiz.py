score = 0

import time

second = 1

print ("Question 1: How many dots appear on a pair of dice?")
print ("A: 45\nB: 42\nC: 39")

while True:
    answer1 = input("Choose A, B or C: ").lower()
    if answer1 == "b":
        score += 5
        print(f"-- CONGRATUALTIONS YOU GOT IT RIGHT! YOUR SCORE IS {score} --")
        break
    elif answer1 == "a" or "c":
        score -= 2
        print (f"-- THIS IS INCORRECT, YOUR CODE IS {score}, PLEASE TRY AGAIN --") 
        break

time.sleep(second)

print ("Question 2: What is the tallest type?")
print ("A: Oakwoods\nB: Sprucewood\nC: Redwoods")
while True:
    answer1 = input("Choose A, B or C: ").lower()
    if answer1 == "c":
        score += 5
        print(f"-- CONGRATUALTIONS YOU GOT IT RIGHT! YOUR SCORE IS {score} --")
        break
    elif answer1 == "a" or "b":
        score -= 2
        print (f"-- THIS IS INCORRECT, YOUR CODE IS {score}, PLEASE TRY AGAIN --") 
        break

time.sleep(second)

print ("Question 3: What is acrophobia a fear of?")
print ("A: Speeds\nB: Heights\nC: Spiders")
while True:
    answer1 = input("Choose A, B or C: ").lower()
    if answer1 == "b":
        score += 5
        print(f"-- CONGRATUALTIONS YOU GOT IT RIGHT! YOUR SCORE IS {score} --")
        break
    elif answer1 == "a" or "c":
        score -= 2
        print (f"-- THIS IS INCORRECT, YOUR CODE IS {score}, PLEASE TRY AGAIN --") 
        break

time.sleep(second)


print ("Question 4: Which year did the Titanic sink in the Atlantic Ocean?")
print ("A: 1912\nB: 1909\nC: 1920")
while True:
    answer1 = input("Choose A, B or C: ").lower()
    if answer1 == "a":
        score += 5
        print(f"-- CONGRATUALTIONS YOU GOT IT RIGHT! YOUR SCORE IS {score} --")
        break
    elif answer1 == "b" or "c":
        score -= 2
        print (f"-- THIS IS INCORRECT, YOUR CODE IS {score}, PLEASE TRY AGAIN --") 
        break

time.sleep(second)

print ("Question 5: Which was Disney's first movie?")
print ("A: Cinderella\nB: Tangled\nC: Snow White")

while True:
    answer1 = input("Choose A, B or C: ").lower()
    if answer1 == "c":
        score += 5
        print(f"-- CONGRATUALTIONS YOU GOT IT RIGHT! YOUR SCORE IS {score} --")
        break
    elif answer1 == "a" or "b":
        score -= 2
        print (f"-- THIS IS INCORRECT, YOUR CODE IS {score}, PLEASE TRY AGAIN --") 
        break

time.sleep(second)

print ("Question 6: Which alien creature in film has acid for blood?")
print ("A: E.T\nB: Xenomorph\nC: Preditor")

while True:
    answer1 = input("Choose A, B or C: ").lower()
    if answer1 == "b":
        score += 5
        print(f"-- CONGRATUALTIONS YOU GOT IT RIGHT! YOUR SCORE IS {score} --")
        break
    elif answer1 == "a" or "c":
        score -= 2
        print (f"-- THIS IS INCORRECT, YOUR CODE IS {score}, PLEASE TRY AGAIN --") 
        break

time.sleep(second)

print ("Question 7: What is the chemical element with the symbol Fe?")
print ("A: Zinc\nB: Copper\nC: Iron")

while True:
    answer1 = input("Choose A, B or C: ").lower()
    if answer1 == "c":
        score += 5
        print(f"-- CONGRATUALTIONS YOU GOT IT RIGHT! YOUR SCORE IS {score} --")
        break
    elif answer1 == "a" or "b":
        score -= 2
        print (f"-- THIS IS INCORRECT, YOUR CODE IS {score}, PLEASE TRY AGAIN --") 
        break

time.sleep(second)

print ("Question 8: What is the national sport of Japan?")
print ("A: Karate\nB: Sumo Wrestling\nC: Samurai")

while True:
    answer1 = input("Choose A, B or C: ").lower()
    if answer1 == "b":
        score += 5
        print(f"-- CONGRATUALTIONS YOU GOT IT RIGHT! YOUR SCORE IS {score} --")
        break
    elif answer1 == "a" or "c":
        score -= 2
        print (f"-- THIS IS INCORRECT, YOUR CODE IS {score}, PLEASE TRY AGAIN --") 
        break

time.sleep(second)

print ("Question 9: What animal had the most powerful bite in the world?")
print ("A: Nile Crocodile\nB: Freshwater Crocodile\nC: Salwater Crocodile")
while True:
    answer1 = input("Choose A, B or C: ").lower()
    if answer1 == "a":
        score += 5
        print(f"-- CONGRATUALTIONS YOU GOT IT RIGHT! YOUR SCORE IS {score} --")
        break
    elif answer1 == "b" or "c":
        score -= 2
        print (f"-- THIS IS INCORRECT, YOUR CODE IS {score}, PLEASE TRY AGAIN --") 
        break

time.sleep(second)

print ("Question 10: Which State in America is the biggest?")
print ("A: Alaska\nB: New York\nC: Texas")

while True:
    answer1 = input("Choose A, B or C: ").lower()
    if answer1 == "a":
        score += 5
        print(f"-- CONGRATUALTIONS YOU GOT IT RIGHT! YOUR SCORE IS {score} --")
        break
    elif answer1 == "a" or "c":
        score -= 2
        print (f"-- THIS IS INCORRECT, YOUR CODE IS {score}, PLEASE TRY AGAIN --") 
        break

second2 = 2
time.sleep(second)

print ("-- THANK YOU FOR ANSWERING MY QUESTIONS! --")
print (f"-- YOUR FINAL SCORE IS {score}")


