import tkinter as tk
from tkinter import messagebox

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Countdown Timer")
        self.time_remaining = 0  # Stores total time in seconds

        # Input Frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter Time:").grid(row=0, column=0, padx=5)
        self.entry_days = tk.Entry(input_frame, width=5)
        self.entry_days.grid(row=0, column=1, padx=5)
        tk.Label(input_frame, text="Days").grid(row=0, column=2, padx=5)

        self.entry_hours = tk.Entry(input_frame, width=5)
        self.entry_hours.grid(row=0, column=3, padx=5)
        tk.Label(input_frame, text="Hours").grid(row=0, column=4, padx=5)

        self.entry_minutes = tk.Entry(input_frame, width=5)
        self.entry_minutes.grid(row=0, column=5, padx=5)
        tk.Label(input_frame, text="Minutes").grid(row=0, column=6, padx=5)

        self.entry_seconds = tk.Entry(input_frame, width=5)
        self.entry_seconds.grid(row=0, column=7, padx=5)
        tk.Label(input_frame, text="Seconds").grid(row=0, column=8, padx=5)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        self.start_button = tk.Button(button_frame, text="Start Timer", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = tk.Button(button_frame, text="Reset Timer", command=self.reset_timer, state=tk.DISABLED)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        # Timer Display
        self.timer_label = tk.Label(self.root, text="00:00:00:00", font=("Helvetica", 24))
        self.timer_label.pack(pady=20)

        # Variables for state tracking
        self.running = False

    def start_timer(self):
        if not self.running:
            try:
                days = int(self.entry_days.get() or 0)
                hours = int(self.entry_hours.get() or 0)
                minutes = int(self.entry_minutes.get() or 0)
                seconds = int(self.entry_seconds.get() or 0)

                # Calculate total time in seconds
                self.time_remaining = days * 86400 + hours * 3600 + minutes * 60 + seconds

                if self.time_remaining <= 0:
                    raise ValueError("Time must be greater than zero.")

                # Disable entry fields and start button
                self.entry_days.config(state=tk.DISABLED)
                self.entry_hours.config(state=tk.DISABLED)
                self.entry_minutes.config(state=tk.DISABLED)
                self.entry_seconds.config(state=tk.DISABLED)
                self.start_button.config(state=tk.DISABLED)
                self.reset_button.config(state=tk.NORMAL)

                self.running = True
                self.update_timer()
            except ValueError as e:
                messagebox.showerror("Invalid Input", str(e))

    def update_timer(self):
        if self.time_remaining > 0:
            days, remainder = divmod(self.time_remaining, 86400)
            hours, remainder = divmod(remainder, 3600)
            minutes, seconds = divmod(remainder, 60)

            self.timer_label.config(text=f"{days:02d}:{hours:02d}:{minutes:02d}:{seconds:02d}")

            self.time_remaining -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="00:00:00:00")
            messagebox.showinfo("Timer Completed", "Time's up!")
            self.reset_timer()

    def reset_timer(self):
        self.running = False
        self.time_remaining = 0

        # Reset entry fields and buttons
        self.entry_days.config(state=tk.NORMAL)
        self.entry_hours.config(state=tk.NORMAL)
        self.entry_minutes.config(state=tk.NORMAL)
        self.entry_seconds.config(state=tk.NORMAL)
        self.start_button.config(state=tk.NORMAL)
        self.reset_button.config(state=tk.DISABLED)

        # Clear timer display
        self.timer_label.config(text="00:00:00:00")

# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()
