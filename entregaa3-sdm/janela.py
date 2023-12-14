import customtkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

janela = customtkinter.CTk()
janela.geometry('500x300')

def CliqueLogin():
    print('Fazer Login')
def CliqueCadastro():
    print('Fazer Cadastro')


texto = customtkinter.CTkLabel(janela, text='Fazer Login')
texto.pack(padx=20, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text='Seu e-mail')
email.pack(padx=20, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text='Sua senha', show='*')
senha.pack(padx=20, pady=10)

checkbox = customtkinter.CTkCheckBox(janela, text='Lembrar Login')
checkbox.pack(padx=10, pady=10)

#====== Botoes ========
BotaoLogin = customtkinter.CTkButton(janela, text='Login', command=CliqueLogin)
BotaoLogin.pack(padx=10, pady=10)

Register = customtkinter.CTkButton(janela, text='Registrar', command=CliqueCadastro)
Register.pack(padx=10, pady=10) 

class CustomTkinterApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Custom Tkinter App')
    
        #Criar um botão
        self.botao = tk.Button(self.root, text='Remover Botão', command=self.botao.pack)
        self.botao.pack(pady=10)
                               
    def remover_botao(self):
    #Destruir o botão
        self.botao.destroy()

janela.mainloop()