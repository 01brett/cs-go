# import module we need
import random

# file i/o functions for historical results
def load_results():
    with open("history.txt", "r") as txt:
        return txt.read().split(",")


def save_results(w, t, l):
    with open("history.txt", "w") as txt:
        txt.write(f"{str(w)},{str(t)},{str(l)}")


# welcome message
results_history = load_results()
wins = int(results_history[0])
ties = int(results_history[1])
losses = int(results_history[2])
print("Welcome to Rock, Paper, Scissors!")
print(f"Wins: {wins}, Ties: {ties}, Losses: {losses}")
print("Please choose to continue...")


# initialize user, computer choices
computer = random.randint(1, 3)
user = int(input("[1] Rock  [2] Paper   [3] Scissors    [9] Quit\n"))

# gamplay loop
while not user == 9:
    # user chooses ROCK
    if user == 1:
        if computer == 1:
            print("Computer chose rock...tie!")
            ties += 1
        elif computer == 2:
            print("Computer chose paper...computer wins :(")
            losses += 1
        else:
            print("Computer chose scissors...you wins :)")
            wins += 1

    # user chooses PAPER
    elif user == 2:
        if computer == 1:
            print("Computer chose rock...you win :)")
            wins += 1
        elif computer == 2:
            print("Computer chose paper...tie!")
            ties += 1
        else:
            print("Computer chose scissors...computer wins :(")
            losses += 1

    # user chooses SCISSORS
    elif user == 3:
        if computer == 1:
            print("Computer chose rock...computer wins :(")
            losses += 1
        elif computer == 2:
            print("Computer chose paper...you win :)")
            wins += 1
        else:
            print("Computer chose scissors...tie!")
            ties += 1
    else:
        print("Invalid selection. Please try again.")
    # print updated stats
    print(f"Wins: {wins}, Ties: {ties}, Losses: {losses}")

    # prompt user to make another selection
    print("Please choose to continue...")
    # initialize user, computer choices
    computer = random.randint(1, 3)
    user = int(input("[1] Rock  [2] Paper   [3] Scissors    [9] Quit\n"))

# #game over, save results
save_results(wins, ties, losses)
