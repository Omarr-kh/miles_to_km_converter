import tkinter as tk

# Window Setup
window = tk.Tk()
window.minsize(width=400, height=150)
window.title("Mile to Km")

# Entry
miles = tk.Entry()
miles.grid(column=5, row=2)
miles.config(width=10)

km = tk.Entry()
km.grid(column=5, row=3)
km.config(width=10)

# Labels
tk.Label(text="Miles").grid(column=6, row=2)
tk.Label(text="is equal to").grid(column=4, row=3)
tk.Label(text="Km").grid(column=6, row=3)

window.mainloop()
