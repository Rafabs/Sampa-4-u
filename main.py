import sys
import os
sys.path.append('Mapa dos Trilhos')
sys.path.append('Mapa dos Trilhos\\Linhas')
from PIL import Image, ImageTk  # Manipular imagens
from datetime import datetime
from tkinter import ttk
import tkinter as tk
from cet import transito
from temperatura import get_weather
from gtfs import sptrans
from mapa import mapa_global
from Metrô_SP_L1 import line1
from Metrô_SP_L2 import line2
from Metrô_SP_L3 import line3
from Metrô_SP_L4 import line4
from Metrô_SP_L5 import line5
from CPTM_SP_L7 import line7
from CPTM_SP_L8 import line8
from CPTM_SP_L9 import line9
from CPTM_SP_L10 import line10
from CPTM_SP_L11 import line11
from CPTM_SP_L12 import line12
from CPTM_SP_L13 import line13
from Metrô_SP_L15 import line15
from Pirapora import pirapora
from Guararema import guararema

# Criando a janela
layout = tk.Tk()
layout.title("SAMPA 4U")
# Define uma largura e altura específicas para a janela
layout.geometry(f"{1920}x{1080}")

canvas = tk.Canvas(layout, width=1920, height=1080)
canvas.pack()
canvas.configure(bg='#333333')

# Carrega a imagem usando o PIL
image = Image.open('Mapa dos Trilhos\\Favicon\\SP4U_LOGO.ico')
photo = ImageTk.PhotoImage(image)

# Define o ícone
layout.iconphoto(False, photo)

# Carrega o logotipo do SP4U
logo = Image.open("Mapa dos Trilhos\\Imgs\\SP4U_LOGO.jpg")
# Redimensiona a imagem para ajustar ao tamanho do canvas
logo = logo.resize((100, 100))
logo_tk = ImageTk.PhotoImage(logo)
logo_label = ttk.Label(layout, image=logo_tk)
logo_label.place(x=10, y=10)

# Trânisto CET/SP
vel_CentroBairro, vel_BairroCentro = transito()

# Texto de saudação inicial
nome_usuario = os.getlogin()
canvas.create_text(120, 20, text=('Olá, ' + nome_usuario),
                   font="Helvetica 12", anchor="w", fill='#FFFFFF')

# Temperatura + data + hora
temperatura = canvas.create_text(
    120, 40, text=get_weather(), font="Helvetica 12", anchor="w", fill='#FFFFFF')
data_hora = canvas.create_text(120, 60, text=datetime.now().strftime(
    "%d/%m/%Y %H:%M:%S"), font="Helvetica 12", anchor="w", fill='#FFFFFF')

# Informações de Trânsito CET
centro_bairro = canvas.create_text(120, 80, text=(
    "Centro/Bairro:", vel_CentroBairro), font="Helvetica 12", anchor="w", fill='#FFFFFF')
bairro_centro = canvas.create_text(120, 100, text=(
    "Bairro/Centro:", vel_BairroCentro), font="Helvetica 12", anchor="w", fill='#FFFFFF')

# Código das cores do mapa (em ordem numérica)
azul = "#0455A1"
verde = "#007E5E"
vermelha = "#EE372F"
amarela = "#FFF000"
lilás = "#9B3894"
rubi = "#CA016B"
diamante = "#97A098"
esmeralda = "#01A9A7"
turquesa = "#049FC3"
coral = "#F68368"
safira = "#133C8D"
jade = "#00B352"
prata = "#C0C0C0"

# Código das cores de background
preto = "#000000"
branco = "#FFFFFF"

# Criando o primeiro frame (Mapas)
frame_mapas = ttk.LabelFrame(layout, text="Mapas", labelanchor='n')
frame_mapas.place(relx=0.5, rely=0, anchor=tk.N)

# Botões do primeiro frame
map_transp_button = tk.Button(
    frame_mapas, text="Acessar Mapa", command=mapa_global, fg="#ffffff", bg="#442fff")
map_transp_button.pack(pady=5, fill='both', expand=True)

# Criando o frame (Sistemas)
frame_sistemas = ttk.LabelFrame(
    layout, text="Sistemas de Buscas de Linhas", labelanchor='n')
frame_sistemas.place(relx=0.5, rely=0.075, anchor=tk.N)

# Botões do frame
sptrans_button = tk.Button(
    frame_sistemas, text="SPTRANS", command=sptrans, fg="black", bg="#ff2f2f")
sptrans_button.pack(pady=5, fill='both', expand=True)

# Botão para abrir o mapa da malha ferroviária e de corredores de ônibus
button_l1 = tk.Button(layout, text="Azul", command=line1,
                      fg="white", bg=azul, width=11)
button_l1.place(x=1830, y=5)
linha1_azul_icon = canvas.create_text(
    1800, 13, text="●", font="Helvetica 32", anchor="w", fill=azul)
l1_icon = canvas.create_text(
    1809, 15, text="1", font="Helvetica 10 bold", anchor="w", fill=branco)

button_l2 = tk.Button(layout, text="Verde", command=line2,
                      bg=verde, fg="white", width=11)
button_l2.place(x=1830, y=30)
linha2_verde_icon = canvas.create_text(
    1800, 38, text="●", font="Helvetica 32", anchor="w", fill=verde)
l2_icon = canvas.create_text(
    1809, 40, text="2", font="Helvetica 10 bold", anchor="w", fill=branco)

button_l3 = tk.Button(layout, text="Vermelha", command=line3,
                      bg=vermelha, fg="black", width=11)
