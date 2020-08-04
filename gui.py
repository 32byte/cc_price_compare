import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()



    def create_widgets(self):

        def show_search():
            search_saved = self.search.get()
            print(search_saved)

        self.menu = tk.Menu(self)
        self.master.config(menu=self)
        helpmenu = Menu(menu)



        self.title = tk.Label(self, text="Compare prices for games", font="bold")
        self.title.pack()

        self.info_button = tk.Button(self, text="Info", bg="#c9c9c9", fg="grey")
        self.pack(side="top")

        self.label1 = tk.Label(self, text="Enter Game here:")
        self.label1.pack(side="left", pady=8)

        self.search = tk.Entry(self)
        self.search.pack(side="left", padx=15)

        self.search_button = tk.Button(self, text="Search", bg="grey", command=show_search)
        self.search_button.pack(side="left", padx=10)

        self.label2 = tk.Label()



root = tk.Tk()
app = App(master=root)
app.mainloop()
