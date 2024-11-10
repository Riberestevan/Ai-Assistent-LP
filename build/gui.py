
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
import  tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\mathi\Downloads\Tkinter-Designer-master\Ai-Assist\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = tk.Tk()
window.geometry(f"393x852+{1500}+{150}")
window.configure(bg = "#17224D")



canvas = Canvas(
    window,
    bg = "#17224D",
    height = 852,
    width = 393,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    393.0,
    852.0,
    fill="#17224D",
    outline="")

canvas.create_rectangle(
    0.0,
    326.0,
    393.0,
    852.0,
    fill="#0C2279",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    196.0,
    600.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    196.0,
    228.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    196.0,
    611.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    163.0,
    762.0,
    image=image_image_4
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    bg="#1837AF",
    activebackground="#1837AF"


)
button_1.place(
    x=101.0,
    y=794.0,
    width=190.0,
    height=30.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
    bg="#1837AF",
    activebackground="#1837AF"
)
button_2.place(
    x=324.0,
    y=740.0,
    width=62.0,
    height=45.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    169.0,
    762.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#E8F1F2",
    fg="#001EE0",
    highlightthickness=0
)
entry_1.place(
    x=21.0,
    y=745.0,
    width=296.0,
    height=32.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    196.5,
    606.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#1837AF",
    fg="#FFFFFF",
    highlightthickness=0
)
entry_2.place(
    x=28.0,
    y=451.0,
    width=337.0,
    height=275.0
)
window.resizable(False, False)
window.mainloop()
