import tkinter as tk

# Button Command
def to_km():
    try:
        miles = float(miles_entry.get())
        km = round(miles * 1.60934)
    except ValueError:
        print("insert a number!")
        return
    km_entry.config(state="normal")
    km_entry.insert(0, km)
    km_entry.config(state="readonly")


# Window Setup
window = tk.Tk()
window.minsize(width=300, height=150)
window.title("Mile to Km")
window.config(padx=40, pady=50, background="white")

# Entry
miles_entry = tk.Entry()
miles_entry.grid(column=1, row=0)
miles_entry.config(width=12)

km_entry = tk.Entry()
km_entry.grid(column=1, row=1)
km_entry.config(width=12, state="readonly")

# Labels
tk.Label(text="Miles", background="white").grid(column=2, row=0)
tk.Label(text="is equal to", background="white").grid(column=0, row=1)
tk.Label(text="Km", background="white").grid(column=2, row=1)

# Button
tk.Button(text="Calculate", command=to_km).grid(column=1, row=2)

window.mainloop()
