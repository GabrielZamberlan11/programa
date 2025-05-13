import customtkinter as ctk
import subprocess
import sqlite3

conexao= sqlite3.connect('registro_clientes.db')
cursor=conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

ctk.set_appearance_mode("white")
ctk.set_default_color_theme("blue")
jan = ctk.CTk()
jan.geometry("400x450")
jan.title()
jan.configure(fg_color="#DEB887")

def mudar ():
    nome=nom.get()
    emailok=email.get()
    if nome.strip and emailok.strip():
        cursor.execute('INSERT INTO usuarios (nome,email) VALUES (?,?)', (nome,emailok))
        conexao.commit()
        print(f"Nome {nome} e Email {email} salvo com sucesso")

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





jan.mainloop()

conexao.close()