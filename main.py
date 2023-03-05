# Importação padrão para utilizar o Selenium
import funcoes
import threading
from datetime import datetime, timedelta
import time
import tkinter as tk


#Acessar o filtro salvo 
filtro = [    "form-filtroAcss-dlgFilterPrefs-tableUser-37-j_idt349",    "form-filtroAcss-dlgFilterPrefs-tableUser-38-j_idt349"]

# Definindo função que será executada após o clique no botão "Iniciar"
def iniciar_processo():
    # Obtendo os valores das datas dos campos de entrada
    data_inicio_str = data_inicio.get()
    data_fim_str = data_fim.get()
    
    # Obtendo lista de datas
    data = funcoes.gerar_datas(data_inicio_str, data_fim_str)

    # Iniciando processo em threads
    x = [    
        threading.Thread(target=funcoes.definitiva, args=[filtro[0], data]),
        threading.Thread(target=funcoes.definitiva, args=[filtro[1], data])
    ]

    x[0].start()
    time.sleep(0.6)
    x[1].start()
    
    # Exibindo mensagem de aguardar
    status_label.config(text='Os dedos serão extraídos, aguarde!')

# Criando janela
janela = tk.Tk()
janela.title("Extração de Dados")

# Definindo dimensões da janela
largura = 400
altura =  200

# Obtendo resolução do sistema
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

# Calculando posição da janela na tela
x = largura_tela/2 - largura/2
y = altura_tela/2 - altura/2

# Definindo geometria da janela
janela.geometry('%dx%d+%d+%d' % (largura, altura, x, y))

# Criando entrada de data de início
data_inicio_label = tk.Label(janela, text='Data de Início:')
data_inicio_label.pack(pady=10)
data_inicio_label.pack()

data_inicio = tk.Entry(janela)
data_inicio.pack()

# Criando entrada de data de fim
data_fim_label = tk.Label(janela, text='Data de Fim:')
data_fim_label.pack(pady=10)
data_fim_label.pack()

data_fim = tk.Entry(janela)
data_fim.pack()

# Criando botão de iniciar
iniciar_botao = tk.Button(janela, text="Iniciar", command=iniciar_processo, width=10, height=2, bg='lightblue')
iniciar_botao.pack(pady=10)
iniciar_botao.pack()

# Criando label para exibir status
status_label = tk.Label(janela, text='')
status_label.pack()

# Exibindo janela
janela.mainloop()






# # Importação padrão para utilizar o Selenium
# import funcoes
# import threading
# from datetime import datetime, timedelta
# import time

# #Acessar o filtro salvo 

# filtro = [
#     "form-filtroAcss-dlgFilterPrefs-tableUser-37-j_idt349",
#     "form-filtroAcss-dlgFilterPrefs-tableUser-38-j_idt349"
#     ]

# data_inicio = input("Digite a data de início (dd/mm/aaaa): ")
# data_fim = input("Digite a data de fim (dd/mm/aaaa): ")

# data = funcoes.gerar_datas(data_inicio, data_fim)

# x = [
#     threading.Thread(target=funcoes.definitiva, args=[filtro[0], data]),
#     threading.Thread(target=funcoes.definitiva, args=[filtro[1], data])

#      ]

# x[0].start()
# time.sleep(1)
# x[1].start()



