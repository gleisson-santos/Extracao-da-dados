# Importação padrão para utilizar o Selenium
import funcoes
import threading


filtro = [
    "form-filtroAcss-dlgFilterPrefs-tableUser-0-j_idt349",
    "form-filtroAcss-dlgFilterPrefs-tableUser-1-j_idt349",
    "form-filtroAcss-dlgFilterPrefs-tableUser-7-j_idt349",
    "form-filtroAcss-dlgFilterPrefs-tableUser-8-j_idt349",
    "form-filtroAcss-dlgFilterPrefs-tableUser-9-j_idt349",
    ]
data = funcoes.gerar_datas()


x = [
    threading.Thread(target=funcoes.definitiva, args=[filtro[0], data]),
    threading.Thread(target=funcoes.definitiva, args=[filtro[1], data]),
    threading.Thread(target=funcoes.definitiva, args=[filtro[2], data]),
    threading.Thread(target=funcoes.definitiva, args=[filtro[3], data]),
    threading.Thread(target=funcoes.definitiva, args=[filtro[4], data])
     ]
i = 0

x[0].start()

x[1].start()

x[2].start()

x[3].start()

x[4].start()
