# Importação padrão para utilizar o Selenium
import funcoes
import threading
from datetime import datetime, timedelta

#Acessar o filtro salvo 

filtro = [
    "form-filtroAcss-dlgFilterPrefs-tableUser-37-j_idt349",
    "form-filtroAcss-dlgFilterPrefs-tableUser-38-j_idt349"
    ]


data_inicio_str = input("Digite a data de início (dd/mm/aaaa): ")
data_fim_str = input("Digite a data de fim (dd/mm/aaaa): ")

data = funcoes.gerar_datas(data_inicio_str, data_fim_str)

x = [    
    threading.Thread(target=funcoes.definitiva, args=[filtro[0], data]),
    threading.Thread(target=funcoes.definitiva, args=[filtro[1], data])
]

x[0].start()
x[1].start()



