import tkinter
import customtkinter as ctk
from tkinter import messagebox


window = tkinter.Tk()
window.title("Volunteer Login")
window.geometry('640x400')
window.configure(bg='#888988')


# button1 = ctk.CTkButton(window, text='MY EVENT', bg="light blue")
# button1.place(x=10,y=10)
# button2 = ctk.CTkButton(window, text='MANAGE EVENT', bg="light blue")
# button2.place(x=10,y=40)


my_tab = ctk.CTkTabview(window)
my_tab.pack(pady=10)
my_tab.place(x=10,y=30)
case_1 = my_tab.add('NAME OF THE EVENT')
case_2 = my_tab.add('MAX NO OF PARTICIPANTS')
case_3 = my_tab.add('RULES OF THE EVENT')
case_4 = my_tab.add('TIME PERIOD OF THE EVENT')
button1 = ctk.CTkButton(case_1, text='enter', bg_color="#888988", height=10, width=20)
button1.place(x=10, y=10)

button2 = ctk.CTkButton(case_2, text='enter', bg_color="#888988", height=10, width=25)
button2.place(x=10, y=50)

button3 = ctk.CTkButton(case_3, text='enter', bg_color="#888988", height=10, width=25)
button3.place(x=10, y=90)

button4 = ctk.CTkButton(case_4, text='enter', bg_color="#888988", height=10, width=25)
button4.place(x=10, y=130)


window.mainloop()
