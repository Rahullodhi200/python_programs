#python program 4(Rock Paper Scissor)
import time

print("Welcome to the game RoSyPy\n")
time.sleep(1)

t1 = time.time()

player1_choice = input("Player 1, please choose rock, paper, or scissors: ")
time.sleep(.5)
player2_choice = input("Player 2, please choose rock, paper, or scissors: ")

time.sleep(1)

print("\nCalculating results...\n")
time.sleep(2)

if (player1_choice == "rock" and player2_choice == "scissors") or (player1_choice == "paper" and player2_choice == "rock") or (player1_choice == "scissors" and player2_choice == "paper"):
  print("Player 1 wins!")
elif (player1_choice == player2_choice):
  print("It's a tie!")
else:
  print("Player 2 wins!")

t2 = time.time()
print("Time taken to complete game: ", t2 - t1, " seconds")