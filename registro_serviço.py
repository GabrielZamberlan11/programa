import customtkinter as ctk
import sqlite3
import subprocess
from PIL import Image

conexao= sqlite3.connect('registro_clientes.db') 
cursor=conexao.cursor() 

with open("data.txt","r") as f:
     data=f.read().strip()

with open("cliente_registrado.txt","r") as f:
     id_cliente=f.read().strip()

def salvar(): 
    hora=escolhahora.get() 
    serviçoo= escolha.get() 

    if hora.strip and serviçoo.strip(): 
        cursor.execute('INSERT INTO agendamento (id_cliente,serviço,data,horario) VALUES (?,?,?,?)', (id_cliente,serviçoo,data,hora)) 
        conexao.commit() 
        print(f"Serviço, Data e Hora salvo com sucesso") 


def voltar():
     subprocess.Popen(["python","main_page.py"])
     jan.iconify()
     jan.destroy()

ctk.set_appearance_mode("white")
ctk.set_default_color_theme("blue")
jan = ctk.CTk()
jan.geometry("400x450")
jan.title("Divina Pele")
jan.configure(fg_color="#DEB887")

serviços=["Máscaras faciais", "Penteados", "Maquiagens","Tratamento de rejuvenescimento", "Aromaterapia", "Massagens", "Limpeza de Pele"]


escolha=ctk.CTkComboBox(jan,values=serviços,font=("Arial",18),height=20,width=200)
escolha.pack(pady=20,anchor="w")
 

horarios=["09:00", "10:00", "12:00","14:00", "15:00","16:00","17:00"]

escolhahora=ctk.CTkComboBox(jan,values=horarios,font=("Arial",18),height=20,width=200)
escolhahora.pack(pady=20,anchor="w")

butao=ctk.CTkButton(jan,text="confirmar",font=("Arial",20),fg_color="#006400",command=salvar)
butao.pack(pady=25)

voltei=ctk.CTkButton(jan,text="Voltar para tela inicial",font=("Arial",25),command=voltar,fg_color="#B8860B")
voltei.pack(pady=25,anchor="w",padx=15)


image_pil= Image.open("Divina Pele.jpg") 
image_ctk=ctk.CTkImage(light_image=image_pil, dark_image=image_pil, size=(175, 175)) 

label_imagem=ctk.CTkLabel(jan,image=image_ctk,text="" ) 
label_imagem.pack(pady=5) 




jan.mainloop()

conexao.close()