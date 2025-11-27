import tkinter as tk


class HomePage(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("New Hub")
        self.geometry("800x500")
        self.configure(bg="lightgray")
        self.resizable(width=False, height=False)


    def get_root(self):
        return self


class Animate:
    def __init__(self, root):
        # start size

        self.width = 400
        self.height = 200
        self.target_width = 800
        self.target_height = 500
        self.duration = 3000
        self.steps = 60
        self.step_time = self.duration//self.steps
        self.dx = (self.target_width-self.width)/self.steps
        self.dy = (self.target_height-self.height)/self.steps
        self.root = root.get_root()

        # create the frame with initial size
        self.frame = tk.Frame(self.root, bg="lightblue", width=self.width, height=self.height)
        self.frame.pack(pady=20)
        self.frame.pack_propagate(False)

        self.label = tk.Label(self.frame, text="News Hub", font=("Arial", 16), bg="lightblue")
        self.label.pack(expand=True)

        self.animate_step(0)

    def animate_step(self, step):
        if step <= self.steps:

            self.width +=self.dx
            self.height +=self.dy
            self.frame.configure(width=int(self.width), height=int(self.height))
            self.frame.after(self.step_time, lambda: self.animate_step(step + 1))




if __name__ == "__main__":
    root = HomePage()
    animation = Animate(root)
    root.mainloop()