import random

def game():
    print("You are playing the game..")
    score = random.randint(1, 100)
    # Fetch the high score from a file
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
        if hiscore!="":
            hiscore=int(hiscore)
        else:
            hiscore=0
    print(f"Your score: {score}")
    if(score>hiscore):
        # Write this high score to the file
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
    else:
        print(f"Your previous high score is: {hiscore}\nTry again to beat it!")
    return score
game()