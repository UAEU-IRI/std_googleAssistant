# source code: http://code.activestate.com/recipes/580708-tkinter-animated-gif/

# adjusted Design

from tkinter import *

from PIL import Image, ImageTk


class AnimatedGIF(Label, object):

    def __init__(self, master, path, forever=True):

        self._master = master

        self._loc = 0

        self._forever = forever

        self._is_running = False

        im = Image.open(path)

        self._frames = []

        i = 0

        try:

            while True:
                photoframe = ImageTk.PhotoImage(im.copy().convert('RGBA'))

                self._frames.append(photoframe)

                i += 1

                im.seek(i)

        except EOFError:

            pass

        self._last_index = len(self._frames) - 1

        try:

            self._delay = im.info['duration']

        except:

            self._delay = 100

        self._callback_id = None

        super(AnimatedGIF, self).__init__(master, image=self._frames[0])

    def start_animation(self, frame=None):

        if self._is_running: return

        if frame is not None:
            self._loc = 0

            self.configure(image=self._frames[frame])

        self._master.after(self._delay, self._animate_GIF)

        self._is_running = True

    def stop_animation(self):

        if not self._is_running: return

        if self._callback_id is not None:
            self.after_cancel(self._callback_id)

            self._callback_id = None

        self._is_running = False

    def _animate_GIF(self):

        self._loc += 1

        self.configure(image=self._frames[self._loc])

        if self._loc == self._last_index:

            if self._forever:

                self._loc = 0

                self._callback_id = self._master.after(self._delay, self._animate_GIF)

            else:

                self._callback_id = None

                self._is_running = False

        else:

            self._callback_id = self._master.after(self._delay, self._animate_GIF)

    def pack(self, start_animation=True, **kwargs):

        if start_animation:
            self.start_animation()

        super(AnimatedGIF, self).pack(**kwargs)

    def grid(self, start_animation=True, **kwargs):

        if start_animation:
            self.start_animation()

        super(AnimatedGIF, self).grid(**kwargs)

    def place(self, start_animation=True, **kwargs):

        if start_animation:
            self.start_animation()

        super(AnimatedGIF, self).place(**kwargs)

    def pack_forget(self, **kwargs):

        self.stop_animation()

        super(AnimatedGIF, self).pack_forget(**kwargs)

    def grid_forget(self, **kwargs):

        self.stop_animation()

        super(AnimatedGIF, self).grid_forget(**kwargs)

    def place_forget(self, **kwargs):

        self.stop_animation()

        super(AnimatedGIF, self).place_forget(**kwargs)


if __name__ == "__main__":
    root = Tk()

    l = AnimatedGIF(root, "C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/CHARACTERS/BabyG/BabyWin.gif")

    photoN = PhotoImage(file="C:/Users/Reemy/Documents/GitHub/std_googleAssistant/GUI/Icons/Next.png")

    next = Button(root, bg="white")

    next.config(image=photoN)

    next.pack(side="top", anchor=NE)

    l.pack()

    root.mainloop()