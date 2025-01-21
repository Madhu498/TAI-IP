from geopy.geocoders import Nominatim
import tkinter as tk
from tkinter import messagebox

# Function to get location coordinates
def find_location():
    user_input = location_entry.get()
    if not user_input.strip():
        messagebox.showerror("Error", "Location cannot be empty!")
        return
    
    geolocator = Nominatim(user_agent="location_finder_app")
    try:
        location = geolocator.geocode(user_input)
        if location:
            result_label.config(
                text=f"Location: {location.address}\nLatitude: {location.latitude}\nLongitude: {location.longitude}"
            )
        else:
            result_label.config(text="Location not found. Please try again.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Location Finder")

# GUI layout
tk.Label(root, text="Enter a location:", font=("Arial", 14)).pack(pady=10)
location_entry = tk.Entry(root, width=50, font=("Arial", 14))
location_entry.pack(pady=10)

tk.Button(root, text="Find Location", command=find_location, font=("Arial", 14), bg="blue", fg="white").pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=500, justify="left")
result_label.pack(pady=20)

# Run the GUI event loop
root.mainloop()
