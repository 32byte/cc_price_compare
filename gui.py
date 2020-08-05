import tkinter as tk
from PIL import Image
from PIL import ImageTk


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

        # self.menu = tk.Menu(self)
        #self.master.config(menu=self)
        #helpmenu = Menu(menu)



        self.title = tk.Label(self, text="Compare prices for games", font=("Gotham", 15, )).grid(row=0, column=1)
        #self.title.pack()

        self.info_button = tk.Button(self, text="Info", bg="#c9c9c9", fg="grey").grid(row=0, column=0)
        #self.pack()

        self.label1 = tk.Label(self, text="Game:", font=("Calibri", 12), padx=10, pady=87).grid(row=2, column=0)
        #self.label1.pack()

        self.search = tk.Entry(self)
        self.search.grid(row=1, column=1)
       #self.search.pack()

        self.search_button_image = Image.open("C:/Users/andrzago20/GitHub/cc_price_compare/images/search_button2.png")
        self.search_button_image = self.search_button_image.resize((17,17), Image.ANTIALIAS)
        self.search_button_image_tk = ImageTk.PhotoImage(self.search_button_image)


        self.search_button = tk.Button(self, text="Search", bg="#c9c9c9", image=self.search_button_image_tk, compound="left", command=show_search)
        self.search_button.grid(row=1)# colummn=2)
       # self.search_button.pack(side="left", padx=10)

        self.all_prices_label = tk.Label(self, text="All prices:", font=("Calibri", 10)).grid(row=3, column=1)#.pack(0)



root = tk.Tk()
app = App(master=root)
app.mainloop()
