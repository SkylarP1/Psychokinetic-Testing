import random
import math
import os
import time
from datetime import datetime
import pandas as pd

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

ordering = []
chose = 0;
secureRand = random.SystemRandom()

control1 = []
for x in range(0,5000):
    control1.append(secureRand.randint(0,1000000))
control2 = []
for x in range(0,5000):
    control2.append(secureRand.randint(0,1000000))


def testing(x):
    global ordering
    order = secureRand.randint(1,5)
    chosen = str(x)
    if x == 0:
        nchosen = 1000000
    if x == 1000000:
        nchosen = 0
    if(order == 1):
        ordering = [chosen, nchosen, "The Quick Brown Fox", "Jumping Over the Candle"]
    if(order == 2):
        ordering = [chosen,"The Quick Brown Fox", nchosen,"Jumping Over the Candle"]
    if(order == 3):
        ordering = [chosen,"The Quick Brown Fox", "Jumping Over the Candle", nchosen]
    if(order == 4):
        ordering = ["The Quick Brown Fox", chosen, "Jumping Over the Candle", nchosen]
    if(order == 5):
        ordering = ["The Quick Brown Fox", "Jumping Over the Candle", chosen, nchosen]


id = input("Enter Test Subject's ID: ")

name = id + " " + datetime.utcnow().strftime('%Y-%m-%d-%H%M%S') + ".csv"
f = open(name, "x")
cls()


print("Welcome to Psychokinetic Testing. \nYou will be presented with 4 sections, each of which you will have to focus on the text on screen.\nThis text will either be the number chosen below, or a sentance.\nPlease, focus as hard as you can on this text.")
print("\nPlease choose a number(Type A or B and press Enter):\nA.0\nB.1,000,000")

#user input on choice of number
while True:
    #gathering input
    choice = input()
    #if choice is a, upper or lower case
    if choice == "A" or choice == "a":
        chose = 0
        #break loop because it's a valid choice
        break
    #if choice is b, upper or lower case
    elif choice == "B" or choice == "b":
        chose = 1000000
        #break loop because it's a valid choice
        break
    #if choice is neither A or B or a or b, it loops back to get a valid input
    else:
        print("Please select either A or B")
        continue
testing(chose)



for j in range(1,5):
    for i in range(1,5):
        cls()
        print("Test ", j," beginning in ", (5-i))
        time.sleep(1)

    start_time = time.time_ns() // 1_000_000
    results = []
    print(ordering[j-1])
    time.sleep(3)
    wheelState = 0
    wheel = ["\\","|","/","--"]
    for k in range(0,5000):
        results.append(secureRand.randint(0,1000000))
        elapsed = ((time.time_ns() // 1_000_000) - start_time) % 500
        if(elapsed >= 450):
            wheelState += 1
            wheelState %= len(wheel)
            temp = k // 500
            cls()
            print(ordering[j-1])
            print("[", "=" * temp, "-" * (10-temp), "]", wheel[wheelState])
        time.sleep(0.001)
    if(j == 1):
        trial1 = results
    if(j == 2):
        trial2 = results
    if(j == 3):
        trial3 = results
    if(j == 4):
        trial4 = results
    input("Please enter any key to continue:")
data = {
    ordering[0]: trial1,
    ordering[1]: trial2,
    ordering[2]: trial3,
    ordering[3]: trial4,
    "Control1": control1,
    "Control2": control2
}

df = pd.DataFrame(data)
df.to_csv(name, index = False)
