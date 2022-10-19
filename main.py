import random
print("Welcome To Hangman Game")
world_list = ["pramod", "thapa", "lalitpur", "kathmandu"]
choose = random.choice(world_list)
lenth_of_choose = len(choose)
display = []
lives = 6
for l in range(lenth_of_choose):
    display += "_"
end_game = False
while not end_game:
    guess = input("Guess a word\n").lower()
    for position in range(lenth_of_choose):
        letter = choose[position]
        if letter == guess:
            display[position] += letter
    if guess not in choose:
        lives -= 1
        print(f"You Lose A Life, You Have {lives} Lives Left")
        if lives ==0:
            end_game = True
            print("!!! Sorry You Are Hanged, GAME OVER !!!")
    print(display)
    if "_" not in display:
        end_game = True
        print(f"You guess the word right, The word was '{choose}' You Win")


