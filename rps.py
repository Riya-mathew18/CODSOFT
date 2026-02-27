import tkinter as tk
import random
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x500")
choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0
target_score = 3  
def play(user_choice):
    global player_score, computer_score
    computer_choice = random.choice(choices)
    computer_label.config(text=f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        player_score += 1
        result_label.config(text="You win this round!")
    else:
        computer_score += 1
        result_label.config(text="Computer wins this round!")
    score_label.config(text=f"Score → You: {player_score} | Computer: {computer_score}")
    if player_score == target_score:
        result_label.config(text="You won the game!")
        disable_buttons()
    elif computer_score == target_score:
        result_label.config(text=" Computer won the game!")
        disable_buttons()
def disable_buttons():
    rock_button.config(state="disabled")
    paper_button.config(state="disabled")
    scissors_button.config(state="disabled")
def restart_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    score_label.config(text="Score → You: 0 | Computer: 0")
    result_label.config(text="")
    computer_label.config(text="")
    rock_button.config(state="normal")
    paper_button.config(state="normal")
    scissors_button.config(state="normal")
title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16))
title.pack(pady=20)
rock_button = tk.Button(root, text="Rock", width=15, command=lambda: play("rock"))
rock_button.pack(pady=5)
paper_button = tk.Button(root, text="Paper", width=15, command=lambda: play("paper"))
paper_button.pack(pady=5)
scissors_button = tk.Button(root, text="Scissors", width=15, command=lambda: play("scissors"))
scissors_button.pack(pady=5)
computer_label = tk.Label(root, text="")
computer_label.pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)
score_label = tk.Label(root, text="Score → You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)
restart_button = tk.Button(root, text="Restart Game", command=restart_game)
restart_button.pack(pady=20)
root.mainloop()