from tkinter import *
from PIL import ImageTk, Image  
import os
import json
from pathlib import Path


if not os.path.exists("annotations"):
    os.mkdir("annotations")

# done = os.listdir("annotations")
# done = [int(image[:-4]) for image in done]

with open("evjvqa_train.json", "r", encoding="utf-8") as file:
    data = json.load(file)


images_name_dict = data['images']
images_name_dict = sorted(images_name_dict, key=lambda x: x['id'])

new_list = []
for entry in images_name_dict:
    new_list.append(entry)


print(f"Remain {len(new_list)}")

images_name_dict = new_list


DEFAULT_IMAGE_NAME = images_name_dict[0]['filename']

IMAGE_ID = images_name_dict[0]['id']
# IMAGE_ID = idx

DEFAULT_IMAGE_PATH = "train-images/" + DEFAULT_IMAGE_NAME
INDEX = 0
MAX_LENGTH = len(images_name_dict)

window = Tk()
window.title("Image Captioning ")
window.geometry('1200x500')
image1 = ImageTk.PhotoImage(Image.open(DEFAULT_IMAGE_PATH).resize((450, 350)))

lbl = Label(window, image=image1)

lbl.grid(column=0, rowspan=10)

title = Label(window, text = IMAGE_ID)
title.config(font=('Helvetica bold',10))
title.grid(column=1, row=0, sticky = N)

input_label = Label(window, text = "Nhập vào đây bạn ơi: ")
input_label.grid(column=1, row=1, sticky = N)

NUM_CAPTIONS = 5
ENTRY_VAR = []
for i in range(1, NUM_CAPTIONS + 1):
    entry_text = StringVar()
    caption1_t = Label(window, text = f"{i}.")
    ENTRY_VAR.append(entry_text)
    caption1_t.grid(column=1, row= i + 1, sticky = N)
    caption1 = Entry(window, width=50, textvariable=entry_text)
    caption1.grid(column=2, row= i + 1, sticky = N)


def set_content(image_dict, ENTRY_VAR):
    IMAGE_ID = image_dict['id']
    with open(f"annotations/{IMAGE_ID}.txt", "r", encoding="utf-8") as file:
        contents = [line.strip() for line in file.readlines()]
    for i, var in enumerate(ENTRY_VAR): 
            var.set(contents[i])

set_content(images_name_dict[INDEX], ENTRY_VAR)

END = 3 * NUM_CAPTIONS + 1

print(IMAGE_ID)

def clicked_prev():
    global INDEX
    INDEX -= 1
    if INDEX < 0:
        INDEX += MAX_LENGTH
    image = ImageTk.PhotoImage(Image.open("train-images/" + images_name_dict[INDEX]['filename'])\
        .resize((450, 350)))
    global window
    window.img = image
    lbl.configure(image=window.img)
    title.config(text=images_name_dict[INDEX]['id'])
    IMAGE_ID = images_name_dict[INDEX]['id']
    print(IMAGE_ID)
    set_content(images_name_dict[INDEX], ENTRY_VAR)


def clicked_next():
    global INDEX
    INDEX += 1
    if INDEX >= MAX_LENGTH:
        INDEX -= MAX_LENGTH
    image = ImageTk.PhotoImage(Image.open("train-images/" + images_name_dict[INDEX]['filename'])\
        .resize((450, 350)))
    global window
    window.img = image
    lbl.configure(image=window.img)
    title.config(text=images_name_dict[INDEX]['id'])
    IMAGE_ID = images_name_dict[INDEX]['id']
    print(IMAGE_ID)
    set_content(images_name_dict[INDEX], ENTRY_VAR)
    
def clicked():
    global INDEX
    if INDEX >= MAX_LENGTH:
        INDEX -= MAX_LENGTH
    IMAGE_ID = images_name_dict[INDEX]['id']
    with open(f"annotations/{IMAGE_ID}.txt", "w+", encoding="utf-8") as file:
        for var in ENTRY_VAR:
            print(var.get(), file=file) 
            var.set("")
    print(f"Saved to {IMAGE_ID}.txt")




btn_prev = Button(window, text="Prev", command=clicked_prev)
btn_prev.grid(column=2, row=END + 1, sticky = W)

btn_next = Button(window, text="Next", command=clicked_next)
btn_next.grid(column=2, row=END + 1, sticky=E)

btn_save = Button(window, text="Save", command=clicked)
btn_save.grid(column=2, row=END + 1)

window.mainloop()