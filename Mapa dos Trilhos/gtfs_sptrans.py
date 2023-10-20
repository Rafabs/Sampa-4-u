import csv
import webbrowser
import tkinter as tk
from tkinter import ttk, PhotoImage
from tkinter.scrolledtext import ScrolledText
import folium
from folium.plugins import MarkerCluster
from PIL import Image, ImageTk

def sptrans():
    # Criando a janela
    root = tk.Toplevel()
    root.title("Consulta de Rotas SPTrans")
    root.geometry("1920x1080")

    # Carrega a imagem usando o PIL
    image = Image.open('Mapa dos Trilhos\\Favicon\\onibus_sptrans.ico')
    photo = ImageTk.PhotoImage(image)

    # Define o ícone
    root.iconphoto(False, photo)

    def exibir_rotas():
        try:
            with open('Mapa dos Trilhos\\Gtfs_SPTRANS\\routes.txt', newline='', encoding='utf-8') as arquivo:
                leitor = csv.reader(arquivo)
                next(leitor)
                rotas = [f"{linha[2]} - {linha[3]}\n" for linha in leitor]
                resultado_text.insert(tk.END, "".join(rotas))
                return rotas
        except FileNotFoundError:
            resultado_text.insert(
                tk.END, "Arquivo 'routes.txt' não encontrado.")
            return []

    def exibir_tarifas():
        try:
            with open('Mapa dos Trilhos\\Gtfs_SPTRANS\\fare_attributes.txt', newline='', encoding='utf-8') as arquivo:
                leitor = csv.reader(arquivo)
                next(leitor)
                for linha in leitor:
                    nome = linha[0]
                    tarifa = f'R$ {float(linha[1]):.2f}'
                    tabela_tarifas.insert("", "end", values=(nome, tarifa))
        except FileNotFoundError:
            tabela_tarifas.insert("", "end", values=(
                "Arquivo 'fare_attributes.txt' não encontrado.", ""))

    def carregar_mapa():
        m = folium.Map(location=[-23.5505, -46.6333], zoom_start=12)

        shapes = {}
        caminho_arquivo_shapes = "Mapa dos Trilhos\\Gtfs_SPTRANS\\shapes.txt"

        with open(caminho_arquivo_shapes, 'r', encoding='utf-8') as arquivo_shapes:
            linhas = arquivo_shapes.readlines()
            for linha in linhas[1:]:
                dados = linha.strip().split(',')
                if len(dados) >= 4:
                    shape_id = dados[0]
                    lat = float(dados[1].strip('"'))
                    lon = float(dados[2].strip('"'))

                    if shape_id not in shapes:
                        shapes[shape_id] = []

                    shapes[shape_id].append((lat, lon))

        for shape_id, coordenadas in shapes.items():
            folium.PolyLine(coordenadas, color='red').add_to(m)

        m.save("Mapa dos Trilhos\\mapa_shapes.html")
        webbrowser.open("Mapa dos Trilhos\\mapa_shapes.html")

    def pontos():
        n = folium.Map(location=[-23.5505, -46.6333], zoom_start=12)
        marker_cluster = MarkerCluster().add_to(n)

        caminho_arquivo_stops = "Mapa dos Trilhos\\Gtfs_SPTRANS\\stops.txt"
        dados_paradas = []

        with open(caminho_arquivo_stops, 'r', encoding='utf-8') as arquivo_stops:
            leitor_csv = csv.reader(arquivo_stops)
            cabecalho = next(leitor_csv)

            for linha in leitor_csv:
                dados_paradas.append(linha)

        for dados in dados_paradas:
            stop_id, stop_name, stop_desc, stop_lat, stop_lon = dados
            stop_lat = float(stop_lat)
            stop_lon = float(stop_lon)

            folium.Marker(
                location=[stop_lat, stop_lon],
                popup=folium.Popup(f"ID: {stop_id}<br>Localização: {stop_name}<br>Descrição/Referência: {stop_desc}",
                                   max_width=300),

            ).add_to(marker_cluster)

        n.save("Mapa dos Trilhos\\mapa_paradas_cluster.html")
        webbrowser.open("Mapa dos Trilhos\\mapa_paradas_cluster.html")

    def filtrar_linhas():
        termo = campo_pesquisa.get().lower()
        linhas_filtradas = [linha for linha in rotas if termo in linha.lower()]
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, "".join(linhas_filtradas))

    # Estilos
    estilo = ttk.Style()
    estilo.configure("TButton", font=("Arial", 12), width=30)
    estilo.configure("TLabel", font=("Arial", 14))
    estilo.configure("TEntry", font=("Arial", 12))

    # Titulo
    titulo_label = ttk.Label(root, text="Consulta de Rotas SPTrans")
    titulo_label.pack(pady=(20, 30))

    # Campo de Pesquisa
    pesquisa = ttk.Label(
        root, text="Pesquisar por número ou nome da linha", foreground="red")
    pesquisa.pack(padx=20, pady=(5, 20), anchor='w',)

    campo_pesquisa = ttk.Entry(root, width=50)
    campo_pesquisa.insert(tk.END, "")
    campo_pesquisa.pack(padx=20, pady=(5, 20), anchor='w')
    campo_pesquisa.bind('<KeyRelease>', lambda event: filtrar_linhas())

    # Frame para Resultado e Tabela de Linhas
    frame_esquerdo = ttk.Frame(root)
    frame_esquerdo.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)

    # Resultado
    resultado_text = ScrolledText(
        frame_esquerdo, width=80, height=20, wrap=tk.WORD)
    resultado_text.pack(pady=(0, 20), anchor='w', fill=tk.BOTH, expand=True)

    # Frame para Botões
    frame_botoes = ttk.Frame(frame_esquerdo)
    frame_botoes.pack(pady=(0, 20), anchor='w')

    # Botões
    botao_shapes = ttk.Button(
        frame_botoes, text="Visualizar Mapa de Ruas Atendidas", command=carregar_mapa)
    botao_shapes.pack(side=tk.LEFT, padx=10)

    botao_stops = ttk.Button(
        frame_botoes, text="Visualizar Mapa com as Paradas", command=pontos)
    botao_stops.pack(side=tk.RIGHT, padx=10)

    # Tabela de Linhas
    rotas = exibir_rotas()

    # Frame para Tabela de Tarifas
    frame_direito = ttk.Frame(root)
    frame_direito.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)

    # Tabela de Tarifas
    tabela_tarifas = ttk.Treeview(frame_direito, columns=(
        "Modalidade", "Tarifa"), show="headings")
    tabela_tarifas.heading("Modalidade", text="Modalidade")
    tabela_tarifas.heading("Tarifa", text="Tarifa")
    tabela_tarifas.column("Modalidade", width=150, anchor="w")
    tabela_tarifas.column("Tarifa", width=50, anchor="w")

    # Definir a altura da tabela (por exemplo, 200 pixels)
    tabela_tarifas.config(height=200)

    # Empacotar a tabela dentro do frame
    tabela_tarifas.pack(pady=(0, 20), fill=tk.BOTH, expand=True)

    exibir_tarifas()

    root.mainloop()


if __name__ == "__main__":
    sptrans()