import tkinter as tk

# Button Command
def to_km():
    miles = int(miles_entry.get())
    km = miles * 1.60934
    km_entry.config(state="normal")
    km_entry.insert(0, km)
    km_entry.config(state="readonly")


# Window Setup
window = tk.Tk()
window.minsize(width=400, height=150)
window.title("Mile to Km")

# Entry
miles_entry = tk.Entry()
miles_entry.grid(column=5, row=2)
miles_entry.config(width=10)

km_entry = tk.Entry()
km_entry.grid(column=5, row=3)
km_entry.config(width=10, state="readonly")

# Labels
tk.Label(text="Miles").grid(column=6, row=2)
tk.Label(text="is equal to").grid(column=4, row=3)
tk.Label(text="Km").grid(column=6, row=3)

# Button
tk.Button(text="Calculate", command=to_km).grid(column=5, row=4)

window.mainloop()
