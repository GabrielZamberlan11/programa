import customtkinter as ctk
import subprocess
import sqlite3
from PIL import Image

#banco de dados

mapa_nome_id= {}
id_selecionado=None


conexao= sqlite3.connect('registro_clientes.db') 
cursor=conexao.cursor()

cursor.execute("SELECT id,nome FROM clientes")
resultados=cursor.fetchall()

mapa_nome_id= {nome: id for id, nome in resultados}
nomes=list(mapa_nome_id.keys())

#comandos

def carregar():
    clientes.configure(values=nomes)
    clientes.set("")


def ao_selecionar(event):
    global id_selecionado
    nome_selecionado=clientes.get()
    id_correspondente=mapa_nome_id.get(nome_selecionado)
    if id_correspondente:
        id_selecionado=id_correspondente
        confirmação.configure(text=f"ID selecionado: {id_correspondente}")
    else:
        id_selecionado=None
        confirmação.configure(text="Nome nao encontrado.")
        

def ao_digitar(event):
    texto=clientes.get().lower()
    filtrados=[nome for nome in nomes if texto in nome.lower()]
    clientes.configure(values=filtrados)

    nome_exato=clientes.get()
    if nome_exato in mapa_nome_id:
        ao_selecionar(event=None)


def fazer_cadastro():
    subprocess.Popen(["python","registro_nome.py"])
    jan.iconify()
    jan.destroy()


def confirm():
    if id_selecionado is not None:
        with open("cliente_registrado.txt","w") as f:
            f.write(str(id_selecionado))
    
        subprocess.Popen(["python","registro_dia.py"])
        jan.iconify()
        jan.destroy()
    else:
        confirmação.configure(text="Selecione um cliente válido.")
    

def agendados():
    subprocess.Popen(["python","agendamentos.py"])
    jan.iconify()
    jan.destroy()

#janela

ctk.set_appearance_mode("white")
ctk.set_default_color_theme("blue")
jan = ctk.CTk()
jan.geometry("500x450")
jan.title()
jan.configure(fg_color="#DEB887")


cadastro=ctk.CTkButton(jan,text="Fazer Cadastro",font=("Arial",30),command= fazer_cadastro,fg_color="#006400")
cadastro.pack(anchor="w", pady=50,padx=15)

okok=ctk.CTkLabel(jan,text="Se o cliente ja tiver cadastrado no sistema,\n selecione o cliente na entrada abaixo\n e clique em agendar.",font=("Arial",23))
okok.pack()

clientes=ctk.CTkComboBox(jan,font=("Arial",20),height=20,width=250,values=[])
clientes.pack(anchor="w", padx=15,pady=30)

carregar()


clientes.bind("<KeyRelease>", ao_digitar)
clientes.bind("<<ComboboxSelected>>",ao_selecionar)

apenas_agendar=ctk.CTkButton(jan,text="Agendamento",font=("Arial",30),command=confirm,fg_color="#006400")
apenas_agendar.pack(pady=20,anchor="w",padx=30)

tabela=ctk.CTkButton(jan,text="Ver agendamentos",font=("Arial",25),height=40,width=100,command=agendados,fg_color="#8B4513")
tabela.place(x=250,y=330)

confirmação=ctk.CTkLabel(jan,text="")
confirmação.pack()

#imagem
image_pil= Image.open("Divina Pele.jpg") 
image_ctk=ctk.CTkImage(light_image=image_pil, dark_image=image_pil, size=(160, 160)) 

label_imagem=ctk.CTkLabel(jan,image=image_ctk,text="" ) 
label_imagem.place(x=300,y=-20)




jan.mainloop()

conexao.close()