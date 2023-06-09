# # Importação padrão para utilizar o Selenium  modelo 2
# import funcoes
# import threading
# from datetime import datetime, timedelta
# import time
# import tkinter as tk


# #Acessar o filtro salvo
# filtro = [
#     "form-filtroAcss-dlgFilterPrefs-tableUser-33-j_idt349",
#     "form-filtroAcss-dlgFilterPrefs-tableUser-35-j_idt349"
#  ]

# # Definindo função que será executada após o clique no botão "Iniciar"
# def iniciar_processo():
#     # Obtendo os valores das datas dos campos de entrada
#     data_inicio_str = data_inicio.get()
#     time.sleep()
#     data_fim_str = data_fim.get()

#     # Obtendo lista de datas
#     data = funcoes.gerar_datas(data_inicio_str, data_fim_str)

#     # Iniciando processo em threads
#     x = [
#         threading.Thread(target=funcoes.definitiva, args=[filtro[0], data]),
#         threading.Thread(target=funcoes.definitiva, args=[filtro[1], data])
#     ]

#     i = 0

#     for t in x:
#         t.start()


#     # Exibindo mensagem de aguardar
#     status_label.config(text='Os dedos serão extraídos, aguarde!')

# # Criando janela
# janela = tk.Tk()
# janela.title("Extração de Dados!")

# # Definindo dimensões da janela
# largura = 400
# altura =  200

# # Obtendo resolução do sistema
# largura_tela = janela.winfo_screenwidth()
# altura_tela = janela.winfo_screenheight()

# # Calculando posição da janela na tela
# x = largura_tela/2 - largura/2
# y = altura_tela/2 - altura/2

# # Definindo geometria da janela
# janela.geometry('%dx%d+%d+%d' % (largura, altura, x, y))

# # Criando entrada de data de início
# data_inicio_label = tk.Label(janela, text='Data de Início:')
# data_inicio_label.pack(pady=10)
# data_inicio_label.pack()

# data_inicio = tk.Entry(janela)
# data_inicio.pack()

# # Criando entrada de data de fim
# data_fim_label = tk.Label(janela, text='Data de Fim:')
# data_fim_label.pack(pady=10)
# data_fim_label.pack()

# data_fim = tk.Entry(janela)
# data_fim.pack()

# # Criando botão de iniciar
# iniciar_botao = tk.Button(janela, text="Iniciar", command=iniciar_processo, width=10, height=2, bg='lightblue')
# iniciar_botao.pack(pady=10)
# iniciar_botao.pack()

# # Criando label para exibir status
# status_label = tk.Label(janela, text='')
# status_label.pack()

# # Exibindo janela
# janela.mainloop()


# # Importação padrão para utilizar o Selenium Modleo principal
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


# # Importação padrão para utilizar o Selenium Modelo  3
# import funcoes
# import threading
# from datetime import datetime, timedelta
# import time
# import tkinter as tk

# # Acessar o filtro salvo
# filtro = [
#     "form-filtroAcss-dlgFilterPrefs-tableUser-33-j_idt349",
#     "form-filtroAcss-dlgFilterPrefs-tableUser-35-j_idt349"
# ]

# # Definindo função que será executada após o clique no botão "Iniciar"
# def iniciar_processo():
#     # Obtendo os valores das datas dos campos de entrada
#     data_inicio_str = data_inicio.get()
#     data_fim_str = data_fim.get()

#     # Obtendo lista de datas
#     data = funcoes.gerar_datas(data_inicio_str, data_fim_str)

#     # Iniciando processo em threads
#     x = [
#         threading.Thread(target=funcoes.definitiva, args=[filtro[0], data]),
#         threading.Thread(target=funcoes.definitiva, args=[filtro[1], data])
#     ]

#     for t in x:
#         t.start()

#     # Esperando as threads terminarem
#     for t in x:
#         t.join()

#     # Exibindo mensagem de conclusão
#     status_label.config(text='Processo concluído!')

# # Criando janela
# janela = tk.Tk()
# janela.title("Extração de Dados!")

# # Definindo dimensões da janela
# largura = 400
# altura =  200

# # Obtendo resolução do sistema
# largura_tela = janela.winfo_screenwidth()
# altura_tela = janela.winfo_screenheight()

