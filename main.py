# Importação padrão para utilizar o Selenium
import funcoes
import threading

#Acessar o filtro salvo 

filtro = [
    "form-filtroAcss-dlgFilterPrefs-tableUser-37-j_idt349"

    ]

data = funcoes.gerar_datas()

x = [
    threading.Thread(target=funcoes.definitiva, args=[filtro[0], data])

     ]
i = 0

x[0].start()

x[1].start()


