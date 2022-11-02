import tkinter
from tkinter import *
from tkinter import ttk

# cores --------------------------------
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha

fundo = "#3b3b3b"

#  -------------- CONFIGURANDO A JANELA -----------------
janela = Tk()
janela.title('Jogo PPT')
janela.geometry('260x280')
janela.configure(bg=fundo)

#  -------------- DIVIDINDO A JANELA -----------------

frame_cima = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW)

frame_baixo = Frame(janela, width=260, height=300, bg=co0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)

style = ttk.Style(janela)
style.theme_use('clam')

#  -------------- CONFIGURANDO FRAME CIMA -----------------

jg_1 = Label(frame_cima, text='VOCÊ', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
jg_1.place(x=20, y=70)

jg_1_linha = Label(frame_cima, height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
jg_1_linha.place(x=0, y=0)

jg_1_point = Label(frame_cima, text='0', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
jg_1_point.place(x=50, y=20)

#  -------------- CONFIGURANDO PONTO -----------------

point = Label(frame_cima, text=':', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
point.place(x=125, y=20)

# ----------- PC ----------------------

jg_2_point = Label(frame_cima, text='0', height=1, anchor='center', font=('Ivy 30 bold'), bg=co1, fg=co0)
jg_2_point.place(x=170, y=20)

jg_2 = Label(frame_cima, text='PC', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
jg_2.place(x=205, y=70)

jg_2_linha = Label(frame_cima, height=10, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co0)
jg_2_linha.place(x=255, y=0)

empate_linha = Label(frame_cima, width=255, anchor='center', font=('Ivy 1 bold'), bg=co0, fg=co0)
empate_linha.place(x=0, y=95)


janela.mainloop()
