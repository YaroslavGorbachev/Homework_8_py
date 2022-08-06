from cProfile import label
from distutils.cmd import Command
from tkinter import filedialog
from tkinter import *   
from webbrowser import get
from tkinter import messagebox  
from tkinter import scrolledtext 
from os import path
import view
import csv
import out_data
import data
import out_search
import removal

def okno():
    window = Tk()
    window.title("Справочник контактов")
    window.geometry('500x500')
  
    lbl = Label(window, text="Привет я справочник \n чтобы со мной работать  используй: \n 'Список команд:",font=(50) )
    lbl.grid(column=3, row=0) 

    btn = Button(window,text="Показать спиок контактов",command=out_data.look_phone_book)
    btn.grid(column=3, row=1)  
    btn = Button(window,text="Добавить контак ",command=data.get_id)
    btn.grid(column=3, row=3)  
    btn = Button(window,text="Найти контак",command=out_search.search_view_number)
    btn.grid(column=3, row=5) 
    btn = Button(window,text="Удалить Контак ",command=removal.del_phone_number)
    btn.grid(column=3, row=5) 


    btn = Button(window,text="Выход ",command=exit)
    btn.grid(column=3, row=9) 

    


 








