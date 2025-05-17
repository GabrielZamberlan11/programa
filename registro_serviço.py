import customtkinter as ctk
import sqlite3



conexao= sqlite3.connect('registro_clientes.db') 
cursor=conexao.cursor() 

with open("data.txt","r") as f:
        data=f.read().strip()

cursor.execute("SELECT * FROM  usuarios ORDER BY id DESC LIMIT 1") 
resultado=cursor.fetchone()
if resultado:
     id_cliente=resultado[0]
else:
     id_cliente=None

def salvar(): 
    hora=escolhahora.get() 
    serviçoo= escolha.get() 

    if hora.strip and serviçoo.strip(): 
        cursor.execute('INSERT INTO agendamento (id_cliente,serviço,data,horario) VALUES (?,?,?,?)', (id_cliente,serviçoo,data,hora)) 
        conexao.commit() 
        print(f"Serviço, Data e Hora salvo com sucesso") 




ctk.set_appearance_mode("white")
ctk.set_default_color_theme("blue")
jan = ctk.CTk()
jan.geometry("400x450")
jan.title()
jan.configure(fg_color="#DEB887")

serviços=["Máscaras faciais", "Penteados", "Maquiagens","Tratamento de rejuvenescimento", "Aromaterapia", "Massagens", "Limpeza de Pele"]


escolha=ctk.CTkComboBox(jan,values=serviços,font=("Arial",18),height=20,width=200)
escolha.pack(pady=20,anchor="w")
 

horarios=["09:00", "10:00", "12:00","14:00", "15:00","16:00","17:00"]

escolhahora=ctk.CTkComboBox(jan,values=horarios,font=("Arial",18),height=20,width=200)
escolhahora.pack(pady=20,anchor="w")

butao=ctk.CTkButton(jan,text="confirmar",font=("Arial",20),fg_color="#006400",command=salvar)
butao.pack(pady=25)



jan.mainloop()

conexao.close()