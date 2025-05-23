import customtkinter as ctk
import subprocess
import sqlite3
from PIL import Image

conexao= sqlite3.connect('registro_clientes.db')
cursor=conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
''')



ctk.set_appearance_mode("white")
ctk.set_default_color_theme("blue")
jan = ctk.CTk()
jan.geometry("400x450")
jan.title("Divina Pele")
jan.configure(fg_color="#DEB887")

def mudar ():
    nome=nom.get()
    emailok=email.get()
    if nome.strip and emailok.strip():
        cursor.execute('INSERT INTO clientes (nome,email) VALUES (?,?)', (nome,emailok))
        conexao.commit()
        id_gerado=cursor.lastrowid
        print(f"Nome e Email salvo com sucesso")


    with open("cliente_registrado.txt","w") as f:
        f.write(str(id_gerado))

    subprocess.Popen(["python","registro_dia.py"])
    jan.iconify()
    jan.destroy()


ok=ctk.CTkLabel(jan, text="Nome:", font=("Arial",25))
ok.pack(pady=15,anchor="w",padx=20)

nom=ctk.CTkEntry(jan,height=15,width=300,font=("Arial",20))
nom.pack(padx=10,anchor="w",pady=1)

okok=ctk.CTkLabel(jan, text="Email:", font=("Arial",25))
okok.pack(pady=15,anchor="w",padx=20)

email=ctk.CTkEntry(jan,height=15,width=300,font=("Arial",20))
email.pack(padx=10,anchor="w",pady=1)

confirm=ctk.CTkButton(jan,text="confirmar", font=("Arial",30),width=200,height=65,fg_color="#006400",command=mudar)
confirm.pack(pady=40)

image_pil= Image.open("Divina Pele.jpg") 
image_ctk=ctk.CTkImage(light_image=image_pil, dark_image=image_pil, size=(175, 175)) 

label_imagem=ctk.CTkLabel(jan,image=image_ctk,text="" ) 
label_imagem.pack(pady=5) 



jan.mainloop()

conexao.close()