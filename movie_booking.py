from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Movie Ticket Booking System")
root.geometry("900x600")
root.configure(bg="#0f172a")

# Heading
heading = Label(
    root,
    text="🎬 MOVIE TICKET BOOKING SYSTEM",
    font=("Arial", 24, "bold"),
    bg="#0f172a",
    fg="white"
)
heading.pack(pady=20)

# Movie Selection Frame
frame = Frame(root, bg="#1e293b", padx=20, pady=20)
frame.pack(pady=20)

Label(
    frame,
    text="Select Movie",
    font=("Arial", 14, "bold"),
    bg="#1e293b",
    fg="white"
).grid(row=0, column=0, padx=10, pady=10)

movie_var = StringVar()
movie_var.set("Pushpa 2")

movies = [
    "Pushpa 2",
    "KGF Chapter 2",
    "Leo",
    "Salaar",
    "RRR"
]

OptionMenu(frame, movie_var, *movies).grid(row=0, column=1)

Label(
    frame,
    text="Number of Tickets",
    font=("Arial", 14, "bold"),
    bg="#1e293b",
    fg="white"
).grid(row=1, column=0, padx=10, pady=10)

ticket_var = IntVar()
ticket_var.set(1)

Spinbox(frame, from_=1, to=10, textvariable=ticket_var, width=10).grid(row=1, column=1)

Label(
    frame,
    text="Customer Name",
    font=("Arial", 14, "bold"),
    bg="#1e293b",
    fg="white"
).grid(row=2, column=0, padx=10, pady=10)

name_entry = Entry(frame, width=25, font=("Arial", 12))
name_entry.grid(row=2, column=1)

price_label = Label(
    root,
    text="Ticket Price: ₹200",
    font=("Arial", 16, "bold"),
    bg="#0f172a",
    fg="yellow"
)
price_label.pack(pady=10)

def book_ticket():
    name = name_entry.get()
    movie = movie_var.get()
    tickets = ticket_var.get()

    if name == "":
        messagebox.showerror("Error", "Enter Customer Name")
        return

    total = tickets * 200

    messagebox.showinfo(
        "Booking Successful",
        f"Customer: {name}\n"
        f"Movie: {movie}\n"
        f"Tickets: {tickets}\n"
        f"Total Amount: ₹{total}"
    )

book_btn = Button(
    root,
    text="BOOK NOW",
    font=("Arial", 16, "bold"),
    bg="#ef4444",
    fg="white",
    padx=20,
    pady=10,
    command=book_ticket
)
book_btn.pack(pady=20)

footer = Label(
    root,
    text="DBMS Project - Movie Ticket Booking System",
    font=("Arial", 12),
    bg="#0f172a",
    fg="lightgray"
)
footer.pack(side=BOTTOM, pady=10)

root.mainloop()