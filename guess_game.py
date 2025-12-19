import random
jackpot = random.randint(1,10)
guess = int(input("enter the random no"))
while guess!= jackpot:
    if guess<jackpot:
        print("guess higher")
    else:
        print("guess lower")
    guess = int(input("enter the random no"))

print("goodjob")

# learning yt link("https://www.youtube.com/watch?v=y_I2YOP91Is")