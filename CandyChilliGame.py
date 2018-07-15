print("Welcome to my game!")
print("  There are 40 objects in a jar. 39 candies and 1 chilli pepper.")
print("  Each player can take between 1 and 5 candies per round.")
print("  The object is to not end up with the chilli.")
print("\n")

def game():
    name1 = input("Player 1 enter your name: ")
    name2 = input("Player 2 enter your name: ")
    move = "{} pick 1 to 5 candies: "
    move1 = move.format(name1)
    move2 = move.format(name2)
    candies = 39
    
    while candies > 0:
        print("\n")
        play = int(input(move1))
        candies -= play
        print("There are",candies,"candies left.")
        
        if candies == 0:
            break
        print("\n")
        play = int(input(move2))
        candies -= play
        print("There are",candies,"candies left.")
        
    print("Game over",name1,"wins!",name2,"gets the chilli.")

game()

"""
To use the algorithm to win, pick 3 candies on the first pick.
Then, take 6 minus what player 2 takes to win.
"""
