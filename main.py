# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter.constants import ANCHOR
import keyboard
import tkinter as tk
import random
from PIL import Image,ImageTk

def hide_all():
    canvas.itemconfig(bg_cat_id, state='normal')
    for x in canvas_obj_list:
        canvas.itemconfig(x, state='hidden')

def on_press(e):
    hide_all()
    pick = random.randint(0, len(canvas_obj_list) - 1)
    canvas.itemconfig(canvas_obj_list[pick], state='normal')
    canvas.itemconfig(bg_cat_id, state='hidden')

def test():
    hide_all()
    window.after(100, test)

width = 300
height = 300
window = tk.Tk()
window.overrideredirect(1)
window.title(string='Bongo Cat v1')
window.geometry(f"{width}x{height}")
canvas = tk.Canvas(window, width=width, height=height, bg="white", border="0")
canvas.pack()

kb = Image.open('res/keyboard.png')
kb_w, kb_h = kb.size
kb = kb.resize((int(kb_w * 0.4), int(kb_h * 0.4)), Image.ANTIALIAS)
kb = ImageTk.PhotoImage(kb)
canvas.create_image(60, 151, anchor='nw', image=kb)

img_path_list = [f'res/key-{x}.png'for x in [1,2,3,4,5,6]]
img_obj_list = [Image.open(x).resize((width, height), Image.ANTIALIAS) for x in img_path_list]
img_obj_list = [ImageTk.PhotoImage(x) for x in img_obj_list]
canvas_obj_list = [canvas.create_image(0, 0, anchor='nw', image=x) for x in img_obj_list]
bg_cat = Image.open('res/arms-up.png').resize((width, height), Image.ANTIALIAS)
bg_cat = ImageTk.PhotoImage(bg_cat)
bg_cat_id = canvas.create_image(0, 0, anchor='nw', image=bg_cat)

hide_all()

keyboard.on_press(on_press)

window.after(100, test)
window.mainloop()
