import webbrowser
import tkinter as tk
from tkinter import *
from tkcalendar import *
from PIL import Image, ImageTk


class Interface(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainPage, CalendarPage, Investments):
            frame = F(container, self)
            self.frames[F] = frame
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
        text = tk.Label(r, text="Customizable Budgeting App", width=50, height=5, bg='purple',
                        fg='white').grid()
        button = tk.Button(r, text='Budgeting Calendar', width=30,
                           command=lambda: controller.show_frame(CalendarPage)).grid(pady=5)
        button1 = tk.Button(r, text='Investments', width=30,
                            command=lambda: controller.show_frame(Investments)).grid(pady=5)
        button2 = tk.Button(r, text='Queens Budgeting Resources', width=30,
                            command=lambda: webbrowser.open_new_tab(
                                'https://www.queensu.ca/urs/resources/budget-resources')).grid(pady=5)

        load = Image.open("QEC-Purple.png")
        [imageSizeWidth, imageSizeHeight] = load.size

        newImageSizeWidth = int(imageSizeWidth / 2)
        newImageSizeHeight = int(imageSizeHeight / 2)

        load = load.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = tk.Label(r, image=render)

        img.image = render
        img.place(x=18, y=265)

        gap = tk.Label(r, text="", height=2, bg='blue').grid()


class CalendarPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        r = self
        r.configure(bg='purple')
        cd = Calendar(r, selectmode="day", year=2020, month=5)
        cd.pack(pady=20)

        def onclick():
            label.config(text=cd.get_date())

        button = tk.Button(r, text="Get Date", command=onclick)
        button.pack(pady=20)
        button1 = tk.Button(r, text='Go Back', width=30,
                            command=lambda: controller.show_frame(MainPage))
        button1.pack(pady=20)
        label = tk.Label(r, text="")
        label.pack(pady=20)


class Investments(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        r = self
        # take the data
        lst = [('Groceries', 'Price:', 'Rent&Utilities', 'Price:'),
               ('Apples', 10.00, 'Aug', 600.30),
               ('Chicken', 15.50, 'Sep', 611.00),
               ('Broccoli', 13.20, 'Oct', 609.30),
               ('Milk', 6.00, 'Nov', 605.40)]
        total_rows = len(lst)
        total_columns = len(lst[0])
        r.configure(bg='purple')
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                e = Entry(r, width=7, fg='blue',
                               font=('Arial', 16, 'bold'))

                e.grid(row=i, column=j)
                e.insert(END, lst[i][j])


app = Interface()
app.title('Student Budgeting App')
windowWidth = app.winfo_reqwidth()
windowHeight = app.winfo_reqheight()
positionRight = int(app.winfo_screenwidth() / 2 - windowWidth / 2 - 50)
positionDown = int(app.winfo_screenheight() / 2 - windowHeight / 2 - 100)
app.geometry("+{}+{}".format(positionRight, positionDown))
app.mainloop()
