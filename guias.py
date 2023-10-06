import fitz
from PIL import Image, ImageTk  # Manipular imagens

def mapa_rede():
    pdf = fitz.open('Mapa dos Trilhos\\Data\\mapa-da-rede-metro.pdf')
    imagem = pdf[0].get_pixmap()
    imagem_pil = Image.frombytes("RGB", [imagem.width, imagem.height], imagem.samples)
    imagem_pil.show()

def guia_pt_metro():
    pdf = fitz.open('Mapa dos Trilhos\\Data\\Guia_do_passageiro_abr_2022.pdf')
    imagem = pdf[0].get_pixmap()
    imagem_pil = Image.frombytes("RGB", [imagem.width, imagem.height], imagem.samples)
    imagem_pil.show()

def guia_en_metro():
    pdf = fitz.open('Mapa dos Trilhos\\Data\\Desktop_Guide_abr_2022_v2.pdf')
    imagem = pdf[0].get_pixmap()
    imagem_pil = Image.frombytes("RGB", [imagem.width, imagem.height], imagem.samples)
    imagem_pil.show()

def guia_cptm():
    pdf = fitz.open('Mapa dos Trilhos\\Data\\Regulamento-Viagem.pdf')
    imagem = pdf[0].get_pixmap()
    imagem_pil = Image.frombytes("RGB", [imagem.width, imagem.height], imagem.samples)
    imagem_pil.show()

def guia_cptm_expresso_turistico():
    pdf = fitz.open('Mapa dos Trilhos\\Data\\Regulamento de Viagem Expresso Turístico.pdf')
    imagem = pdf[0].get_pixmap()
    imagem_pil = Image.frombytes("RGB", [imagem.width, imagem.height], imagem.samples)
    imagem_pil.show()