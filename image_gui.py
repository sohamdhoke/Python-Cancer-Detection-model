import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageInputGUI:
    def __init__(self, master):
        self.master = master
        master.title("Image Input")
       # master.geometry('800X600')

        # create a button to select the image file
        self.select_button = tk.Button(master, text="Select Image", command=self.select_image)
        self.select_button.pack()

        # create a label to display the selected image
        self.image_label = tk.Label(master)
        self.image_label.pack()

        # set the background color or image
        # uncomment one of the following lines to use a solid color or image background
        #self.master.config(bg="blue")  # set a solid color background
        self.set_background_image("C:\College stuff'\sem4\Mini Project\mr.jfif")  # set a background image

    def select_image(self):
        # open a file dialog to select an image file
        file_path = filedialog.askopenfilename()

        # load the image file
        image = Image.open(file_path)

        # convert the image to a format that tkinter can display
        photo = ImageTk.PhotoImage(image)

        # display the image in the label
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def set_background_image(self, image_path):
        # load the background image
        bg_image = Image.open(image_path)

        # convert the image to a format that tkinter can display
        bg_photo = ImageTk.PhotoImage(bg_image)

        # create a label for the background image
        bg_label = tk.Label(self.master, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # set the label as the background
        bg_label.image = bg_photo
        self.master.config(bg='')

if __name__ == '__main__':
    root = tk.Tk()
    app = ImageInputGUI(root)
    root.mainloop()
