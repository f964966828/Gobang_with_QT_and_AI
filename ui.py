import time
import tkinter as tk

class Gobang(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.frame = StartPage(self.container, self)
        self.show_start_page()

    def show_start_page(self):
        self.geometry('250x280')

        self.frame.stop = True
        self.frame = StartPage(self.container, self)
        self.frame.tkraise()

    def show_game_page(self):
        self.geometry('600x600')

        self.frame.stop = True
        self.frame = GamePage(self.container, self)
        self.frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.grid(row=0, column=0, sticky="nsew")
        self.stop = False

        label = tk.Label(self, text="Gobang", font=("Verdana", 18))
        label.pack(pady=40,padx=80)

        PvPButton = tk.Button(self, text="PvP",
                            command=lambda: controller.show_game_page())
        PvPButton.pack(pady=20)

        PvCButton = tk.Button(self, text="PvC",
                            command=lambda: controller.show_game_page())
        PvCButton.pack(pady=20)

class GamePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.grid(row=0, column=0, sticky="nsew")
        self.controller = controller
        self.stop = False

        self.time_label = tk.Label(text="", font=('Helvetica', 48))
        self.time_label.pack()
        self.time_label.place(x=150, y=10)

        BackButton = tk.Button(self, text="Back",
                            command=lambda: controller.show_start_page())
        BackButton.pack()
        BackButton.place(x=10, y=10)

        self.start_time = time.time()
        self.update_clock()

    def update_clock(self):
        now = time.strftime("%H:%M:%S", time.gmtime(time.time() - self.start_time))
        self.time_label.configure(text=now)
        if not self.stop:
            self.controller.after(1000, self.update_clock)
        else:
            self.time_label.configure(text="")

app = Gobang()
app.mainloop()