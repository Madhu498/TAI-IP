import tkinter as tk
from tkinter import messagebox
import re

def validate_credit_card(card_number):
    # Remove non-numeric characters
    card_number = re.sub(r'\D', '', card_number)
    
    # Validate the length
    if len(card_number) < 13 or len(card_number) > 19:  # Typical credit card lengths
        return False, "Card number must be between 13 and 19 digits."

    # Luhn Algorithm for validation and correction suggestion
    def luhn_algorithm_with_suggestion(card_num):
        total = 0
        reverse_digits = list(map(int, card_num[::-1]))
        correction_needed = False
        correction_digit = None
        invalid_position = None

        for i, digit in enumerate(reverse_digits):
            if i % 2 == 1:  # Double every second digit from the right
                n = digit * 2
                if n > 9:
                    n -= 9
            else:
                n = digit
            total += n

        if total % 10 != 0:
            correction_needed = True
            remainder = total % 10
            correction_digit = (10 - remainder) % 10
            invalid_position = len(card_num) - 1  # Suggest fixing the last digit for simplicity

        return total % 10 == 0, correction_needed, correction_digit, invalid_position

    is_valid, correction_needed, correction_digit, invalid_position = luhn_algorithm_with_suggestion(card_number)

    if not is_valid:
        if correction_needed and correction_digit is not None:
            suggestion_message = (
                f"Invalid Credit Card Number!\n"
                f"Suggestion: Replace the digit at position {invalid_position + 1} "
                f"with {correction_digit} to make it valid."
            )
        else:
            suggestion_message = "Invalid Credit Card Number!"
        return False, suggestion_message
    return True, "Valid Credit Card Number!"

def validate():
    card_number = entry.get()
    is_valid, message = validate_credit_card(card_number)
    if is_valid:
        messagebox.showinfo("Result", message)
    else:
        messagebox.showerror("Result", message)

# Initialize the GUI application
app = tk.Tk()
app.title("Enhanced Credit Card Validator")
app.geometry("450x300")
app.resizable(False, False)

# Add a label
label = tk.Label(app, text="Enter Credit Card Number:", font=("Arial", 14))
label.pack(pady=10)

# Add an entry field
entry = tk.Entry(app, font=("Arial", 14), width=30)
entry.pack(pady=10)

# Add a validate button
validate_button = tk.Button(app, text="Validate", font=("Arial", 14), command=validate)
validate_button.pack(pady=10)

# Add instructions for user
instructions = tk.Label(app, text="* Ensure only digits are entered.", font=("Arial", 10), fg="gray")
instructions.pack(pady=10)

# Run the GUI loop
app.mainloop()
