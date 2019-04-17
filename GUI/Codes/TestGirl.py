from tkinter import *
from PIL import Image, ImageTk
from itertools import count, cycle

class ImageLabel(Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)

root = Tk()
photo1 = PhotoImage(file="/home/pi/std_googleAssistant/GUI/Icons/GirlMusic.gif")
lbl = ImageLabel(root)
lbl.pack()
lbl.load(photo1)
root.title("Intelligent Fellow")
root.geometry("1000x920")
root.configure(background='white')
root.mainloop()