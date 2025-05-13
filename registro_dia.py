import customtkinter as ctk
import tkinter as tk
from tkcalendar import Calendar
import subprocess



ctk.set_appearance_mode("white")
ctk.set_default_color_theme("blue")
jan = ctk.CTk()
jan.geometry("450x450")
jan.title()
jan.configure(fg_color="#DEB887")

def ok():
    subprocess.Popen(["python","registro_serviço.py"])
    jan.iconify()
    jan.destroy()



calendario= Calendar(jan,selectmode='day',font=("Arial",15)) 
calendario.pack(pady=20)

confirm= ctk.CTkButton(jan,text="confirmar",font=("Arial",20),fg_color="#006400",command=ok)
confirm.pack(pady=15)





jan.mainloop()