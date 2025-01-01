import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        
        # Set up the random number and attempts
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        
        # GUI Elements
        self.instructions_label = tk.Label(
            root, text="Guess a number between 1 and 100:", font=("Arial", 14)
        )
        self.instructions_label.pack(pady=10)
        
        self.guess_entry = tk.Entry(root, font=("Arial", 14))
        self.guess_entry.pack(pady=10)
        
        self.submit_button = tk.Button(
            root, text="Submit Guess", font=("Arial", 14), command=self.check_guess
        )
        self.submit_button.pack(pady=10)
        
        self.feedback_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
        self.feedback_label.pack(pady=10)
    
    def check_guess(self):
        try:
            # Get the user's guess
            user_guess = int(self.guess_entry.get())
            self.attempts += 1
            
            # Check the guess
            if user_guess < self.number_to_guess:
                self.feedback_label.config(text="Too low! Try again.")
            elif user_guess > self.number_to_guess:
                self.feedback_label.config(text="Too high! Try again.")
            else:
                messagebox.showinfo(
                    "Congratulations!",
                    f"You guessed the number in {self.attempts} attempts!",
                )
                self.reset_game()
        except ValueError:
            self.feedback_label.config(text="Invalid input. Please enter a number.")
    
    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.feedback_label.config(text="")
        self.guess_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
game = NumberGuessingGame(root)

# Run the GUI event loop
root.mainloop()
