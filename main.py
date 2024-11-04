"""
Bind events cheatsheet: https://instructobit.com/tutorial/51/Python-Tkinter-event-handling
"""

import customtkinter as ctk

RES = (int(1920 * 0.4), int(1080 * 0.4))
FIELD_PERCENT_X = 0.4  # From 0 to 1
FIELD_PERCENT_Y = 0.2  # From 0 to 1

field_size_x = int(FIELD_PERCENT_X * RES[0])
field_size_y = int(field_size_x / 5)

# Configure Window
root = ctk.CTk()
root.geometry(f"{RES[0]}x{RES[1]}")
print(f"Opening window with resolution {RES[0]}x{RES[1]}")


def count(event):
    # print(textbox.get("1.0", "end"))
    counter.configure(text=str(len(textbox.get("1.0", "end-1c"))))


frame = ctk.CTkFrame(master=root)
frame.pack(pady=30, padx=30, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Character Counter", font=("Roboto", 24))
label.pack(pady=30, padx=10)

textbox = ctk.CTkTextbox(master=frame, width=field_size_x, height=field_size_y)
textbox.bind("<KeyPress>", count)
textbox.bind("<KeyRelease>", count)
textbox.pack(pady=30, padx=10)

counter = ctk.CTkLabel(master=frame, text="0", font=("Roboto", 24))
counter.pack(pady=30, padx=10)

root.mainloop()
