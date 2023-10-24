import shutil
import os

# Define o caminho do arquivo de log
log_file_path = 'Mapa dos Trilhos\\log.txt'

# Define o caminho de destino para salvar o log
dest_path = 'Mapa dos Trilhos\\'

# Verifica se o arquivo de log existe
if os.path.exists(log_file_path):
    # Move o arquivo de log para o destino especificado
    shutil.move(log_file_path, os.path.join(dest_path, 'log.txt'))
    print(f'Log salvo em: {os.path.join(dest_path, "log.txt")}')
else:
    print('Arquivo de log não encontrado.')