# # Calculando posição da janela na tela
# x = largura_tela/2 - largura/2
# y = altura_tela/2 - altura/2

# # Definindo geometria da janela
# janela.geometry('%dx%d+%d+%d' % (largura, altura, x, y))

# # Criando entrada de data de início
# data_inicio_label = tk.Label(janela, text='Data de Início:')
# data_inicio_label.pack(pady=10)

# data_inicio = tk.Entry(janela)
# data_inicio.pack()

# # Criando entrada de data de fim
# data_fim_label = tk.Label(janela, text='Data de Fim:')
# data_fim_label.pack(pady=10)

# data_fim = tk.Entry(janela)
# data_fim.pack()

# # Criando botão de iniciar
# iniciar_botao = tk.Button(janela, text="Iniciar", command=iniciar_processo, width=10, height=2, bg='lightblue')
# iniciar_botao.pack(pady=10)

# # Criando label para exibir status
# status_label = tk.Label(janela, text='')
# status_label.pack()

# # Exibindo janela
# janela.mainloop()


import funcoes
import threading
from datetime import datetime, timedelta
import time
import tkinter as tk
from tkinter import ttk

# Acessar o filtro salvo
filtro = ["form-filtroAcss-dlgFilterPrefs-tableUser-8-j_idt350",
          "form-filtroAcss-dlgFilterPrefs-tableUser-9-j_idt350"]

# Definindo função que será executada após o clique no botão "Iniciar"


def iniciar_processo():
    # Obtendo os valores das datas dos campos de entrada
    data_inicio_str = data_inicio.get()
    data_fim_str = data_fim.get()

    # Obtendo lista de datas
    data = funcoes.gerar_datas(data_inicio_str, data_fim_str)

    # Iniciando processo em threads
    threads = [
        threading.Thread(target=funcoes.definitiva, args=[filtro[0], data]),
        threading.Thread(target=funcoes.definitiva, args=[filtro[1], data])

    ]

    for t in threads:
        t.start()

    # Exibindo mensagem de aguardar e iniciando barra de progresso
    status_label.config(text='Processando...')
    progresso['maximum'] = len(data)
    progresso['value'] = 0

    while True:
        if all(not t.is_alive() for t in threads):
            break
        else:
            progresso['value'] = len(funcoes.dedos_extraidos)
            janela.update()
            time.sleep(0.1)

    # Atualizando mensagem de status e barra de progresso
    status_label.config(text='Extração concluída!')
    progresso['value'] = len(data)


# Criando janela
janela = tk.Tk()
janela.configure(bg="#fff")
janela.title("Extração de Dados!")


# adicionar imagem da empresa
img = tk.PhotoImage(file="imagem_empresa.gif")
tk.Label(janela, image=img, bg="#FFF").place(x=10, y=10)


# Definindo dimensões da janela
largura = 400
altura = 250

# Obtendo resolução do sistema
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

# Calculando posição da janela na tela
x = largura_tela/2 - largura/2
y = altura_tela/2 - altura/2

# Definindo geometria da janela
# janela.geometry('%dx%d+%d+%d' % (largura, altura, x, y))
janela.geometry("500x300")

# Criando entrada de data de início
data_inicio_label = tk.Label(janela, text='Data de Início:')
# data_inicio_label.pack(pady=10)
data_inicio_label.place(x=350, y=20)

data_inicio = tk.Entry(janela)
# data_inicio.pack()
data_inicio.place(x=350, y=40)


# Criando entrada de data de fim
data_fim_label = tk.Label(janela, text='Data de Fim:')
# data_fim_label.pack(pady=10)
data_fim_label.place(x=350, y=70)

data_fim = tk.Entry(janela)
# data_fim.pack()
data_fim.place(x=350, y=90)

# Criando botão de iniciar
iniciar_botao = tk.Button(
    janela, text="Iniciar", command=iniciar_processo, width=10, height=2, bg='lightblue')
# iniciar_botao.pack(pady=10)
iniciar_botao.place(x=350, y=120, height=25)


# Criando label para exibir status
status_label = tk.Label(janela, text='')
status_label.pack()

# Criando barra de progresso
progresso = ttk.Progressbar(janela, mode='determinate', maximum=100)
# progresso.pack(pady=10)
progresso.place(width=300, relx=0.5, rely=0.9, anchor='center')

# Exibindo janela
janela.mainloop()