button_l3.place(x=1830, y=55)
linha3_vermelha_icon = canvas.create_text(
    1800, 63, text="●", font="Helvetica 32", anchor="w", fill=vermelha)
l3_icon = canvas.create_text(
    1809, 65, text="3", font="Helvetica 10 bold", anchor="w", fill=preto)

button_l4 = tk.Button(layout, text="Amarela", command=line4,
                      bg=amarela, fg="black", width=11)
button_l4.place(x=1830, y=80)
linha4_amarela_icon = canvas.create_text(
    1800, 88, text="●", font="Helvetica 32", anchor="w", fill=amarela)
l4_icon = canvas.create_text(
    1809, 90, text="4", font="Helvetica 10 bold", anchor="w", fill=preto)

button_l5 = tk.Button(layout, text="Lilás", command=line5,
                      bg=lilás, fg="white", width=11)
button_l5.place(x=1830, y=105)
linha5_lilas_icon = canvas.create_text(
    1800, 113, text="●", font="Helvetica 32", anchor="w", fill=lilás)
l5_icon = canvas.create_text(
    1809, 115, text="5", font="Helvetica 10 bold", anchor="w", fill=branco)

button_l7 = tk.Button(layout, text="Rubi", command=line7,
                      bg=rubi, fg="white", width=11)
button_l7.place(x=1830, y=130)
linha7_rubi_icon = canvas.create_text(
    1800, 138, text="●", font="Helvetica 32", anchor="w", fill=rubi)
l7_icon = canvas.create_text(
    1809, 140, text="7", font="Helvetica 10 bold", anchor="w", fill=branco)

button_l8 = tk.Button(layout, text="Diamante", command=line8,
                      bg=diamante, fg="black", width=11)
button_l8.place(x=1830, y=155)
linha8_diamante_icon = canvas.create_text(
    1800, 163, text="●", font="Helvetica 32", anchor="w", fill=diamante)
l8_icon = canvas.create_text(
    1809, 165, text="8", font="Helvetica 10 bold", anchor="w", fill=preto)

button_l9 = tk.Button(layout, text="Esmeralda",
                      command=line9, bg=esmeralda, fg="black", width=11)
button_l9.place(x=1830, y=180)
linha9_esmeralda_icon = canvas.create_text(
    1800, 188, text="●", font="Helvetica 32", anchor="w", fill=esmeralda)
l9_icon = canvas.create_text(
    1809, 190, text="9", font="Helvetica 10 bold", anchor="w", fill=preto)

button_l10 = tk.Button(layout, text="Turquesa",
                       command=line10, bg=turquesa, fg="black", width=11)
button_l10.place(x=1830, y=205)
linha10_turquesa_icon = canvas.create_text(
    1800, 213, text="●", font="Helvetica 32", anchor="w", fill=turquesa)
l10_icon = canvas.create_text(
    1806, 215, text="10", font="Helvetica 10 bold", anchor="w", fill=preto)

button_l11 = tk.Button(layout, text="Coral", command=line11,
                       bg=coral, fg="black", width=11)
button_l11.place(x=1830, y=230)
linha11_coral_icon = canvas.create_text(
    1800, 238, text="●", font="Helvetica 32", anchor="w", fill=coral)
l11_icon = canvas.create_text(
    1806, 240, text="11", font="Helvetica 10 bold", anchor="w", fill=preto)

button_l12 = tk.Button(layout, text="Safira",
                       command=line12, bg=safira, fg="white", width=11)
button_l12.place(x=1830, y=255)
linha12_safira_icon = canvas.create_text(
    1800, 263, text="●", font="Helvetica 32", anchor="w", fill=safira)
l12_icon = canvas.create_text(
    1806, 265, text="12", font="Helvetica 10 bold", anchor="w", fill=branco)

button_l13 = tk.Button(layout, text="Jade", command=line13,
                       bg=jade, fg="black", width=11)
button_l13.place(x=1830, y=280)
linha13_jade_icon = canvas.create_text(
    1800, 288, text="●", font="Helvetica 32", anchor="w", fill=jade)
l13_icon = canvas.create_text(
    1806, 290, text="13", font="Helvetica 10 bold", anchor="w", fill=preto)

button_l15 = tk.Button(layout, text="Prata", command=line15,
                       bg=prata, fg="black", width=11)
button_l15.place(x=1830, y=305)
linha15_prata_icon = canvas.create_text(
    1800, 313, text="●", font="Helvetica 32", anchor="w", fill=prata)
l15_icon = canvas.create_text(
    1806, 315, text="15", font="Helvetica 10 bold", anchor="w", fill=preto)

button_guararema = tk.Button(
    layout, text="Guararema", command=guararema, bg="#f8e71c", fg="black", width=11)
button_guararema.place(x=1830, y=330)

button_pirapora = tk.Button(
    layout, text="Pirapora", command=pirapora, bg="#7ed321", fg="black", width=11)
button_pirapora.place(x=1830, y=355)

while True:
    canvas.itemconfigure(temperatura, text=get_weather())
    canvas.itemconfigure(data_hora, text=datetime.now().strftime(
        "%d/%m/%Y | %H:%M:%S | São Paulo"))
    try:
        canvas.itemconfigure(temperatura, text=get_weather())
        canvas.itemconfigure(data_hora, text=datetime.now().strftime(
            "%d/%m/%Y | %H:%M:%S | São Paulo"))
        layout.update()
    except:
        print("Ocorreu um erro de Tcl/Tkinter. Saindo do loop.")
        break