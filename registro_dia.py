import customtkinter as ctk
import tkinter as tk
from tkcalendar import Calendar
import subprocess
import sqlite3

conexao= sqlite3.connect('registro_clientes.db')
cursor=conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS eventos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        serviço TEXT NOT NULL
        data TEXT NOT NULL
        horario TEXT NOT NULL
    )
''')

conexao.commit()

ctk.set_appearance_mode("white")
ctk.set_default_color_theme("blue")
jan = ctk.CTk()
jan.geometry("450x450")
jan.title()
jan.configure(fg_color="#DEB887")

def ok():
    data=calendario.get_date()
    if nome.strip and emailok.strip():
        cursor.execute('INSERT INTO usuarios (data,) VALUES (?)', (data,))
        conexao.commit()
        print(f"Data {data} salvo com sucesso")

    subprocess.Popen(["python","registro_serviço.py"])
    jan.iconify()
    jan.destroy()



calendario= Calendar(jan,date_pattern='dd/mm/yy',font=("Arial",15)) 
calendario.pack(pady=20)

confirm= ctk.CTkButton(jan,text="confirmar",font=("Arial",20),fg_color="#006400",command=ok)
confirm.pack(pady=15)





jan.mainloop()