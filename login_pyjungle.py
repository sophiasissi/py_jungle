import customtkinter
from tkinter import *

def login_click():
    #print('Clicou')
    #x = entry1.get()
    #y = entry2.get()
    #print(x)
    #print(y)
    janela.quit()

janela = Tk(className='Sistema de Login - Window Color')
janela.geometry('700x400')
janela.title('Sistema de Login PYjungle')
janela.iconbitmap("")
janela.resizable(False, False)
janela['bg']='green'


#Trabalhando
img = PhotoImage(file="imagem\Img2.png")
label_img = customtkinter.CTkLabel(master=janela, image=img)
label_img. place(x=60, y=100)

label_tt = customtkinter.CTkLabel(master=janela, text="BEM VINDO\n AO PYJUNGLE!",
font=("Roboto", 30), text_color='#100'). place(x=60, y=10)

#frame
frame = customtkinter.CTkFrame(master=janela, width=350, height=396)
frame.pack(side=RIGHT)

#frame widgets
label =  customtkinter.CTkLabel(master=frame, text="Faça seu cadastro", font=('Roboto', 30))
label.place(x=25, y=5)


entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Nome de usuário", width=300, font=("Roboto", 14))
entry1.place(x=25, y=105)
label = customtkinter.CTkLabel(master=frame, text="*O campo de usuário e de carater obrigatorio.", text_color="green", font=("Roboto", 9)). place(x=25, y=135)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Senha do usuário", width=300, font=("Roboto", 14))
entry2.place(x=25, y=175)
label = customtkinter.CTkLabel(master=frame, text="*O campo de senha do usuario e de carater obrigatorio.", text_color="green", font=("Roboto", 9)). place(x=25, y=205)


checkbox = customtkinter.CTkCheckBox(master=frame, text="Lembra-se de mim sempre").place(x=25, y=235)

button = customtkinter.CTkButton(master=frame, text="LOGIN", width=300,command=login_click).place(x=25, y=285)

janela.mainloop()


