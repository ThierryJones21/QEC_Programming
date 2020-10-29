import webbrowser
import tkinter as tk
from tkinter import *
from PIL import Image


class Interface(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainPage, GuideMenu, EquipmentMenu, BBBCMenu, CLMenu, CAMenu, ShipSearchMenu):
            frame = F(container, self)
            self.frames[F] = frame;
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        r = self
        r.configure(bg='blue')
        text = tk.Label(r, text="Customizable Budgeting App", width=50, height=5, bg='blue',
                        fg='white').grid()
        button = tk.Button(r, text='Player Guide', width=30,
                           command=lambda: controller.show_frame(GuideMenu)).grid(pady=5)
        button1 = tk.Button(r, text='Equipment Guide', width=30,
                            command=lambda: controller.show_frame(EquipmentMenu)).grid(pady=5)
        button2 = tk.Button(r, text='Ship Search', width=30,
                            command=lambda: controller.show_frame(ShipSearchMenu)).grid(pady=5)
        button3 = tk.Button(r, text='Tier List', width=30,
                            command=lambda: webbrowser.open_new_tab('https://tinyurl.com/tsg2gnc')).grid(pady=5)
        gap = tk.Label(r, text="", height=2, bg='black').grid()


class GuideMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        r = self
        r.configure(bg='blue')
        text = tk.Label(r, text="", width=50, height=5, bg='black', fg='white').grid()
        button = tk.Button(r, text='General FAQ', width=30,
                           command=lambda: webbrowser.open_new_tab('https://azurlane.koumakan.jp/FAQ')).grid(pady=5)
        button1 = tk.Button(r, text='General Guide', width=30,
                            command=lambda: webbrowser.open_new_tab(
                                'https://azurlane.koumakan.jp/User:Shipposting_Duck')).grid(pady=5)
        button2 = tk.Button(r, text='Beginner\'s Guide', width=30,
                            command=lambda: webbrowser.open_new_tab(
                                'https://azurlane.koumakan.jp/User:Itsfyh/EN_Beginner\'s_Guide')).grid(pady=5)
        button3 = tk.Button(r, text='New Player Ship Guide', width=30,
                            command=lambda: Image.open('Images/newShipGuide.png').show()).grid(pady=5)
        button4 = tk.Button(r, text='Go Back', width=30,
                            command=lambda: controller.show_frame(MainPage)).grid(pady=5)
        gap = tk.Label(r, text="", height=2, bg='black').grid()


class EquipmentMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        r = self
        r.configure(bg='blue')
        text = tk.Label(r, text="Guides Provided by Nerezza", width=50, height=5, bg='black', fg='white').grid()
        button = tk.Button(r, text='Battle Ships Guide (BB/BC)', width=30,
                           command=lambda: controller.show_frame(BBBCMenu)).grid(pady=5)
        button1 = tk.Button(r, text='Carrier Ships Guide (CL/CV/BBV)', width=30,
                            command=lambda: Image.open('Images/Planes.jpg').show()).grid(pady=5)
        button2 = tk.Button(r, text='Light Cruisers Guide (CL)', width=30,
                            command=lambda: controller.show_frame(CLMenu)).grid(pady=5)
        button3 = tk.Button(r, text='Heavy Cruisers Guide (CA)', width=30,
                            command=lambda: controller.show_frame(CAMenu)).grid(pady=5)
        button4 = tk.Button(r, text='Destroyer Ships Guide (DD)', width=30,
                            command=lambda: Image.open('Images/GeneralDD.jpg').show()).grid(pady=5)
        button5 = tk.Button(r, text='Go Back', width=30,
                            command=lambda: controller.show_frame(MainPage)).grid(pady=5)
        gap = tk.Label(r, text="", height=2, bg='black').grid()


class ShipSearchMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        r = self
        r.configure(bg='black')
        text = tk.Label(r, text="Enter Ship Name:", width=50, height=5, bg='black', fg='white').grid()

        mystring = tk.StringVar(r)
        entry = tk.Entry(r, textvariable=mystring).grid(pady=5)

        button = tk.Button(r, text='Search on Wiki', width=20,
                           command=lambda: webbrowser.open_new_tab(
                               'https://azurlane.koumakan.jp/' + mystring.get().capitalize())).grid(pady=10)

        button1 = tk.Button(r, text='Go Back', width=15,
                            command=lambda: controller.show_frame(MainPage).grid(pady=5))

        gap = tk.Label(r, text="", height=2, bg='black').grid()


class BBBCMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        r = self
        r.configure(bg='black')
        text = tk.Label(r, text="Guides Provided by Nerezza", width=50, height=5, bg='black', fg='white').grid()
        button = tk.Button(r, text='Barrage Focused w/ DD guns', width=30,
                           command=lambda: Image.open('Images/BarrageBBwDD.png').show()).grid(pady=5)
        button1 = tk.Button(r, text='Barrage Focused w/ CL guns', width=30,
                            command=lambda: Image.open('Images/BarrageBBwCL.png').show()).grid(pady=5)
        button2 = tk.Button(r, text='Shelling Focused w/ DD guns', width=30,
                            command=lambda: Image.open('Images/ShellingBBwDD.png').show()).grid(pady=5)
        button3 = tk.Button(r, text='Shelling Focused w/ CL guns', width=30,
                            command=lambda: Image.open('Images/ShellingBBwCL.png').show()).grid(pady=5)
        button4 = tk.Button(r, text='Mixed w/ DD guns', width=30,
                            command=lambda: Image.open('Images/GenericBBwDD.png').show()).grid(pady=5)
        button5 = tk.Button(r, text='Mixed w/ CL guns', width=30,
                            command=lambda: Image.open('Images/GenericBBwCL.png').show()).grid(pady=5)
        button6 = tk.Button(r, text='Go Back', width=30,
                            command=lambda: controller.show_frame(EquipmentMenu)).grid(pady=5)
        gap = tk.Label(r, text="", height=2, bg='black').grid()


class CLMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        r = self
        r.configure(bg='black')
        text = tk.Label(r, text="Guides Provided by Nerezza", width=50, height=5, bg='black', fg='white').grid()
        button = tk.Button(r, text='Gun Based CL', width=30,
                           command=lambda: Image.open('Images/GunBasedCL.jpg').show()).grid(pady=5)
        button1 = tk.Button(r, text='Torpedo Based CL', width=30,
                            command=lambda: Image.open('Images/TorpBasedCLwCL.jpg').show()).grid(pady=5)
        button2 = tk.Button(r, text='Torpedo Based CL w/ DD guns', width=30,
                            command=lambda: Image.open('Images/TorpBasedCLwDD.jpg').show()).grid(pady=5)
        button3 = tk.Button(r, text='Go Back', width=30,
                            command=lambda: controller.show_frame(EquipmentMenu)).grid(pady=5)
        gap = tk.Label(r, text="", height=2, bg='black').grid()


class CAMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        r = self
        r.configure(bg='black')
        text = tk.Label(r, text="Guides Provided by Nerezza", width=50, height=5, bg='black', fg='white').grid()
        button = tk.Button(r, text='Gun Based CA', width=30,
                           command=lambda: Image.open('Images/GunBasedCA.jpg').show()).grid(pady=5)
        button1 = tk.Button(r, text='Torpedo Based CA', width=30,
                            command=lambda: Image.open('Images/TorpBasedCA.jpg').show()).grid(pady=5)
        button2 = tk.Button(r, text='Go Back', width=30,
                            command=lambda: controller.show_frame(EquipmentMenu)).grid(pady=5)
        gap = tk.Label(r, text="", height=2, bg='black').grid()


app = Interface()
app.title('Student Budgeting App')
windowWidth = app.winfo_reqwidth()
windowHeight = app.winfo_reqheight()
positionRight = int(app.winfo_screenwidth() / 2 - windowWidth / 2 - 50)
positionDown = int(app.winfo_screenheight() / 2 - windowHeight / 2 - 80)
app.geometry("+{}+{}".format(positionRight, positionDown))
app.mainloop()