import tkinter as tk
from PIL import Image
from PIL import ImageTk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        def show_search():
            search_saved = self.search.get()
            print(search_saved)






        # ---initianting  widgets-------------------------------------------------------------------------------------
        self.title = tk.Label(self, text="Compare prices for games", font=("Gotham", 15,), pady=5)
        self.info_button = tk.Button(self, text="Info", bg="#c9c9c9", fg="grey", padx=5)
        self.label1 = tk.Label(self, text="Game:", font=("Calibri", 12),)
        self.search = tk.Entry(self)

        self.search_button_image = Image.open("C:/Users/andrzago20/GitHub/cc_price_compare/images/search_button2.png")
        self.search_button_image = self.search_button_image.resize((17, 17), Image.ANTIALIAS)
        self.search_button_image_tk = ImageTk.PhotoImage(self.search_button_image)
        #self.search_button_design = Image.open("C:/Users/andrzago20/GitHub/cc_price_compare/images/button.png")
        #self.search_button_design = self.search_button_design.resize((192, 108), Image.ANTIALIAS)

        self.search_button = tk.Button(self, text="Search", bg="#c9c9c9", image=self.search_button_image_tk,
                                       compound="left", command=show_search)
        #self.search_button.config(image=self.search_button_design)
        self.all_prices_label = tk.Label(self, text="All prices:", font=("Calibri", 10))
        self.steam_label = tk.Label(self, text="Steam.com", font="bold")
        self.instnat_label = tk.Label(self, text="Instant-Gaming.com", font="bold")
        self.g2a_label = tk.Label(self, text="g2a.com", font="bold")
        self.steam1 = tk.Label(self)
        self.steam2 = tk.Label(self)
        self.steam3 = tk.Label(self)
        self.instant1 = tk.Label(self)
        self.instant2 = tk.Label(self)
        self.instant3 = tk.Label(self)
        self.g2a1 = tk.Label(self)
        self.g2a2 = tk.Label(self)
        self.g2a2 = tk.Label(self)
        self.g2a3 = tk.Label(self)








        self.create_widgets()





    def create_widgets(self):


        # self.menu = tk.Menu(self)
        #self.master.config(menu=self)
        #helpmenu = Menu(menu)


        #adding widgets to grid----------------------------------
        self.title.grid(columnspan=3, sticky="N", )
        self.info_button.grid(row=0, column=3, sticky="E")
        self.label1.grid(row=1, column=0)
        self.search_button.grid(row=1, column=2, padx=10)
        self.search.grid(row=1, column=1)
        self.all_prices_label.grid(row=3, column=0, pady=10)
        self.steam_label.grid(row=4, column=0)
        self.instnat_label.grid(row=4, column=1, padx= 10)
        self.g2a_label.grid(row=4, column=2)
        self.steam1.grid(row=5, column=0)
        self.steam2.grid(row=6, column=0)
        self.steam3.grid(row=7, column=0)
        self.instant1.grid(row=5, column=1)
        self.instant2.grid(row=6, column=1)
        self.instant3.grid(row=7, column=1)
        self.g2a1.grid(row=5, column=2)
        self.g2a2.grid(row=6, column=2)
        self.g2a3.grid(row=7, column=2)



root = tk.Tk()
app = App(master=root)
app.mainloop()
