import customtkinter as ctk
import subprocess
import sqlite3

#banco de dados:

conexao= sqlite3.connect('registro_clientes.db') 
cursor=conexao.cursor()

#comandos:

def voltar():
    subprocess.Popen(["python","main_page.py"])
    jan.iconify()
    jan.destroy()


def mostrar_agendamentos():
   cursor.execute("""
                  SELECT clientes.nome,agendamento.data,agendamento.horario,agendamento.serviço
                  FROM agendamento
                  JOIN clientes ON agendamento.id_cliente=clientes.id
                  ORDER BY agendamento.data,agendamento.horario
    """)
   dados=cursor.fetchall()
   
   if not dados:
       tabela_agendamentos.insert("end","Nenhum agendamento realizado.")
    
   else:
       for nome,data,hora,serviço in dados:
           linha=f"Cliente: {nome}\nData: {data} | Horario: {hora} | Serviço: {serviço}\n"
           linha+="-"*60 +"\n"
           tabela_agendamentos.insert("end",linha)



ctk.set_appearance_mode("white")
ctk.set_default_color_theme("blue")
jan = ctk.CTk()
jan.geometry("600x550")
jan.title()
jan.configure(fg_color="#DEB887")

label=ctk.CTkLabel(jan,text="Tabela de agendamentos:",font=("Arial",30))
label.pack(anchor="w",pady= 20,padx=15)

tabela_agendamentos=ctk.CTkTextbox(jan,font=("Arial",16),width=550,height=400)
tabela_agendamentos.pack()


butao=ctk.CTkButton(jan,text="Voltar",font=("Arial",25),command=voltar,fg_color="#8B4513")
butao.pack(pady=20)

mostrar_agendamentos()


jan.mainloop()
conexao.close()