a= int(input("Enter the score: "))
# input the obtained score in game

def game():
    return a  # this score is gonnna return

score = game()
with open("high_score.txt") as f:
    high_score = int(f.read())  # it will read the score
print("The current high score is: ", high_score)

# if the obt score is more than saved high score, it will become the next highscore
if high_score<score :
    with open("high_score.txt", "w") as f:
        f.write(str(score))   # the new high score will be updated in the folder

# the commment below for the high sore
if high_score<score:
    print("The new High score is: ", score)
else:
    print("The High score is still: ", high_score)



