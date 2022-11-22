import tkinter
import random
import PIL.Image
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
from time import sleep

# cores --------------------------------
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"  # green / verde
co5 = "#e85151"  # red / vermelha

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

jogada_pc = Label(frame_baixo, text='', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
jogada_pc.place(x=190, y=10)

jogada_vc = Label(frame_baixo, text='', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co1)
jogada_vc.place(x=30, y=10)

# FUNÇÕES

global voce
global pc

ponto_vc = 0
ponto_pc = 0
rodadas = 5


# função logica
def jogar(i):
    global rodadas
    global ponto_vc
    global ponto_pc

    if rodadas > 0:
        print(rodadas)
        opc = ['Pedra', 'Papel', 'Tesoura']
        pc = random.choice(opc)

        voce = i

        #  IGUAL
        if voce == 'Pedra' and pc == 'Pedra' or voce == 'Papel' and pc == 'Papel' or voce == 'Tesoura' and pc == 'Tesoura':

            print('empate')
            empate_linha['bg'] = co3
            jg_1_linha['bg'] = co0
            jg_2_linha['bg'] = co0

        #  GANHA
        elif voce == 'Pedra' and pc == 'Tesoura' or voce == 'Tesoura' and pc == 'Papel' or voce == 'Papel' and pc == 'Pedra':

            print('VOCÊ GANHOU')
            empate_linha['bg'] = co0
            jg_1_linha['bg'] = co4
            jg_2_linha['bg'] = co0

            ponto_vc += 10

        #  PERDE
        elif voce == 'Pedra' and pc == 'Papel' or voce == 'Papel' and pc == 'Tesoura' or voce == 'Tesoura' and pc == 'Pedra':

            print('PC GANHOU')
            empate_linha['bg'] = co0
            jg_1_linha['bg'] = co0
            jg_2_linha['bg'] = co4

            ponto_pc += 10

        #  atualizando os pontos
        jg_1_point['text'] = ponto_vc
        jg_2_point['text'] = ponto_pc

        #  atualizando as rodadas
        rodadas -= 1

        jogada_pc['text'] = pc
        jogada_vc['text'] = voce

    else:
        jg_1_point['text'] = ponto_vc
        jg_2_point['text'] = ponto_pc

        #  termina o jogo
        fim_do_jogo()


# função iniciar
def iniciar_game():
    global pedra, papel, tesoura
    global b_pedra, b_papel, b_tesoura

    iniciar.destroy()

    #  ----------------------- pedra ---------------------------
    pedra = PIL.Image.open("imagens/pedra.png")
    pedra = pedra.resize((50, 50))
    pedra = ImageTk.PhotoImage(pedra)
    b_pedra = Button(frame_baixo, command=lambda: jogar('Pedra'), width=50, image=pedra, compound=CENTER, bg=co0,
                     fg=co0,
                     font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_pedra.place(x=15, y=60)

    #  ----------------------- papel -------------------------
    papel = PIL.Image.open('imagens/papel.png')
    papel = papel.resize((50, 50))
    papel = ImageTk.PhotoImage(papel)
    b_papel = Button(frame_baixo, command=lambda: jogar('Papel'), width=50, image=papel, compound=CENTER, bg=co0,
                     fg=co0,
                     font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_papel.place(x=100, y=55)

    #  ----------------------- tesoura -----------------------
    tesoura = PIL.Image.open('imagens/tesoura.png')
    tesoura = tesoura.resize((50, 50))
    tesoura = ImageTk.PhotoImage(tesoura)
    b_tesoura = Button(frame_baixo, command=lambda: jogar('Tesoura'), width=50, image=tesoura, compound=CENTER, bg=co0,
                       fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_tesoura.place(x=180, y=55)


# função terminar
def fim_do_jogo():

    global rodadas
    global ponto_vc
    global ponto_pc

    #  reiniciando as variaveis

    ponto_vc = 0
    ponto_pc = 0
    rodadas = 5

    #  destruindo as imagens

    b_pedra.destroy()
    b_papel.destroy()
    b_tesoura.destroy()

    #  definindo o vencedor

    jogador_vc = int(jg_1_point['text'])
    jogador_pc = int(jg_2_point['text'])

    if jogador_vc > jogador_pc:

        vencedor = Label(frame_baixo, text='PARABÉNS, VOCÊ GANHOU !!!', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co4)
        vencedor.place(x=5, y=60)
    elif jogador_pc > jogador_vc:

        vencedor = Label(frame_baixo, text='INFELIZMENTE, VOCÊ PERDEU !!!', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co5)
        vencedor.place(x=5, y=60)

    else:

        vencedor = Label(frame_baixo, text='FOI UM EMPATE !!!', height=1, anchor='center', font=('Ivy 10 bold'), bg=co0, fg=co3)
        vencedor.place(x=5, y=60)


    print('Acabou o Jogo')


#  ----------------------- inicio -----------------------
iniciar = Button(frame_baixo, command=iniciar_game, width=30, text='Pressione', bg=fundo, fg=co0, font=('Ivy 10 bold'),
                 anchor=CENTER,
                 relief=RAISED, overrelief=RIDGE)
iniciar.place(x=5, y=150)

janela.mainloop()
